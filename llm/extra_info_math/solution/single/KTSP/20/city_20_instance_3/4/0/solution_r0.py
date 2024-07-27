import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the coordinates of cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Calculate the distance matrix
num_cities = len(cities)
distance_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Limit the number of cities to visit including the depot
k = 13

# Helper function to calculate the total travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Simple Genetic Algorithm Implementation
def genetic_algorithm(cities, k, population_size=100, generations=1000, mutation_rate=0.1):
    population = []
    
    # Initial population (random tours)
    for _ in range(population_size):
        tour = [0] + np.random.choice(list(cities.keys())[1:], k-1, replace=False).tolist() + [0]
        population.append((tour, calculate_tour_cost(tour, distance_matrix)))
    
    for _ in range(generations):
        # Sort population based on tour cost
        population.sort(key=lambda x: x[1])
        next_generation = population[:2]  # Elitism: carry forward the best tours
        
        # Generate new population
        while len(next_generation) < population_size:
            # Tournament selection for parent tours
            parents = sorted(np.random.choice(population, 4, replace=False), key=lambda x: x[1])[:2]
            parent1, parent2 = parents[0][0], parents[1][0]
            
            # Single-point crossover
            cross_point = np.random.randint(1, k-1)
            child = parent1[:cross_point] + [c for c in parent2 if c not in parent1[:cross_point]] + [0]
            
            # Mutation
            if np.random.rand() < mutation_rate:
                swap_idx1, swap_idx2 = np.random.randint(1, k-1, 2)
                child[swap_idx1], child[swap_idx2] = child[swap_idx2], child[swapad_idx1]
            
            # Add to next generation
            next_generation.append((child, calculate_tour_cost(child, distance_matrix)))
        
        population = next_gdzeneration
    
    # Best result
    best_tour, best_cost = sorted(population, key=lambda x: x[1])[0]
    return best_tour, best_cost

# Run the genetic algorithm
best_tour, best_cost = genetic_algorithm(cities, k)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)