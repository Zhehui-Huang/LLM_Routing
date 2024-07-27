import numpy as np
import random
from scipy.spatial.distance import euclidean
from deap import base, creator, tools, algorithms

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants
NUM_CITIES = len(coordinates)
POP_SIZE = 300
NUM_GENERATIONS = 100
CX_PB = 0.7
MUT_PB = 0.2

# Distance calculation between each pair of cities
distance_matrix = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# DEAP framework setup for Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(2, NUM_CITIES), NUM_CITIES - 2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def evaluate_route(individual):
    route1 = [0] + individual[:len(individual)//2] + [0]
    route2 = [1] + individual[len(individual)//2:] + [1]
    
    cost1 = sum(distance_matrix[route1[i]][route1[i+1]] for i in range(len(route1)-1))
    cost2 = sum(distance_matrix[route2[i]][route2[i+1]] for i in range(len(route2)-1))
    
    return cost1 + cost2,

toolbox.register("evaluate", evaluate_route)

def main():
    population = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    
    algorithms.eaSimple(population, toolbox, cxpb=CX_PB, mutpb=MUT_PB, ngen=NUM_GENERATIONS,
                        stats=stats, halloffame=hof, verbose=True)
    
    best_individual = hof.items[0]
    route1_split = len(best_individual) // 2
    route1 = [0] + best_individual[:route1_split] + [0]
    route2 = [1] + best_individual[route1_split:] + [1]
    cost1 = sum(distance_matrix[route1[i]][route1[i+1]] for i in range(len(route1)-1))
    cost2 = sum(distance_matrix[route2[i]][route2[i+1]] for i in range(len(route2)-1))
    
    print("Robot 0 Tour:", route1)
    print("Robot 0 Total Travel Cost:", cost1)
    print("Robot 1 Tour:", route2)
    print("Robot 1 Total Travel Cost:", cost2)
    print("Overall Total Travel Cost:", cost1 + cost2)

if __name__ == "__main__":
    main()