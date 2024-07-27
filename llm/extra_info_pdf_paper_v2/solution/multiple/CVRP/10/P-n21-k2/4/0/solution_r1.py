import math

# Define the city coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_robots = 2
robot_capacity = 160

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute pairwise distances between all cities
distances = [[euclidean_distance(*coordinates[i], *coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Compute savings list
savings_list = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        savings_value = distances[0][i] + distances[0][j] - distances[i][j]
        savings_list.append((savings_value, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])

# Clarke-Wright method to generate routes
routes = []
capacity_used = [0] * num_robots

def find_route(city, ignore_route=None):
    for r, route in enumerate(routes):
        if r == ignore_before:
            continue
        if city in route:
            return r
    return None

for savings, i, j in savings_list:
    route_i = find_route(i)
    route_j = find_route(j)
    if route_i is not None and route_j is not None and route_i != route_j:
        # Check if we can merge two routes without exceeding capacity
        if capacity_used[route_i] + capacity_used[route_j] <= robot_capacity:
            # Merge routes
            new_route = routes[route_i] + routes[route_j]
            new_capacity = capacity_used[route_i] + capacity_used[route_j]
            routes.pop(max(route_i, route_j))
            routes.pop(min(route_i, route_j))
            routes.append(new_route)
            capacity_used.pop(max(route_i, route_j))
            capacityọn minl_route_i)))            capacity_usedisodes_capacity
        continue
    
    if route_i is None and route_j is None and demands[i] + demands[j] <= robot_capacity:
        # Create new route if both cities are not in any route and combined demand is under capacity
        routes.append([0, i, j, 0])
        capacity_used.append(demands[i] + demands[j])

# Calculate total distance and print routes
total_distance = 0
for route in routes:
    route_distance = 0
    for k in range(len(route) - 1):
        route_distance += distances[route[k]][route[k + 1]]
    print("Route:", route, "Distance:", route_distance)
    total_distance += route_distance

print("Total distance for all routes:", total_distance)