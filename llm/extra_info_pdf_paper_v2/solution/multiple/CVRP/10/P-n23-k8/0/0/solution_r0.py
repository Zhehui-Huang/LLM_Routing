import math
from itertools import combinations

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Calculate all initial distances and savings
distance_matrix = {}
savings_list = []
for i, j in combinations(range(len(coordinates)), 2):
    dist = euclidean_distance(i, j)
    distance_matrix[(i, j)] = dist
    distance_matrix[(j, i)] = dist
    if i != 0 and j != 0:
        savings = euclidean_distance(i, 0) + euclidean_distance(0, j) - dist
        savings_list.append((savings, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])

# Initialize routes for each robot as empty routes with just the depot
routes = {r: [0] for r in range(num_robots)}

# Clarke-Wright Savings Algorithm implementation
def assign_delivery():
    city_delivery = {i: demands[i] for i in range(1, len(demands))}
    for savings, i, j in savings_list:
        if city_delivery[i] > 0 and city_delivery[j] > 0:
            # Check which robot can take this connection based on capacity and current assignment
            for robot_id in range(num_robots):
                route = routes[robot_id]
                if (route[-1] == i or route[-1] == 0) and (city_delivery[i] + city_delivery[j] <= robot_capacity):
                    # Do the connection
                    if route[-1] == i:
                        route.append(j)
                    else:
                        route.extend([i, j])
                    robot_capacity_remaining = robot_capacity - city_delivery[i] - city_delivery[j]
                    # Adjust deliveries and capacity
                    city_delivery[i], city_delivery[j] = 0, 0
                    break

assign_delivery()

# Adding return to depot and calculating cost
total_cost = 0
for robot_id, route in routes.items():
    if len(route) > 1 and route[-1] != 0:
        route.append(0)
    route_cost = sum(distance_matrix[(route[k], route[k + 1])] for k in range(len(route) - 1))
    total_cost += route_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")