import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger

# Define the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
num_cities = len(coordinates)
depots = num_cities - 1  # all but the last are considered depots in the example
num_robots = 8

# Distances matrix calculation using Euclidean distance
def euclidean_dist(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_dist(coordinates[i], coordinates[j])

# LP model
model = LpProblem("Robot_Routing_Problem", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities)], cat='Binary')

# Objective function
model += lpSum(distance_matrix[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities))

# Constraints
# Each city is visited exactly once
for j in range(1, num_cities):
    model += lpSum(x[i, j] for i in range(num_cities)) == 1
for i in range(1, num_cities):
    model += lpSum(x[i, j] for j in range(num_cities)) == 1

# Continuity and subtour elimination
u = LpVariable.dicts("u", range(num_cities), lowBound=0, upBound=num_cities - 1, cat=LpInteger)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            model += u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1

# Robots must leave the starting depot
model += lpSum(x[0, j] for j in range(1, num_cities)) == num_robots

# Solve Model
model.solve()

# Extract tours
tours = []
for k in range(num_cities):
    tour = []
    i = k
    while True:
        tour.append(i)
        i = next((j for j in range(num_cities) if x[i, j].varValue == 1), None)
        if i is None or i == k:
            break
    if tour:
        tours.append(tour)

# Print results
total_cost = 0
for idx, tour in enumerate(tours):
    if len(tour) > 1:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")