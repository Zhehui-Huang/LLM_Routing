import pulp
import numpy as np
from scipy.spatial.distance import euclidean

# Data setup
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), 
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), 
    (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
depots = list(range(7 + 1))
num_cities = len(cities_coordinates)

# Calculating the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean(cities_coordinates[i], cities_coordinates[j])

# Problem setup
model = pulp.LpProblem("Multi-Depot Vehicle Routing", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((k, i, j) for k in depots 
                                for i in range(num_cities) 
                                for j in range(num_cities) if i != j), 
                          cat='Binary')

# Create helper variable for sub-tour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(num_cities) if i not in depots), 
                          lowBound=0, upBound=len(cities_coordinates), cat='Continuous')

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[k, i, j] 
                    for k in depots
                    for i in range(num_cities)
                    for j in range(num_cities) 
                    if i != j)

# Constraints
for k in depots:
    model += pulp.lpSum(x[k, k, j] for j in range(num_cities) if j != k) == 1  # Leave depot
    model += pulp.lpSum(x[k, i, k] for i in range(num_cities) if i != k) == 1  # Return to depot

for j in range(num_cities):
    if j not in depots:
        model += pulp.lpSum(x[k, i, j] for k in depots for i in range(num_cities) if i != j) == 1  # Each city visited once by any vehicle

for k in depots:
    for i in range(num_cities):
        if i not in depots:
            model += pulp.lpSum(x[k, i, j] for j in range(num_cities) if j != i) - pulp.lpSum(x[k, j, i] for j in range(num_cities) if j != i) == 0

# Subtour Elimination
for i in range(num_cities):
    for j in range(num_cities):
        if i not in depots and j not in depots and i != j:
            for k in depots:
                model += u[i] - u[j] + (num_cities - len(depots)) * x[k, i, j] <= num_cities - len(depots) - 1

# Solve problem
model.solve()

# Extract the routes from the solution
tours = {}
for k in depots:
    tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[k, i, j]) == 1:
                tour.append((i, j))
    tours[k] = tour

# Print the results
total_cost = 0
for k, tour in tours.items():
    print(f"Robot {k} Tour: {tour}")
    tour_cost = sum(distance_matrix[i][j] for i, j in tour)
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")