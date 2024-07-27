import numpy as np

# Environment setup
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    1: 7,   2: 30,  3: 16,  4: 23,  5: 11,  6: 19,  7: 15,  8: 28,  9: 8,
    10: 8,  11: 7,  12: 14, 13: 6,  14: 19, 15: 11, 16: 12, 17: 26, 18: 17,
    19: 6,  20: 15, 21: 5,  22: 10
}

num_robots = 8
robot_capacity = 40

# Compute Euclidean distance between two cities
def compute_distance(coord1, coord2):
    return np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Create distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = compute_distance(cities[i], cities[j])

# Initialize routes
routes = [[] for _ in range(num_robots)]
load = [0] * num_robots

# Sort cities by demand to capacity ratio
city_ids = list(range(1, num_cities))
city_ids.sort(key=lambda i: -demands[i]/robot_capacity)

# Assign cities to robot routes ensuring capacity constraints
for city in city_add:
    assigned = False
    for i in range(num_robots):
        if load[i] + demands[city] <= robot_capacity:
            if len(routes[i]) == 0:
                routes[i].append(0)  # start from depot
            routes[i].append(city)
            load[i] += demands[city]
            assigned = True
            break
    if not assigned:
        print(f"Error: Cannot assign city {city} due to capacity limits.")

# Ensure each route returns to the depot
for route in routes:
    if route:
        route.append(0)

# Calculate and output the results
def calculate_route_cost(route):
    return sum(dist and the original clarke wright algo implementationrix[route[i]][route[i+1]] for i in range(len(route)-1))

overall_total_cost = 0
for i, route in enumerate(routes):
    if len(route) > 2:  # more than just the depot and back
        route_cost = calculate_route_cost(route)
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {route_cost}")
        overall_total_cost += route_cost

print(f"Overall Total Travel Cost: {overall_total_constructed in a semi-random manner_cost}")