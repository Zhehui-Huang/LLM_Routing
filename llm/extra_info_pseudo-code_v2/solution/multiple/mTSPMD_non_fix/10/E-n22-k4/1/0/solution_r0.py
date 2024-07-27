import numpy as np
import random
from itertools import permutations

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Parameters
num_robots = 4
depot = 0  # All start at city index 0
max_generations = 100
population_size = 50
mutation_rate = 0.1

# Helper functions
def calculate_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize population
def initialize_population():
    population = []
    cities = list(range(1, len(coordinates)))  # all cities except the depot
    for _ in range(population_size):
        random.shuffle(cities)
        chromosomes = [depot] + cities
        population.append(chromosomes)
    return population

# Calculate fitness
def calculate_fitness(chromosome):
    total_distance = 0
    for i in range(len(chromosome) - 1):
        total_distance += calculate_distance(chromosome[i], chromosome[i + 1])
    return total_distance

# Selection
def selection(population):
    sorted_population = sorted(population, key=lambda chromo: calculate_fitness(chromo))
    return sorted_population[:population_size//2]  # elitism: Select the best half

# Crossover
def crossover(parent1, parent2):
    p1, p2 = random.sample(range(1, len(parent1)), 2)
    start, end = min(p1, p2), max(p1, p2)
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    fill_pos = list(filter(lambda i: parent2[i] not in parent1[start:end], range(len(parent2))))
    fill_vals = iter(fill_pos)
    for i in range(len(child)):
        if child[i] is None:
            child[i] = parent2[next(fill_vals)]
    child[0] = depot
    return child

# Mutation
def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

# Run GA
population = initialize_population()
for generation in range(max_generations):
    new_population = selection(population)
    while len(new_population) < population_size:
        p1, p2 = random.choices(new_population, k=2)
        child = crossover(p1, p2)
        mutate(child)
        new_population.append(child)
    population = new_population

# Get best solution
best_solution = min(population, key=calculate_fitness)
best_solution_cost = calculate_fitness(best_solution)

print("Optimal Tour: ", best_solution)
print("Total Travel Cost: ", best_solution_cost)