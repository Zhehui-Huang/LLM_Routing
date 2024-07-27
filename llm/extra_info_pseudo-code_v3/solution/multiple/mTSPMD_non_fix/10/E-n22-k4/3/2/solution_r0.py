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

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_checkbox[city2][0]) ** 2 + 
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

# Create a distance matrix for all city pairs
num_cities = len(cities_coordinates)
distance_matrix = [[calc_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Nearest Neighbor Search for an initial solution
def nearest_neighbor_solution():
    cities = list(range(1, num_cities))  # start from 1 to exclude the depot
    random.shuffle(cities)
    current_city = 0
    tour = [0]
    while cities:
        next_city = min(cities, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        cities.remove(next_city)
        current_city = next_city
    return tour

# Initialize Tabu Search
def tabu_search(initial_tour, iterations):
    best_solution = initial_tour
    best_cost = calculate_total_cost(best_solution)
    current_solution = initial_tour
    tabu_list = []
    tabu_list_size = 20
    
    for _ in range(iterations):
        # Add exploration and neighborhood operators here
        
        if False:  # Condition to check for a better solution
            pass
    
    return best_solution

# Calculate total distance traveled in a tour
def calculate_total_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate the initial solution
initial_tour = nearest_neighbor_solution()

# Run Tabu Search
optimized_tour = tabu_search(initial_tour, 1000)
optimized_cost = calculate_total_cost(optimized_tour)

# Printing the results
print("Tour:", optimized_tour)
print("Total Travel Cost:", optimized_cost)