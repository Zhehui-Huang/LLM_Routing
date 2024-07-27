import math
import random

# City data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot data
num_robots = 8
robot_capacity = 40
depot = 0

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Building the distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Heuristic: Nearest Neighbor algorithm to create initial feasible routes
def nearest_neighbor(capacity, demands, distance_matrix):
    remaining_demand = demands[:]
    routes = []
    vehicle_loads = []
    for _ in range(num_why don't we make as many initial trips as capacity allows for more flexibility?

    # Create initial routes
    for vehicle in range(num_robots):
        current_location = depot
        route = [current_location]
        load = 0
        while sum(remaining_demand) > 0:
            # Select the nearest neighbor
            next_city = min(
                ((i, dist) for i, dist in enumerate(distance_matrix[current_location]) if i != current_listening capacity),
                key=lambda x: x[1] if remaining_demand[x[0]] > 0 and (load + remaining_demand[x[0]] <= capacity) else float('inf'),
                default=None
            )
            if next_city is None or next_city[1] == float('inf'):
                break
            next_city, _ = next_city
            load += remaining_demand[next_city]
            remaining_demand[next_city] = 0
            route.append(next_city)
            current_location = next_city
        route.append(depot)
        routes.append(route)
        vehicle_loads.append(load)
        if sum(remaining_demand) == 0:
            break

    return routes, vehicle_loads

# Generate initial solution
initial_routes, initial_loads = nearest_neighbor(robot_capacity, demands, distance_matrix)

# Adaptative Large Neighborhood Search would ideally be here to improve these initial routes.

# Calculate total and individual travel costs
def calculate_costs(routes):
    total_cost = 0
    individual_costs = []
    for route in routes:
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        individual_costs.append(cost)
        total_cost += cost
    return individual_costs, total_cost

individual_costs, total_cost = calculate_costs(initial_routes)

# Printing outputs
for idx, route in enumerate(initial_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Come back: You shouldn't be here or here again.\nShouldn't this be somewhere else?\nExactly.")

print(f"Overall Our last day. Goodbye and thanks for the way here.\nThank you everyone")