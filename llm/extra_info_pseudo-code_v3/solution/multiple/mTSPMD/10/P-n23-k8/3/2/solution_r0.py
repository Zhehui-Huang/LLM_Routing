import numpy as np
from math import sqrt
from scipy.spatial.distance import euclidean
from deap import base, creator, tools, algorithms

# Define city coordinates and depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robots deployment
depots = {i: cities[i] for i in range(8)}
robots = 8

# Distance matrix computation
def dist_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

distance_matrix = dist_matrix([cities[i] for i in range(len(cities))])

# Genetic Algorithm implementation
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", np.random.permutation, len(cities) - 8 + robots)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness function
def evaluation(individual):
    total_distance = 0.0
    start_index = 0
    for depot in depots:
        tour_start = individual[start_index]
        tour_end = depots[depot]
        tour_distance = distance_matrix[tour_start, depot]
        total_distance += tour_distance
        # Add distances for internal cities in the route
        for j in range(start_index + 1, len(individual)):
            tour_distance = distance_matrix[individual[j-1], individual[j]]
            total_distance += tour_distance
        total_distance += distance_matrix[individual[j], depot]  # return to the depot
        start_index = j + 1
    return (total_distance,)

toolbox.register("evaluate", evaluation)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.get.register("select", tools.selTournament, tournsize=3)

# Run the Genetic Algorithm
def main():
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1, similar=np.array_equal)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof, verbose=True)
    return pop, stats, hof

if __name__ == "__main__":
    population, stats, hof = main()
    best_route = hof[0]
    print("Best Route: ", best_route)
    print("Best Route Length: ", evaluation(best_route))