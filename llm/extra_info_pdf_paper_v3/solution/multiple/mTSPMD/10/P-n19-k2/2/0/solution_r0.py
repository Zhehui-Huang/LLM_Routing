import numpy as np
import random
from math import sqrt

# Constants
NUM_CITIES = 19
NUM_ROBOTS = 2
DEPOTS = [0, 1]

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(NUM_CITIES)] for i in range(NUM_CITIES)]

# Genetic Algorithm Hyperparameters
population_size = 50
generations = 500
mutation_rate = 0.2
crossover_rate = 0.8

# Initialize a random tour population
def generate_population(pop_size, num_cities):
    return [random.sample(range(2, num_cities), num_cities - 2) for _ in range(pop_size)]

# Fitness Function: Calculate total travel cost
def calculate_fitness(solution):
    total_cost = 0
    # Tour for Robot 0 (depot 0)
    tour0 = [DEPOTS[0]] + solution[:len(solution)//2] + [DEPOTS[0]]
    total_cost += sum(distance_matrix[tour0[i]][tour0[i+1]] for i in range(len(tour0) - 1))
    # Tour for Robot 1 (depot 1)
    tour1 = [DEPOTS[1]] + solution[len(solution)//2:] + [DEPOTS[1]]
    total_cost += sum(distance_matrix[tour1[i]][tour1[i+1]] for i in range(len(tour1) - 1))
    return total_cost, tour0, tour1

# Selection: Tournament selection
def tournament_selection(population, tournament_size=5):
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda x: calculate_fitness(x)[0])
    return selected[0]

# Crossover: Partially matched crossover (PMX)
def PMX(parent1, parent2):
    size = len(parent1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child1 = [None]*size
    child2 = [None]*size
    child1[cxpoint1:cxpoint2] = parent1[cxpoint1:cxpoint2]
    child2[cxpoint1:cxpoint2] = parent2[cxpoint1:cxpoint2]
    for i in range(size):
        if cxpoint1 <= i < cxpoint2:
            continue
        if parent2[i] not in child1:
            child1[i] = parent2[i]
        if parent1[i] not in child2:
            child2[i] = parent1[i]
    child1 = [x for x in child1 if x is not None] + [x for x in parent2 if x not in child1]
    child2 = [x for x in child2 if x is not None] + [x for x in parent1 if x not in child2]
    return child1, child2

# Mutation: Swap mutation
def mutate(individual, mutation_rate):
    individual = individual[:]
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm Execution
population = generate_population(population_size, NUM_CITIES)
for generation in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        if random.random() < crossover_rate:
            child1, child2 = PMX(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        new_population.append(child1)
        new_population.append(child2)
    population = new_population

# Find the best solution
best_solution = min(population, key=lambda x: calculate_fitness(x)[0])
best_cost, best_tour0, best_tour1 = calculate_fitness(best_solution)

# Output the results
print("Robot 0 Tour:", best_tour0)
print("Robot 0 Total Travel Cost:", sum(distance_matrix[best_tour0[i]][best_tour0[i+1]] for i in range(len(best_tour0) - 1)))
print("Robot 1 Tour:", best_tour1)
print("Robot 1 Total Travel Cost:", sum(distance_matrix[best_tour1[i]][best_tour1[i+1]] for i in range(len(best_tour1) - 1)))
overall_total_travel_cost = sum(distance_matrix[best_tour0[i]][best_tour0[i+1]] for i in range(len(best_tour0) - 1)) + sum(distance_matrix[best_tour1[i]][best_tour1[i+1]] for i in range(len(best_tour1) - 1))
print("Overall Total Travel Cost:", overall_total_travel_cost)