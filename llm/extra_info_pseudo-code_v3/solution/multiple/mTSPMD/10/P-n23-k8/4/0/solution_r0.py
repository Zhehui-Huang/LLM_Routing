import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random
from deap import base, creator, tools, algorithms

# Coordinates for each city and depot
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate the Euclidean distance between two points
def distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# Define the fitness function
def evaluate(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distance(individual[i], individual[i + 1])
    total_distance += distance(individual[-1], individual[0])  # return to start
    return (total_distance,)

# Set random seed for reproducibility
random.seed(42)

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 23), 23 - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Main Genetic Algorithm
def main():
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    algorithms.eaSimple(population, toolbox, 0.7, 0.2, 50, stats=stats, halloffame=hof, verbose=True)
    
    return population, hof

if __name__ == "__main__":
    population, hof = main()
    best_route = hof.items[0]
    best_route.append(best_route[0])  # Closing the route to form a loop
    total_cost = evaluate(best_route)[0]

    print("Best Route:", best_route)
    print("Total Cost:", total_cost)

    # Adapt the above solution to distribute cities between robots based on their start locations