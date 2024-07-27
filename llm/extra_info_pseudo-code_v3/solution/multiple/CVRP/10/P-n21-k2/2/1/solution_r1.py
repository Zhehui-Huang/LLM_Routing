import numpy as np

# Coordinates and demands of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot information
num_robots = 2
robot_capacity = 160

# Distance matrix computation
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = np.array([
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
])

# Initialize routes with a simple greedy solution
def initialize_routes():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity] * num_robots
    cities_to_visit = list(range(1, len(coordinates)))  # Exclude depot city 0

    # Allocate cities to robots trying to minimize excess travel
    while cities_to_visit:
        for idx in range(num_robots):
            if not cities_to_visit:
                break
            for city in cities_to_visit[:]:
                if demands[city] <= capacity_remaining[idx]:
                    if not routes[idx] or distance_matrix[routes[idx][-1]][city] <= distance_matrix[0][city]:
                        routes[idx].append(city)
                        capacity_remaining[idx] -= demands[city]
                        cities_to_visit.remove(city)
    
    # Add depot to the start and end of each route
    for route in routes:
        route.insert(0, 0)
        route.append(0)
        
    return routes

# Calculate travel cost for a given route
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

# Main execution
routes = initialize_routes()

# Calculate costs
total_cost = 0
for i, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    total_cost += route_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")