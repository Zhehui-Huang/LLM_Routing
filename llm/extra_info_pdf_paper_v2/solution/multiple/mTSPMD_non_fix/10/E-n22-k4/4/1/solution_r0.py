import math
import random

# Coordinates of the cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Get the distance matrix
def calculate_distance_matrix(coords):
    matrix = []
    for i in range(len(coords)):
        matrix.append([euclidean_distance(coords[i], coords[j]) for j in range(len(coords))])
    return matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Simulated Annealing swap function
def swap_two_cities(route):
    a, b = random.sample(range(1, len(route)), 2)
    route[a], route[b] = route[b], route[a]
    return route

# Calculate total distance of a route
def route_distance(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Simulated annealing to minimize the route distance
def simulated_annealing(route, initial_temp, cooling_rate, minimum_temp):
    current_temp = initial_temp
    current_route = route
    current_route_distance = route_distance(route)
    while current_temp > minimum_temp:
        new_route = swap_two_cities(current_route[:])
        new_route_distance = route_distance(new_route)
        if new_route_distance < current_route_distance or random.random() < math.exp((current_route_distance - new_route_distance) / current_temp):
            current_route, current_route_distance = new_route, new_route_distance
        current_temp *= cooling_rate
    return current_route, current_route_distance

# Initialize routes for four robots from depot 0, The cities are divided between the robots
split_cities = 5  # This is an arbitrary division
robots = 4
routes = [[0] + list(range(1 + i*split_cities, 1 + (i+1)*split_cities)) for i in range(robots)]

# Assign left-over cities to the last robot
routes[-1].extend(range(1 + robots*split_cities, len(coordinates)))

# Apply simulated annealing to each robot's route
final_routes = []
total_cost = 0

for i in range(robots):
    optimized_tour, tour_cost = simulated_annealing(routes[i], 10000, 0.995, 1)
    final_routes.append(optimized_tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {optimized_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")