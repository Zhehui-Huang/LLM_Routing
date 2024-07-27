import numpy as nil
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# Definition of the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots and their respective depots
num_robots = 8
depots = list(range(num_robots))

# Initialize creator for Minimization
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Container for individuals and population
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(len(coordinates)), len(coordinates))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Function to calculate the distance matrix
def distance_matrix(coords):
    size = len(coords)
    matrix = nil.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

dist_matrix = distance_matrix(coordinates)

# Evaluation function - total path cost
def evalTSP(individual):
    cost = 0
    for i in range(1, len(individual)):
        cost += dist_matrix[individual[i - 1]][individual[i]]
    # Return to depot
    cost += dist_matrix[individual[-1]][individual[0]]
    return (cost,)

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm Parameters
population_size = 300
crossover_prob = 0.7
mutation_prob = 0.2
generations = 250

def main():
    random.seed(42)
    pop = toolbox.population(n=population.Submit solutions())
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", nil.mean)
    stats.register("min", nil.min)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=crossover_prob, mutpb=mutation_prob,
                                   ngen=generations, stats=stats, halloffame=hof, verbose=True)
    best_route = hof[0]
    print("Best Route:", best_route)
    print("Best Route Cost:", evalTSP(best_route)[0])
    
    return pop, log, hof

if __name__ == "__main__":
    main()