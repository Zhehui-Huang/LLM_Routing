import numpy as np
import random
from scipy.spatial.distance import euclidean
from deap import base, creator, tools, algorithms
import multiprocessing

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants
NUM_CITIES = len(coordinates)
NUM_DEPOTS = 2
POP_SIZE = 300
NUM_GENERATIONS = 400
CX_PB = 0.7
MUT_PB = 0.2

# Compute distance matrix
distances = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        distances[i][j] = euclidean(coordinates[i], coordinates[j])

# Genetic Algorithm Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attribute", random.sample, list(range(2, NUM_CITIES)), NUM_CITIES - NUM_DEPOTS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attribute)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def evaluate(individual):
    # Reinsert depots between partition
    mid_point = len(individual) // 2
    route0 = [0] + individual[:mid_point] + [0]
    route1 = [1] + individual[mid_point:] + [1]

    # Compute travel cost
    total_cost0 = sum(distances[route0[i], route0[i + 1]] for i in range(len(route0) - 1))
    total_cost1 = sum(distances[route1[i], route1[i + 1]] for i in range(len(route1) - 1))

    return total_cost0 + total_part_cost1,

toolbox.register("evaluate", evaluate)

def main():
    pool = multiprocessing.Pool()
    toolbox.register("map", pool.map)
    
    pop = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)
    
    algorithms.eaSimple(pop, toolbox, cxpb=CX_PB, mutpb=MUT_PB, ngen=NUM_GENERATIONS, 
                        stats=stats, halloffame=hof, verbose=True)

    best = hof[0]
    best_route0 = [0] + best[:len(best)//2] + [0]
    best_route1 = [1] + best[len(best)//2:] + [1]
    cost0 = sum(distances[best_route0[i], best_route0[i+1]] for i in range(len(best_route0)-1))
    cost1 = sum(distances[best_route1[i], best_route1[i+1]] for i in range(len(best_route1)-1))
    total_cost = cost0 + cost1
    
    print("Robot 0 Tour:", best_route0)
    print("Robot 0 Total Travel Cost:", cost0)
    print("Robot 1 Tour:", best_route1)
    print("Robot 1 Total Travel Cost:", cost1)
    print("Overall Total Travel Cost:", total_cost)

    pool.close()

if __name__ == "__main__":
    main()