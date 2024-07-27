import numpy as np
from scipy.spatial import distance_matrix
from deap import base, creator, tools, algorithms
import random

# City coordinates:
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
num_cities = len(cities)
distance_matrix = distance_matrix(cities, cities)

# Depots and robots:
num_robots = 4
depot_ids = [0]

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(num_cities), num_cities)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval_tsp(individual):
    cost = 0
    for i in range(len(individual) - 1):
        cost += distance_matrix[individual[i]][individual[i + 1]]
    cost += distance_matrix[individual[-1]][individual[0]]  # Return to starting depot
    return cost,

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.03)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_tsp)

def main():
    pop = toolbox.population(n=300)
    result, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, verbose=False)
    
    best_individual = tools.selBest(pop, k=1)[0]
    best_tour = [cities[idx] for idx in best_individual]
    best_cost = eval_tsp(best_individual)[0]
    
    print("Best Tour:", best_individual)
    print("Best Cost:", best_cost)

if __name__ == "__main__":
    main()