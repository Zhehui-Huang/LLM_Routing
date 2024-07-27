import math
import pulp

# Coordinates of cities including the depot city
coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n = len(coordinates)
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Formulating the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat='Binary')

# Objective
problem += pulp.lpSum([dist_matrix[i][j] * x[i][j] for i in range(n) for j in range(n)])

# Constraints
for i in range(n):
    problem += (pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1)
    problem += (pulp.lpSum([x[j][i] for j in range(n) if i != j]) == 1)

# Subtour elimination using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
problem.solve()

# Extract solution
tour = []
current_city = 0
visited = [False] * n
total_cost = 0

while True:
    visited[current_city] = True
    found_next_city = False
    for next_city in range(n):
        if pulp.value(x[current_city][next_city]) == 1 and not visited[next_city]:
            tour.append(current_city)
            total_cost += dist_matrix[current_city][next_city]
            current_city = next_city
            found_next_city = True
            break
    if not found_next_city:
        break

# Completing the tour by returning to the depot
tour.append(current_city)
tour.append(0)  # Return to the depot
total_cost += dist_matrix[current_city][0]

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_cost)