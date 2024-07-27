import numpy as to np
from scipy.spatial.distance import euclidean
import random
from deap import base, creator, tools, algorithms

# Defining the cities' coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate the Euclidean distance between each pair of cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')  # Avoid self-loop

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n), n-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function
def evalTSP(individual):
    route = [0] + individual + [0]
    max_dist = max(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    return (max_dist,)

# Crossover and mutation
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def main():
    random.seed(42)
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    
    # With 100 generations, we expect our GA to evolve well towards an optimum
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, halloffame=hof)
    
    best_route = [0] + hof[0] + [0]
    best_max_dist = evalTSP(hof[0])[0]
    total_distance = sum(distances[best_route[i]][best_route[i+1]] for i in range(len(best_route)-1))
    
    return {
        "Tour": best_route,
        "Total travel cost": total_distance,
        "Maximum distance between consecutive cities": best_max_dist
    }

# Run the main genetic algorithm process
result = main()
print(result)