import numpy as np
import random
from scipy.spatial import distance_matrix

# Given Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots and depot
num_robots = 8
depot = 0

# Creating the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Defining the fitness function (total distance)
def fitness(chromosome):
    total_cost = 0
    for i in range(len(chromosome) - 1):
        total_cost += dist_matrix[chromosome[i], chromosome[i+1]]
    return total_cost

# Genetic operations
def select(population, fitnesses):
    idx = np.random.choice(len(population), size=2, replace=False, p=fitnesses/fitnesses.sum())
    return population[idx[0]], population[idx[1]]

def crossover(parent1, parent2):
    size = len(parent1)
    co_point = random.randint(1, size - 1)
    child = np.concatenate((parent1[:co_point], parent2[co_point:]))
    # Ensure child is valid i.e., contains no duplicate and missing cities
    missing = set(range(size)) - set(child)
    duplicates = [x for x in child if list(child).count(x) > 1]
    for dup, mis in zip(duplicates, missing):
        child[np.where(child == dup)[0][0]] = mis
    return child

def mutate(chromosome, mutation_rate=0.05):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Initialize population
pop_size = 100
chromosome_length = len(coordinates)
population = [np.random.permutation(range(1, chromosome_length)).tolist() for _ in range(pop_size)]

# Genetic Algorithm Execution
generations = 500
for _ in range(generations):
    new_population = []
    fitnesses = np.array([fitness(chromo) for chromo in population])
    for __ in range(pop_size // 2):
        parent1, parent2 = select(population, fitnesses)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
    population = new_population

# Find best solution
fitnesses = np.array([fitness(chromo) for chromo in population])
best_idx = np.argmin(fitnesses)
best_solution = population[best_idx]

# Here we are supposed to break the solution among robots starting from depot
# Skipping this for simplicity

print("Best solution based on GA: ", best_solution)
print("Cost: ", fitness(best_solution))