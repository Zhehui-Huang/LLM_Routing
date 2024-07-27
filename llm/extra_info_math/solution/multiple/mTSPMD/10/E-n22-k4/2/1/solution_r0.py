import numpy as np
from scipy.spatial.distance import euclidean
from pulp import LpMinimize, LpProblem, LpVariable, LpBinary, lpSum

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots and their corresponding depots
depots = [0, 1, 2, 3]
robots = 4

# Calculate the distance matrix
n = len(cities)
distance_matrix = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Model setup
model = LpProblem("VRP_with_Multiple_Depots", LpMinimize)

# Decision Variables
x = {(i, j, k): LpVariable(f"x_{i}_{j}_{k}", cat=LpBinary) for i in range(n) for j in range(n) for k in depots}

# Objective Function: Minimize the sum of the travel distances
model += lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in range(n) for j in range(n)), "Total_Cost"

# Constraints
for j in range(n):
    if j not in depots:
        model += lpSum(x[i, j, k] for i in range(n) for k in depots) == 1, f"One_Visit_{j}"

for k in depots:
    model += lpSum(x[k, j, k] for j in range(n) if j != k) == 1, f"Leave_{k}"
    model += lpSum(x[j, k, k] for j in range(n) if j != k) == 1, f"Return_{k}"
    
    # Continuity within a route for each depot
    for i in range(n):
        if i != k:
            model += lpSum(x[i, j, k] for j in range(n) if j != i) == lpSum(x[j, i, k] for j in range(n) if j != i), \
                     f"Continuity_at_{i}_for_{k}"

# Execute solver
model.solve()

# Outputs
for k in depots:
    tour = [k]
    next_location = k
    while True:
        next_location = [j for j in range(n) if j != next_location and x[next_location, j, k].varValue == 1][0]
        if next_location == k:
            break
        tour.append(next_location)
    tour.append(k)
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost:.2f}")

overall_cost = sum(distance_matrix[tour[i]][tour[i+1]] for k in depots for i, next_location in enumerate(tour[:-1]) if x[tour[i], tour[i+1], k].varValue == 1)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")