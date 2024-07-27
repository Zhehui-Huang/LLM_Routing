import numpy as np
from scipy.spatial.distance import euclidean
import random
from deap import creator, base, tools, algorithms

# List of city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
n_cities = len(cities)

# Distance matrix between cities
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Genetic Algorithm Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(2, n_cities), n_cities-2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    route1 = [0] + individual[:10] + [0]  # Robot 0 tour
    route2 = [1] + individual[10:] + [1]  # Robot 1 tour
    cost1 = sum(distances[route1[i], route1[i+1]] for i in range(len(route1)-1))
    cost2 = sum(distances[route2[i], route2[i+1]] for i in range(len(route2)-1))
    return cost1 + cost2,

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Genetic Algorithm Execution
population = toolbox.population(n=300)
ngen = 40
best_solution = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=ngen, verbose=False)

# Extract best individual
best_individual = tools.selBest(population, 1)[0]
route1 = [0] + best_individual[:10] + [0]
route2 = [1] + best_individual[10:] + [1]
cost1 = sum(distances[route1[i], route1[i+1]] for i in range(len(route1)-1))
cost2 = sum(distances[route2[i], route2[i+1]] for i in range(len(route2)-1))
overall_cost = cost1 + cost2

# Print results
print("Robot 0 Tour:", route1)
print("Robot 0 Total Travel Cost:", cost1)
print("Robot 1 Tour:", route2)
print("Robot 1 Total Travel Cost:", cost2)
print("Overall Total Travel Cost:", overall_cost)