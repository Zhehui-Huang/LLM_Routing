import random
from deap import base, creator, tools, algorithms
import numpy as np
from math import sqrt

# City coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distance_matrix = np.zeros((16, 16))
for i in range(16):
    for j in range(16):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize DEAP framework for EA
creator.create("FitnessMin", base.Fitness, weights=(-1,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Function to generate each individual
def create_individual():
    cities = list(range(8, 16))  # Non-depot cities
    random.shuffle(cities)
    return creator.Individual(cities)

toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, 300)

# Evaluation function
def eval_tsp(individual):
    cost = 0
    for i in range(1, len(individual)):
        cost += distance_matrix[individual[i - 1]][individual[i]]
    # Closing the loop to the starting depot for each robot
    for depot in range(8):
        start_cost = distance_matrix[depot][individual[0]]
        end_cost = distance_matrix[individual[-1]][depot]
        cost += start_cost + end_cost
    return cost,

toolbox.register("evaluate", eval_tsp)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run GA
def run_ga():
    population = toolbox.population()
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("Avg", np.mean)
    stats.register("Min", np.min)

    result, log = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, 
                                      stats=stats, halloffame=hof, verbose=True)
    best_route = hof[0]
    best_cost = best_route.fitness.values[0]

    return best_route, best_cost

# Execute the main GA execution and print results
if __name__ == "__main__":
    best_route, best_cost = run_ga()
    print("Best Route:", best_route)
    print("Best Cost:", best_cost)