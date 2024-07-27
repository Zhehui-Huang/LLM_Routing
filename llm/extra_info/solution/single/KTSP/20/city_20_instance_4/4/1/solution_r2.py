import numpy as np
import random
from scipy.spatial import distance_matrix
from deap import creator, base, tools, algorithms

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Create a distance matrix
distances = distance_matrix(cities, cities)

# Define the problem to minimize the tour distance
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
# Attribute generator for individuals (permute indices 1-19, since 0 is the depot and fixed)
toolbox.register("indices", random.sample, range(1, 20), 15)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function to calculate the total distance of the tour
def evaluate(individual):
    route = [0] + individual + [0]  # Start and end at the depot
    tour_distance = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return (tour_distance,)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create initial population
population = toolbox.population(n=300)
# Apply genetic algorithm
result, log = algorithms.eaSimple(population, toolbox, cxpb=0.8, mutpb=0.2, ngen=400, verbose=False)

# Best individual from the results
best_ind = tools.selBest(population, 1)[0]
best_route = [0] + best_ind + [0]
best_cost = evaluate(best_ind)[0]

# Output the result
print("Tour:", best_route)
print("Total travel cost:", best_cost)