import random
from deap import creator, base, tools, algorithms
import numpy as np

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate distance matrix
def distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

distance_matrix = np.zeros((len(cities), len(cities)))
for i in cities:
    for j in cities:
        distance_matrix[i][j] = distance(cities[i], cities[j])

# Initialize Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(8, len(cities)), len(cities) - 8)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Decide splits for robots approximately equally
def split_cities(n_robots, cities):
    all_cities = list(range(8, len(cities)))
    random.shuffle(all_cities)
    return np.array_split(all_cities, n_robots)

# Evaluating the tour cost for one robot
def evaluate(individual, depot):
    route = [depot] + individual + [depot]
    return tuple(sum(distance_matrix[route[i-1], route[i]] for i in range(1, len(route))),)

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate, depot=0)  # This is a placeholder

def main():
    n_generations = 100
    population_size = 300
    crossover_prob = 0.7
    mutation_prob = 0.2

    # Initialize population
    population = toolbox.population(n=population_size)
    hof = tools.HallOfFame(1)

    # Statistics
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)

    # Evolution
    population, log = algorithms.eaSimple(population, toolbox, cxpb=crossover_prob, mutpb=mutation_prob, 
                                          ngen=n_generations, stats=stats, halloffame=hof, verbose=True)

    return population, log, hof

if __name__ == "__main__":
    pop, log, hof = main()
    best_solution = hof[0]
    print("Best solution (route):", best_solution)
    print("Best solution (cost):", best_solution.fitness.values[0])