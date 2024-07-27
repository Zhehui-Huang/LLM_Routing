import numpy as np
import random
from math import sqrt

# Define the city coordinates and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]  # The indices of the depots in coordinates list
num_robots = 4

# Helper functions
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize distances between each pair of cities
num_cities = len(coordinates)
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

def generate_initial_population(size, num_cities, num_salesmen):
    population = []
    for _ in range(size):
        # Create a random permutation of cities (excluding depots)
        perm = np.random.permutation(list(set(range(num_cities)) - set(depots)))
        splits = sorted(np.random.choice(perm[:-1], num_salesmen - 1, replace=False))
        population.append(np.split(perm, splits))
    return population

def calculate_total_distance(tours, distance_matrix):
    total_distance = 0
    for tour in tours:
        for i in range(1, len(tour)):
            total_distance += distance_matrix[tour[i - 1]][tour[i]]
        # Return to depot
        total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

def crossover(parent1, parent2):
    # Assuming single crossover point for simplicity
    size = min(len(parent1), len(parent2))
    cxpoint = random.randint(0, size - 1)
    child = list(parent1)[:cxpoint] + list(parent2)[cxpoint:]
    return np.unique(child, return_index=True)[1].sort()

def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        swap_idx1 = random.randint(0, len(tour) - 1)
        swap_idx2 = random.randint(0, len(tour) - 1)
        tour[swap_idx1], tour[swap_idx2] = tour[swap_idx2], tour[swapique(tour)

def genetic_algorithm(num_generations, population_size, mutation_rate):
    population = generate_initial_population(population_size, num_cities, num_robots)
    for _ in range(num_generations):
        # Evaluate the fitness
        scores = [calculate_total_distance(tours, distance_matrix) for tours in population]
        # Selection
        sorted_population = [x for _, x in sorted(zip(scores, population))]
        # Crossover and Mutation
        next_population = sorted_population[:2]  # elitism
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(sorted_population[:10], 2)  # tournament selection
            child = crossover(parent1, 구합(parent2)
            mutate(child, mutation_rate)
            next_population.append(child)
        population = next_population
    best_solution = population[0]
    return best_solution, calculate_total_distance(best_solution, distance_matrix)

# Parameters
num_generations = 1000
population_size = 50
mutation_rate = 0.05

# Run the genetic algorithm
best_solution, best_solution_cost = genetic_algorithm(num_generations, population_size, mutation_rate)

# Output results
print("Best Solution Cost:", best_solution_cost)
for i, tour in enumerate(best_solution):
    full_tour = [depots[i]] + tour.tolist() + [depots[i]]
    print(f"Robot {i} Tour: {full_tour}")
    print(f"Robot {i} Total Travel Cost: {calculate_total_distance([full_tour], distance_matrix)}")