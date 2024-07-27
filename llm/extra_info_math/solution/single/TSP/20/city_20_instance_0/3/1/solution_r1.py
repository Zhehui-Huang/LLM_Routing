import pulp
import math
import itertools

# City coordinates
city_coords = [
    (8, 11),  # depot city
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), 
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
    (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(city_coords)  # number of cities including depot

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
c = [[euclidean.value(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
model += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city

# Subtour elimination constraints
for S in range(3, n+1):
    for subset in itertools.combinations(range(1, n), S):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Check model status
if status != pulp.LpStatusOptimal:
    print("Optimal solution was not found.")
else:
    # Retrieve the optimal tour
    tour = []
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j]) == 1:
                tour.append((i, j))

    # Reorder the tour from the starting city (depot 0)
    ordered_tour, current_city = [0], 0
    while len(ordered_tour) < n:
        for i in range(n):
            if x[current_city, i].varValue == 1:
                ordered_tour.append(i)
                current_city = i
                break
    ordered_tour.append(0)  # return to depot

    # Calculate the travel cost
    total_cost = sum(c[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))

    print("Tour:", ordered_tour)
    print("Total travel cost:", total_cost)