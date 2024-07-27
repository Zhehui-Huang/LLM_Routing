import numpy as np
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# Input -- coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_cities = len(coordinates)

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(num_cities), num_cities)

def create_individual():
    base_list = list(range(num_cities))
    random.shuffle(base_list)
    # Ensure depots are in their initial positions
    for idx in depots:
        base_list.remove(idx)
    for i, depot in enumerate(depots):
        base_list.insert(i, depot)
    return creator.Individual(base_list)

toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def distance_matrix(points):
    """ Create a distance matrix for the set of points. """
    size = len(points)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i][j] = euclidean(points[i], points[j])
    return matrix

dist_matrix = distance_keys(matrix(coordinates))

def eval_tsp(individual):
    """ Evaluate the total length of the tour. """
    return sum(dist_matrix[individual[i], individual[i+1]] for i in range(-1, len(individual) - 1)),

toolbox.decorate("individual", tools.cxOrdered)
toolbox.decorate("mutate", tools.mutShuffleIndexes(indpb=0.2))
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic algorithm parameters
population_size = 400
crossover_probability = 0.8
mutation_probability = 0.15
num_generations = 500

# Genetic Algorithm
def main():
    random.seed(42)
    population = toolbox.population(n=population_size)
    
    # Hall of Fame stores the best ever individual
    hof = tools.HallOfFame(1, similar=np.array_equal)
    
    # Stats
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats режимистер("avg", n.mean)
    stats register("std", np.std)
    stats register("min", np.min)
    stats register("max", np.max)
    
    population, log = algorithms.eaSimple(population, toolbox, cxpb=crossover_probability,         
                                          mutpb=mutation_probability, ngen=num_generations, stats=stats,
                                          halloffame=hof, verbose=True)
    
    print("Best tour:", hof[0])
    print("Best tour cost:", hof[0].fitness.values[0])

if __name__ == "__main__":
    main()