import numpy as its
from scipy.spatial.distance import euclidean
import random
from deap import creator, base, tools, algorithms

# List of cities with their coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate the distance matrix between cities
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Define Genetic Algorithm components
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(2, n_cities), n_cities - 2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    route1 = [0] + individual[:10] + [0]
    route2 = [1] + individual[10:] + [1]
    cost_route1 = sum(distances[route1[i], route1[i+1]] for i in range(len(route1) - 1))
    cost_route2 = sum(distances[route2[i], route2[i+1]] for i in range(len(route2) - 1))
    return cost_route1 + cost_route2,

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

population = toolbox.population(n=300)
ngen = 100
best_ind = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=ngen, verbose=True)[-1]

# Process the final best solution
best_ind = tools.selBest(population, 1)[0]
robot0_tour = [0] + best_ind[:10] + [0]
robot1_tour = [1] + best_ind[10:] + [1]
robot0_cost = sum(distances[robot0_tour[i], robot0_tour[i+1]] for i in range(len(robot0_tour) - 1))
robot1_cost = sum(distances[robot1_tour[i], robot1_tour[i+1]] for i in range(len(robot1_tour) - 1))

# Output the result
print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", robot0_cost + robot1_cost)