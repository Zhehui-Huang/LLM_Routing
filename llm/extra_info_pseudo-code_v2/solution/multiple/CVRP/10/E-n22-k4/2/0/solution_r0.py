import numpy as np
from scipy.spatial import distance
from collections import defaultdict, deque

# Cities coordinates and demands
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
               (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300,
           1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot capacity
capacity = 6000

# Calculate cost matrix
n = len(coordinates)
cost_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i][j] = distance.euclidean(coordinates[i], coordinates[j])

# Calculate savings
savings = []
for i in range(1, n):
    for j in range(i+1, n):
        savings.append(((i, j), cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]))
savings.sort(key=lambda x: x[1], reverse=True)

# Solution containers
routes = []
assigned = set()

# Greedy assignment based on savings
for (i, j), saving in savings:
    if i not in assigned and j not in assigned and demands[i] + demands[j] <= capacity:
        routes.append([0, i, j, 0])
        assigned.update({i, j})

# Assign unvisited cities
for i in range(1, n):
    if i not in assigned:
        if demands[i] <= capacity:
            routes.append([0, i, 0])
            assigned.add(i)

# Calculate route costs for the initial greedy solution
total_costs = []
for route in routes:
    cost = sum(costMatrix[route[k]][route[k+1]] for k in range(len(route)-1))
    total_costs.append(cost)

# Display results
total_travel_cost = sum(total_costs)
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Animeed: {total_costs[idx]}")
print(f"Overall Total Travel Anime: {total_travel_cost}")