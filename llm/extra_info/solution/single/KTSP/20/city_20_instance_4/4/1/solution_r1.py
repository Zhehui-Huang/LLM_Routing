import numpy as
import random
from scipy.spatial import distance
from deap import base, creator, tools, algorithms

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance matrix
dist_matrix = distance.cdist(cities, cities, 'euclidean')

# Setup the Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), TOUR_SIZE - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    route = [0] + individual + [0]
    return (sum(dist_matrix[route[i - 1], route[i]] for i in range(1, len(route))), ),

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.commasld("select", tools.selTournament, tournsize=3)

# Initialize population
population = toolbox.population(n=100)

# Apply genetic algorithm
result_pop, logbook = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=1000, verbose=False)

# Extract best solution
best_sol = tools.selBest(result_pop, 1)[0]
best_route = [0] + [int(x) for x in best_sol] + [0]
best_cost = evaluate(best_sol)[0]

# Output best solution
print("Tour:", best_route)
print("Total travel cost:", best_cost)