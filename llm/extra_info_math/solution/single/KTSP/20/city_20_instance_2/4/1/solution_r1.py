import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# City coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Initialize distances matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])

def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Genetic Algorithm settings
population_size = 200
generations = 500
tournament_size = 5
mutation_rate = 0.1
k = 10

def create_individual(cities):
    individual = list(cities)
    random.shuffle(individual)
    return [0] + individual[:k-1] + [0]

def crossover(parent1, parent2):
    start = random.randint(1, k-2)
    end = random.randint(start+1, k-1)
    child = [None]*k
    child[0], child[-1] = 0, 0
    child[start:end] = parent1[start:end]
    filled = set(child)
    filled.add(0)
    for i in range(1, k-1):
        if child[i] is None:
            for gene in parent2:
                if gene not in filled:
                    child[i] = gene
                    filled.add(gene)
                    break
    return child

def mutate(individual):
    i1, i2 = random.sample(range(1, k-1), 2)
    individual[i1], individual[i2] = individual[i2], individual[i1]

def fitness(individual):
    return -calculate_tour_cost(individual)

# Initialize population
current_population = [create_individual(list(cities.keys())) for _ in range(population_size)]

# Start the evolution process
for generation in range(generations):
    new_population = []
    scores = [(fitness(ind), ind) for ind in current_population]
    ranked = sorted(scores, reverse=True)
    
    # Elite selection: the best always passes to the next generation
    new_population.append(ranked[0][1])
    
    while len(new_population) < population_size:
        # Tournament selection
        tournament = [random.choice(current_population) for _ in range(tournament_size)]
        parent1 = max(tournament, key=fitness)
        tournament = [random.choice(current_population) for _ in range(tournament_size)]
        parent2 = max(tournament, key=fitness)
        
        # Crossover
        child = crossover(parent1, parent2)
        
        # Mutation
        if random.random() < mutation_rate:
            mutate(child)
        
        new_population.append(child)
    current_rep_population = new_population

best_ind, best_score = max((ind, fitness(ind)) for ind in current_rep_population)
best_tour = best_ind
best_cost = -best_score

# Output the results accurately
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))