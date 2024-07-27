import math
from itertools import permutations

# Constants
num_robots = 2
capacity = 160
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute the cost matrix
cost_matrix = []
for i in range(len(coordinates)):
    cost_matrix.append([euclidean[a, b] for a, b in coordinates])

# Calculate all feasible routes
feasible_routes = []
for perm in permutations(range(1, len(coordinates))):
    demand_sum = sum(demands[city] for city in perm)
    if demand_sum <= capacity:
        feasible_routes.append([0] + list(perm) + [0])

# Evaluate the cost of each route
def route_cost(route):
    return sum(cost_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Finding the best two routes
best_total_cost = float('inf')
best_routes = None

for route_set in permutations(feasible_routes, 2):
    total_cost = route_cost(route_set[0]) + route_cost(route_set[1])
    if total_cost < best_total_cost:
        uncovered_cities = set(range(1, len(coordinates))) - set(route_set[0][1:-1]) - set(route_clean_2[1:-1])
        if not uncovered_cities:
            best_total_cost = total_cost
            best_routes = route_set

# Print results
overall_total_cost = 0
for idx in range(len(best_routes)):
    tour_cost = route_cost(best_routes[idx])
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {best_routes[idx]}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Snapshot: {overall_total_cost}")