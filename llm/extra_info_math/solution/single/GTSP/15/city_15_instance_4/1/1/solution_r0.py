import pulp
import math

# City Coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]
groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculating the distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables x_ij where i, j represent the city connection
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective Function
model += pulp.lpSum([x[(i, j)] * distance_matrix[i][j] for i in range(n) for j in range(n) if i != j])

# Each group should have exactly 1 outgoing and 1 incoming connection
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in set(range(n)) - set(group)) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in set(range(n)) - set(group)) == 1

# Ensuring flow conservation at every city
for i in range(n):
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == pulp.lpSum(x[(i, j)] for j in range(n) if i != j)

# Continuity / Subtour elimination (Creating artificial variables u)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n, cat=pulp.LpContinuous)
num_groups = len(groups) + 1
for i in range(n):
    for j in range(n):
        if i != j:
            for p in range(1, num_groups):
                for q in range(1, num_groups):
                    if p != q:
                        model += u[p] - u[q] + n * x[(i, j)] + (n-2) * x[(j, i)] <= n - 1

# Solving the problem
status = model.solve()

# Retrieve solution
tour = [0]
while len(tour) <= len(groups):
    for j in range(n):
        if j != tour[-1] and pulp.value(x[(tour[-1], j)]) == 1:
            tour.append(j)
            break

tour.append(0)  # Return to depot
travel_cost = sum([distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])

print("Tour:", tour)
print("Total travel cost:", travel_cost)