import math
import numpy as np

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Parameters
number_of_robots = 4
capacity = 6000

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor Heuristic Function
def nearest_neighbor_cvrp(demands, capacity, distance_matrix):
    n = len(demands)
    robots_routes = []
    demand_fulfilled = np.zeros(n)
    for _ in range(number_of_robots):
        current_city = 0
        route = [current_city]
        used_capacity = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for j in range(1, n):
                if j not in route and demands[j] <= (capacity - used_capacity) and demand_fulfilled[j] == 0:
                    if distance_matrix[current_city][j] < min_distance:
                        min_distance = distance_matrix[current_city][j]
                        next_city = j
            if next_city is None:
                break
            route.append(next_city)
            used_capacity += demands[next_city]
            demand_fulfilled[next_city] = 1
            current_city = next_city
        if len(route) > 1:
            route.append(0)  # Return to depot
            robots_routes.append(route)
    return robots_routes

# Solve CVRP using the nearest neighbor heuristic
routes = nearest_neighbor_cvrp(demands, capacity, distance_matrix)

# Calculate route costs and print results
total_travel_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_travel_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")