import numpy as np
from scipy.spatial.distance import euclidean
import random
from deap import base, creator, tools, algorithms

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate Euclidean distances between all pairs of cities
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n_cities), 12)
toolbox.register("individual", tools.initIterate, creator.Individual, 
                 lambda: [0] + toolbox.indices() + [0])
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    return (sum(distances[individual[i], individual[i+1]] for i in range(len(individual) - 1)),)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Genetic Algorithm parameters
population = toolbox.population(n=300)
ngen = 400
cxpb, mutpb = 0.7, 0.2

# Genetic Algorithm execution
result, log = algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, verbose=False)

best_individual = tools.selBest(result, k=1)[0]
best_tour = best_individual
best_cost = evalTSP(best_individual)[0]

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")