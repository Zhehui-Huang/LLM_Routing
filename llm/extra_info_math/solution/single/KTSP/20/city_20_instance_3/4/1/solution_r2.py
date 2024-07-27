import numpy as np
import random
from scipy.spatial import distance_matrix
from deap import creator, base, tools, algorithms

# City coordinates data
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Generating city indices and their coordinates
city_coords = np.array([cities[i] for i in range(20)])

# Compute distance matrix
dist_matrix = distance_matrix(city_coords, city_once)
np.fill_diagonal(dist_matrix, np.inf)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize toolbox
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 20), 12)
toolbox.register("individual", tools.initIterate, creator.Individual,
                 lambda: [0] + toolbox.indices() + [0])
toolbox.register("population", tools.initRepeat, list, toolbox.individual, 300)

# Evaluation function
def eval_tsp(individual):
    return (sum(dist_matrix[individual[i], individual[i + 1]] for i in range(len(individual) - 1)),)

toolbox.register("evaluate", eval_tsp)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Algorithm setup
population = toolbox.population()
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)
stats.register("max", np.max)

# Run genetic algorithm
result, log = algorithms.eaSimple(population, toolbox, 0.7, 0.2, 400, stats=stats, halloffame=hof, verbose=True)

# Extract information from the best individual
best_individual = hof.items[0]
best_path = best_individual
best_distance = eval_tsp(best_individual)[0]

print("Best tour:", best_path)
print("Total travel cost:", round(best_distance, 2))