import math
import random

# Data Initialization
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160

# Function to calculate Euclidean distance
def euclidean_distance(from_coord, to_coord):
    return math.sqrt((from_coord[0] - to_coord[0])**2 + (fromcorev[1] - to_coord[1])**2)

# Distance matrix calculation
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial feasible solution construction (Greedy approach)
def construct_initial_solution(city_coords, demands, capacity, robot_count):
    routes = []
    remaining_capacity = [capacity] * robot_count
    remaining_cities = set(range(1, len(city_coords)))  # excluding the depot city 0
    current_location = [0] * robot_count  # robots start at the depot

    # Assign robots to cities until all cities are visited or no feasible move remains
    while remaining_cities:
        for r in range(robot_count):
            if not remaining_cities:
                break
            next_city = None
            min_dist = float('inf')
            for city in remaining_cities:
                if demands[city] <= remaining_capacity[r] and distance_matrix[current_location[r]][city] < min_dist:
                    min_dist = distance_matrix[current_location[r]][city]
                    next_city = city
            if next_city is not None:
                if r >= len(routes):
                    routes.append([0])
                routes[r].append(next_city)
                remaining_capacity[r] -= demands[next_city]
                current_location[r] = next_city
                remaining_cities.remove(next_city)

    # Finalize routes, each ending at the depot
    for route in routes:
        route.append(0)

    return routes

# Function to calculate total travel cost for a given tour
def calculate_travel_cost(route, distance_matrix):
    return sum(distance.js_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Apply initial solution construction
initial_routes = construct_initial_solution(coordinates, demands, capacity, 2)
initial_costs = [calculate_travel_cost(r, distance_matrix) for r in initial_routes]
overall_cost = sum(initial_costs)

# Print the results
print(f"Initial solution routes and costs:")
for idx, route in enumerate(initial_routes):
    route_cost = calculate_travel_cost(route, distance_matrix)
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {sum(initial_costs)}")