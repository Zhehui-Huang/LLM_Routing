import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations
import pulp
import math

# Given data
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

number_of_robots = 8
robot_start_end = [i for i in range(8)]  # Each robot i starts and ends at depot i

# Calculate distance matrix
distance_matrix = distance_matrix(cities_coordinates, cities_coordinates)
distance_matrix = np.round(distance_link_matrix, 2)

# Number of cities including depots
num_cities = len(cities_coordinates)

# Optimization model
model = pulp.LpProblem("Multi_Depot_VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in robot_start_end], cat='Binary')

# Objective function
objective = pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities) for k in robot_start_end)
model += objective

# Constraints
# Each robot returns to its starting point
for k in robot_start_end:
    model += pulp.lpSum(x[i, k, k] for i in range(num_cities)) == 1, f"Return_to_start_{k}"
    model += pulp.lpSum(x[k, j, k] for j in range(num_cities)) == 1, f"Start_from_start_{k}"

# Each non-depot city is visited exactly once across all salesmen
for j in range(num_cities):
    if j not in robot_start_end:
        model += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in robot_start_end) == 1, f"Visit_{j}"

# Subtour elimination constraints and continuity
for k in robot_start_end:
    for i in range(num_cities):
        if i != k:
            model += pulp.lpSum(x[i, j, k] for j in range(num_cities)) - pulp.lpSum(x[j, i, k] for j in range(num_cities)) == 0, f"Continuity_{i}_{k}"

# Solve the model
status = model.solve()

# Output results
tours = []
total_cost = 0

for k in robot_start_end:
    tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tour.append(i)
                tour.append(j)
                break
    # Remove duplicates while keeping order, reconstruct tour from segments
    seen = set()
    tour = [x for x in tour if not (x in seen or seen.add(x))]
    
    # Calculate cost of this tour
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost
    tours.append(tour)

print(f"Overall Total Travel Cost: {total_cost}")