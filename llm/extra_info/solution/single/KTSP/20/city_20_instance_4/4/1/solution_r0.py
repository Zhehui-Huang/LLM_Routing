import numpy as np
from scipy.spatial import distance

# Cities' coordinates
cities = np.array([
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),    # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
])

# Distance matrix calculation
distances = distance.cdist(cities, cities, 'euclidean')

# Import genetic algorithm dependencies
from deap import base, creator, tools, algorithms
import random
import operator

# GA parameters
POP_SIZE = 100
TOUR_SIZE = 16
GENERATIONS = 1000
MUT_PROB = 0.2
CROSS_PROB = 0.7

# Genetic algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, typecode="d", fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), TOUR_SIZE-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluate function
def evaluate(individual):
    path = [0] + individual + [0]
    return (sum(distances[path[i], path[i + 1]] for i in range(len(path) - 1)),)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Running the genetic algorithm
population = toolbox.population(n=POP_SIZE)
result_pop = algorithms.eaSimple(population, toolbox, cxpb=CROSS_PROB, mutpb=MUT_PROB, 
                                 ngen=GENERATIONS, verbose=False)

# Extract solution
best_sol = tools.selBest(population, 1)[0]
best_tour = [0] + list(map(int, best_sol)) + [0]
best_cost = evaluate(best_sol)[0]

print("Tour:", best_tour)
print("Total travel cost:", best_cost)