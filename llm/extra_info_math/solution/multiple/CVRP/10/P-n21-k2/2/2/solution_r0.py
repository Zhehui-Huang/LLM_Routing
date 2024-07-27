import math
from collections import defaultdict

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands for each city (including depot which has 0 demand)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Number of vehicles and their capacity
num_vehicles = 2
capacity = 160

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute distance matrix
n = len(coordinates)
distance = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Clarke and Wright Savings Algorithm
def clarke_and_wright():
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = distance[0][i] + distance[0][j] - distance[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = {i: [0, i, 0] for i in range(1, n)}
    used = set()

    for _, i, j in savings:
        if i in used or j in used:
            continue
        if demands[i] + demands[j] > capacity:
            continue

        # Check if they can be merged
        route_i = routes[i]
        route_j = routes[j]
        if route_i[-2] == i and route_j[1] == j:
            # Merge j after i
            new_route = route_i[:-1] + route_j[1:]
            new_demand = sum([demands[k] for k in new_route if k != 0])
            if new_demand <= capacity:
                del routes[j]
                routes[i] = new_route
                used.add(j)
    
    return list(routes.values())

tours = clarke_and_wright()
total_cost = 0
for i, tour in enumerate(tours):
    cost = sum(distance[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Note: This code needs adjustments based on actual constraints on number of routes (vehicles)