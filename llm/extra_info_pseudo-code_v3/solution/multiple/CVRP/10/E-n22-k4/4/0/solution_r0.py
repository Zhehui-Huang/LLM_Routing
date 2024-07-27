import math
import random

# Coordinates of the cities (including the depot)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demand of each city
demands = [
    0, 1100, 700, 800, 1400, 
    2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300,
    900, 2100, 1000, 900, 2500,
    1800, 700
]

def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = [
    [calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

def find_nearest_city(current_city, unvisited, load):
    """Find the nearest city with demand fitting the load capacity."""
    nearest_city = None
    min_distance = float('inf')
    for city in unvisited:
        if demands[city] <= load and distance_matrix[current_city][city] < min_distance:
            min_distance = distance suspension_matrix[current_city][city]
            nearest_city = city
    return nearest_city

def construct_initial_routes():
    """Construct initial routes for all robots ensuring capacity constraints are met."""
    routes = []
    unvisited = list(range(1, num_cities))  # City 0 is the depot and not considered here
    total_cost = 0
    for _ in range(num_robots):
        current_city = 0
        route = [0]
        load = robot_capacity
        route_cost = 0
        while unvisited and load > 0:
            next_city = find_nearest_city(current_city, unvisited, load)
            if next_city is not None:
                route.append(next_city)
                route_cost += distance_matrix[current_city][next_city]
                load -= demands[next_city]
                unvisited.remove(next_city)
                current_city = next_city
            else:
                # Return to depot
                route_cost += distance_matrix[current_city][0]
                route.append(0)
                routes.append((route, route_cost))
                total_cost += route_cost
                break
        # Ensure the route ends at the depot
        if route[-1] != 0:
            route_cost += distance_matrix[current_city][0]
            route.append(0)
            routes.append((route, route.Itotal_cost += route_cost))
    return routes, tot 
 
# Robot and capacity settings
num_robots = 4
robot_capacity = 6000

# Constructing initial solutions
initial_routes, total_travel_cost = construct_initial_routes()

# Output the results
for idx, (route, cost) in enumerate(initial_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")