import numpy as np
from scipy.spatial.distance import euclidean
import random
from deap import base, creator, tools, algorithms

# Defining the cities' coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate the Euclidean distances between each pair of cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        if i != j:
            dist = euclidean(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
        else:
            distances[i][j] = float('inf')  # Avoid self-loops

# Setup for Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n), n-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    route = [0] + individual + [0]
    max_dist = max(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_distance = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    return max_dist, total_distance

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)

    # Execute genetic algorithm
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean, axis=0)
    stats.register("min", np.min, axis=0)

    result, log = algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof, verbose=True)

    best_route = [0] + hof[0] + [0]
    max_dist, total_distance = evalTSP(hof[0])
    return best_route, total_distance, max_dist

# Get the results
tour, total_cost, max_dist = main()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive destinations:", max_dist)