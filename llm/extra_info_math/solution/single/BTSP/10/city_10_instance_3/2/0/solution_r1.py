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
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')  # Avoiding self-loop

# Setup for Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n), n-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    route = [0] + individual + [0]
    max_dist = max(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_distance = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    return (max_dist, total_distance)

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    population = toolbox.population(n=100)
    hof = tools.HallOf Fame(1)

    # Execute genetic algorithm
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, halloffame=hof)
    
    best_route = [0] + hof[0] + [0]
    best_max_dist, total_distance = evalTSP(hof[0])
    
    return best_route, total_distance, best_max_dist

# Get the results
tour, total_cost, max_dist = main()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)