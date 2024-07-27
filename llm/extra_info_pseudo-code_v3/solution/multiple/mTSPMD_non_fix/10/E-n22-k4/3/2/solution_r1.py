import numpy as np
import math
import random

# Cities and their coordinates
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 + 
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

# Create a distance matrix for all city pairs
num_cities = len(cities_coordinates)
distance_matrix = [[calc_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Divide cities among robots
def divide_cities(num_robots, cities):
    random.shuffle(cities)
    return [cities[i::num_robots] for i in range(num_robots)]

# Nearest Neighbor Route for each robot
def nearest_neighbor_route(starting_city, cities):
    tour = [starting_city]
    current_city = starting_city
    while cities:
        next_city = min(cities, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        current_city = next_city
        cities.remove(next_city)
    return tour

# Calculate total distance traveled in a tour
def calculate_total_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Initializing tours and costs
tours = []
costs = []

# Divide cities for each robot
cities_for_robots = divide_cities(num_robots, list(range(1, num_cities)))  # start from 1 to exclude the depot

# Generating tours for each robot
for idx, cities in enumerate(cities_for_robots):
    tour = nearest_neighbor_route(0, cities)
    cost = calculate_total_cost(tour)
    tours.append(tour)
    costs.append(cost)

# Output results
overall_total_cost = sum(costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")