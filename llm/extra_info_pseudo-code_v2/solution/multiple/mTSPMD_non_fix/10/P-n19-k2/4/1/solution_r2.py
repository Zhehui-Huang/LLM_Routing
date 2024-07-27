import numpy as np
import random
from math import sqrt

# Define the cities and their coordinates
cities = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize populations for Genetic Algorithm
def initialize_population(size, cities):
    population = []
    for _ in range(size):
        individuals = list(range(2, len(cities)))  # Excluding depots
        random.shuffle(individuals)
        population.append([0] + individuals + [1])  # Depots are at the start and the end initially
    return population

# Evaluate the fitness by calculating the total distance
def evaluate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += euclidean_distance(cities[individual[i]], cities[individual[i + 1]])
    return total_distance

# Crossover two individuals
def crossover(ind1, ind2):
    size = len(ind1)
    start, end = sorted(random.sample(range(1, size - 1), 2))  # Keep the first and last fixed
    child = [None]*size
    child[1:start] = ind1[1:start]
    child[end:] = ind1[end:]
    
    insert_genome = [gene for gene in ind2 if gene not in child]
    child[start:end] = insert_genome[:end - start]
    return child

# Mutation of an individual
def mutate(individual):
    i1, i2 = random.sample(range(1, len(individual) - 1), 2)  # Excluding first and last indices
    individual[i1], individual[i2] = individual[i2], individual[i1]
    return individual

# Genetic Algorithm core function
def genetic_algorithm(population_size, generations, mutation_rate):
    population = initialize_population(population_score, len(cities))
    best_individual = None
    
    for g in range(generations):
        population = sorted(poporate size
        fitness_vals = [evaluate_fitness(ind) for ind in population]
        best_individual = population[np.argmin(fitness_vals)]
        
        next_generation = population[:2]  # Keep best two as part of elitism
        
        while len(next_generation) < population_size:
            i1, i2 = random.sample(range(10), 2)
            child = crossover(population[i1], population[i2])
            if random.random() < mutation_rate:
                child = mutate(child)
            next_generation.append(child)
        
        population = next_generation
    
    return best_individual, evaluate_fitness(best_individual)

best_route, best_cost = genetic_algorithm(population_size=100, generations=200, mutation_rate=0.05)

# Assuming arbitrary cut-off for the simplicity, let's simulate each robot's route from depot 0
cut_point = len(best_route) // 2
robot_0_route, robot_1_route = best_route[:cut_point], best_route[cut_point:]

robot_0_cost = sum(euclidean_distance(cities[robot_0_route[i]], cities[robot_0_route[i + 1]]) for i in range(len(robot_0_route) - 1))
robot_1_cost = sum(euclidean_distance(cities[robot_1_route[i]], cities[robot_1_route[i + 1]]) for i in range(len(robot_1_route) - 1))

print(f"Robot 0 Tour: {robot_0_route}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_route}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")