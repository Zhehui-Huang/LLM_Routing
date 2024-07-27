import numpy as np
import random

# Define city coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Generate the distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = np.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
    return dist_matrix

distance_matrix = generate_distance_matrix(cities)

# Function to calculate the total travel cost for a path
def calculate_cost(path, distance_matrix):
    return sum(distance_matrix[path[i], path[i+1]] for i in range(len(path) - 1))

# Variable Neighborhood Search to determine best tour
def variable_neighborhood_search(cities, distance_matrix, num_cities=4):
    num_iterations = 1000
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_iterations):
        # Generate an initial random solution
        selected_cities = [0] + random.sample(range(1, len(cities)), num_cities - 1) + [0]
        
        for i in range(1, num_cities):
            for j in range(i + 1, num_cities):
                # Swap two cities
                new_solution = selected_cities[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution, distance_matrix)
                # Check if we have a new best solution
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
    
    return best_solution, best_cost

# Find the best tour and cost
best_tour, total_cost = variable_neighborhood_search(cities, distance_matrix)

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")