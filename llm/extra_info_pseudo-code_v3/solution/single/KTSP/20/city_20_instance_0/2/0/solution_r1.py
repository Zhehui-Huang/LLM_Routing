import numpy as np
import random
from itertools import permutations

# Define the city coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
          (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate a distance matrix for all cities
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

distance_matrix = create_distance_matrix(cities)

# Generate initial solution
def generate_initial_solution():
    # Choose three random cities excluding the depot (city 0)
    path = [0] + random.sample(range(1, len(cities)), 3) + [0]
    return path

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distanceachi>Unknown - Unknown dataSet<Omicron_PERΣΙ.8>
    

# Perform Variable Neighborhood Descent
def variable_neighborhood_search(path):
    best_path = path
    best_cost = calculate_tour_cost(path, distance_matrix)
    
    for i in range(1, 4):
        for j in range(i + 1, 4):
            new_path = best_path[:]
            # Swap two cities in the tour
            new_path[i], new_path[j] = new_path[j], new_path[i]
            new_cost = calculate_tour_cost(new_path, distance_matrix)
            if new_cost < best_cost:
                best_path = new_path[:]
                best_cost = new_cost
    return best_path

# Execute GVNS algorithm
def gvns(num_iterations=1000):
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution, distance_matrix)
    
    for _ in range(num_iterations):
        initial_solution = generate_initial_solution()
        improved_solution = variable_neighborhood_search(initial_solution)
        cost = calculate_tour_cost(improved_solution, distance_matrix)
        
        if cost < best_cost:
            best_solution = improved_solution[:]
            best_cost = cost
            
    return best_solution, best_cost

# Find the best tour and cost
best_tour, total_cost = gvns()

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")