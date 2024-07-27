import numpy as np
from scipy.spatial import distance_matrix
from random import sample, randint, random
from copy import deepcopy

# Define cities and their coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute distances
dist_matrix = distance_matrix(cities, cities)

def fitness(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(sample(range(size), 2))
    child = [None]*size
    child[start:end+1] = parent1[start:end+1]
    filled = set(parent1[start:end+1])
    pointer = 0
    for x in parent2:
        if x not in filled:
            while None is not child[pointer]:
                pointer += 1
            child[pointer] = x
            pointer += 1
    return child

def mutate(route, mutation_rate):
    if random() < mutation_rate:
        i, j = sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(population_size, generations, mutation_rate):
    # Initial population (random)
    pop = [sample(range(1, 20), 9) for _ in range(population_desc_size)]
    pop = [[0] + p + [0] for p in pop]  # Incorporate the depot city

    for generation in range(generations):
        # Evaluate fitness
        fitnesses = [fitness(p) for p in pop]
        next_generation = []
        
        for _ in range(population_size):
            # Tournament selection
            candidates = sample(list(enumerate(fitnesses)), 4)
            parent1_idx, parent2_idx = sorted(candidates, key=lambda x: x[1])[:2]
            parent1, parent2 = pop[parent1_idx[0]], pop[parent2_idx[0]]

            # Crossover
            child = crossover(parent1, parent2)
            
            # Mutation
            mutate(child, mutation_rate)
            
            next_generation.append(child)

        pop = deepcopy(next_generation)
        
    # Get the best solution
    best_idx = min(range(len(pop)), key=lambda i: fitness(pop[i]))
    best_solution = pop[best_idx]
    best_cost = fitness(best_solution)

    return best_solution, best_cost

# Run genetic algorithm
best_route, best_cost = genetic_algorithm(population_size=50, generations=200, mutation_rate=0.05)
print("Tour:", best_route)
print("Total travel cost:", best_cost)