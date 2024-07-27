import math
from itertools import combinations

# Cities coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Calculate pairwise distances and savings
distance_matrix = {}
savings_list = []

for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        distance_matrix[(i, j)] = distance_matrix[(j, i)] = euclidean_distance(i, j)
        if i != 0 and j != 0:  # Savings only for pairs involving cities not the depot
            savings = distance_matrix[(0, i)] + distance_matrix[(0, j)] - distance_matrix[(i, j)]
            savings_list.append((savings, i, j))

# Sort savings in descending order
savings_list.sort(reverse=True, key=lambda x: x[0])

# Initialize routes for each city except the depot
routes = {i: [0, i, 0] for i in range(1, len(coordinates))}

# Clarke-Wright algorithm to merge routes
for savings, i, j in savings_list:
    # Ensure routes are mergeable and not exceeding capacity constraints
    if routes[i][0] == 0 and routes[j][-1] == 0 and routes[i][-2] != j:
        merged_route = routes[i][:-1] + routes[j][1:]
        total_demand = sum(demands[city] for city in merged_route if city != 0)

        if total_demand <= robot_capacity:
            # Merge the routes
            routes[i] = merged_route
            routes[j] = []  # Invalidate the old route of j

# Filter out empty routes and prepare final route assignments
final_routes = [route for route in routes.values() if route]
assigned_routes = [([], 0) for _ in range(num_robots)]  # (route, total_distance)

# Assign routes to robots
for route in final:<|...|># Filter out empty routes and prepare final route assignments
final_routes = [route for route in routes.values() if route]
for i, route in enumerate(final_routes):
    robot_index = i % num_robots
    assigned_routes[robot_index][0].append(route)
    route_distance = sum(distance_matrix[(route[i], route[i+1])] for i in range(len(route)-1))
    assigned_routes[robot_index] = (assigned_routes[robot_index][0], assigned_routes[robot_index][1] + route_distance)

# Output results
total_cost = 0
for i, (routes, cost) in enumerate(assigned_routes):
    print(f'Robot {i} Tours:')
    for route in routes:
        print(f'    {route}')
    print(f'Robot {i} Total Travel Cost: {cost}')
    total_cost += cost

print(f'Overall Total Travel Cost: {total_cost}')