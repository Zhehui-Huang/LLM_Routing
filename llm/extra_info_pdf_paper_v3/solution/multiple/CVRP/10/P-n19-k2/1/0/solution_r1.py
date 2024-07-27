import numpy as np

# City coordinates (including the depot)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city (excluding the depot)
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]

# Total number of robots and their capacities
num_robots = 2
capacity = 160

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Precompute distances
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Simple greedy heuristic to assign cities to routes based on demand and capacity
def assign_routes(demands, capacity, distances):
    remaining_demands = demands.copy()
    routes = []
    costs = []
    
    for _ in range(num_robots):
        load = 0
        current_route = [0]  # start from the depot
        current_capacity = capacity
        while any(remaining_demands[1:]):  # while there are still demands
            last_city = current_route[-1]
            next_city = None
            closest_distance = float('inf')
            for city in range(1, num_cities):  # find the nearest city with demand and capacity available
                if remaining_demands[city] > 0 and remaining_demands[city] <= current_capacity:
                    if distances[last_city][city] < closest_distance:
                        closest_distance = distances[last_city][city]
                        next_city = city
            if next_city is not None:
                current_route.append(next_city)
                current_capacity -= remaining_demands[next_city]
                remaining_demands[next_city] = 0
                if current_capacity < min([d for d in remaining_demands if d > 0], default=float('inf')):
                    break
            else:  # no suitable city found or capacity issue
                break
        current_route.append(0)  # return to depot
        routes.append(current_route)
        route_cost = sum(distances[current_route[i]][current_route[i + 1]] for i in range(len(current_route) - 1))
        costs.append(route_cost)
    
    return routes, costs

routes, costs = assign_routes(demands, capacity, distances)
overall_cost = sum(costs)

# Output results
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")