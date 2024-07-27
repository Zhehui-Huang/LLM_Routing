import numpy as np
from scipy.spatial.distance import euclidean
from deap import base, creator, tools, algorithms
import random
import itertools

# Definitions for Genetic Algorithm
IND_SIZE = 19  # Number of cities minus the number of depots
NUM_CITIES = 21
NUM_DEPOTS = 2
POP_SIZE = 300
NUM_GENERATIONS = 400
CX_PB = 0.7
MUT_PB = 0.2

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculating distances between each city
distances = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        distances[i][j] = euclidean(coordinates[i], coordinates[j])

# Helpers and GA setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(2, NUM_CITIES), IND_SIZE)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def evalMmTSP(individual):
    # Inserting depots
    route0 = [0] + individual[:len(individual)//2] + [0]
    route1 = [1] + individual[len(individual)//2:] + [1]
    
    # Calculate route distances
    total_cost0 = sum(distances[route0[i]][route0[i+1]] for i in range(len(route0)-1))
    total_cost1 = sum(distances[route1[i]][route1[i+1]] for i in range(len(route1)-1))
    
    return total_cost0 + total_cost1,

toolbox.register("evaluate", evalMmTSP)

# Main GA process
def main():
    random.seed(64)
    population = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1, similar=np.array_equal)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("std", np.std)
    
    algorithms.eaSimple(population, toolbox, cxpb=CX_PB, mutpb=MUT_PB, ngen=NUM_GENERATIONS, 
                        stats=stats, halloffame=hof, verbose=True)
    
    best_tour = hof[0]
    route0 = [0] + best_tour[:len(best_tour)//2] + [0]
    route1 = [1] + best_tour[len(best_tour)//2:] + [1]
    cost0 = sum(distances[route0[i]][route0[i+1]] for i in range(len(route0)-1))
    cost1 = sum(distances[route1[i]][route1[i+1]] for i in range(len(route1)-1))
    
    total_cost = cost0 + cost1
    print("Robot 0 Tour:", route0)
    print("Robot 0 Total Travel Cost:", cost0)
    print("Robot 1 Tour:", route1)
    print("Robot 1 Total Travel Cost:", cost1)
    print("Overall Total Travel Cost:", total_cost)

if __name__ == "__main__":
    main()