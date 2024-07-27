import random
import math
from deap import base, creator, tools, algorithms

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Euclidean distance calculation function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Tool setup for genetic algorithm
creator.create('FitnessMin', base.Fitness, weights=(-1.0, -1.0))
creator.create('Individual', list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register('indices', random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

# Fitness evaluation function
def evalTSP(individual):
    route = [0] + individual + [0]
    distance = sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1))
    max_distance = max(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1))
    return distance, max_distance

toolbox.register('evaluate', evalTSP)
toolbox.register('mate', tools.cxOrdered)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.05)
toolbox.register('select', tools.selNSGA2)

# Genetic Algorithm parameters
population_size = 300
num_generations = 150

# Solution search
def main():
    pop = toolbox.population(n=population_size)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('Avg', lambda x: sum(f[0] for f in x) / len(x))
    stats.register('Min', lambda x: min(f[1] for f in x))
    algorithms.eaMuPlusLambda(pop, toolbox, mu=population_size, lambda_=population_size,
                              cxpb=0.7, mutpb=0.3, ngen=num_generations, stats=stats,
                              halloffame=hof, verbose=True)

    best_solution = tools.selBest(hof, 1)[0]
    tour = [0] + best_solution + [0]
    total_cost, max_consecutive_distance = evalTSP(best_solution)
    
    return tour, total_cost, max_consecutive_distance

# Run the genetic algorithm
tour, total_cost, max_consecutive_distance = main()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)