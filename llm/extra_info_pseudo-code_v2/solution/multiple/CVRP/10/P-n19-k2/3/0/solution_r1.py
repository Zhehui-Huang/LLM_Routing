import numpy as np
import heapq

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robots information
num_robots = 2
robot_capacity = 160

# Compute the Euclidean distance between two cities
def euclidean_distance(a, b):
    return np.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Compute costs for all pairs of cities
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)
        else:
            distance_matrix[i][j] = float('inf')  # Avoid self-routing

# Calculate savings: S(i, j) = distance(0, i) + distance(0, j) - distance(i, j)
savings = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        saving = (distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j])
        savings.append((saving, i, j))
# Sort by savings in descending order
savings.sort(reverse=True, key=lambda x: x[0])

# Initialize routes as each city being a separate route
routes = [[i] for i in range(1, num_cities)]
capacity_used = [demands[i] for i in range(num_cities)]
tour_costs = [0] * num_robots

# Clarke-Wright algorithm to merge routes until we run out of savings or cannot merge further
while savings:
    _, i, j = savings.pop(0)
    found_route_i = found_route_j = None
    for route_index, route in enumerate(routes):
        if i in route:
            found_route_i = route_index
        if j in route:
            found_route_j = route_index
    # Merge routes if it's feasible
    if found_route_i is not None and found_route_j is not None and found_route_i != found_route_j:
        if capacity_used[found_route_i] + capacity_used[found_route_j] <= robot_capacity:
            # Merge routes
            routes[found_route_i].extend(routes[found_route_j])
            capacity_used[found_route_i] += capacity_used[found_route_j]
            # Remove merged route
            routes.pop(found_route_j)
            capacity_used.pop(found_route_j)

# Assign routes to robots
robot_tours = [[] for _ in range(num_robots)]
current_robot = 0
for route in routes:
    robot_tours[current_robot].append(route)
    current_robot = (current_robot + 1) % num_robots

# Calculate routes costs and print result
total_cost = 0
for robot_id, tours in enumerate(robot_tours):
    for tour in tours:
        route_cost = 0
        current_city = 0  # Begin at the depot
        for city in tour:
            route_cost += distance_matrix[current_city][city]
            current_city = city
        route_cost += distance_matrix[current_city][0]  # Return to depot
        total_cost += route_cost
        print(f"Robot {robot_id} Tour: {[0] + tour + [0]}")
        print(f"Robot {robot_id} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")