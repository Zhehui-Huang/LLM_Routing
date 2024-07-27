import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates as a dictionary
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
    4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distances between cities
def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

matrix = distance_matrix(cities)

# Helper functions for the genetic algorithm
def create_initial_population(size, num_cities, include_city):
    return [[include_city] + random.sample([i for i in range(num_cities) if i != include_city], 15) for _ in range(size)]

def tour_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i - 1]][tour[i]]
    total_cost += dist_matrix[tour[-1]][tour[0]]  # Return to depot
    return total_cost

def mate(parent1, parent2):
    split = random.randint(1, len(parent1) - 2)
    child = parent1[:split] + [item for item in parent2 if item not in parent1[:split]]
    if len(child) != len(parent1):
        raise Exception("Mating failed: child of incorrect length.")
    return child

def mutate(tour, mutation_rate=0.2):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(tour) - 1)
            tour[i], tour[swap_with] = tour[swap_with], tour[i]
    return tour

# Genetic algorithm to find minimal tour
def genetic_algorithm(matrix, num_iterations, population_size):
    population = create_initial_population(population_size, len(cities), 0)  # Include the depot city 0
    for _ in range(num_iterations):
        population = sorted(population, key=lambda x: tour_cost(x, matrix))
        next_generation = population[:2]  # Elitism: carry the best two to next gen
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)  # Selection
            child = mate(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        population = next_generation

    best_tour = min(population, key=lambda x: tour_state_cost(x, matrix))
    return best_tour, tour_cost(best_tour, matrix)

# Parameters
num_iterations = 1000
population_size = 100

# Running the genetic algorithm
best_tour, best_cost = genetic_algorithm(matrix, num_iterations, population_size)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)