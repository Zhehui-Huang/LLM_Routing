from deap import base, creator, tools, algorithms
import random
import math
import numpy as np

# City coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate distance matrix
n_cities = len(cities)
distance_matrix = [[distance(i, j) for j in range(n_cits)] for i in range(n_cities)]

# Set up genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, n_cities), n_cities-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    # Include the starting city 0
    route = [0] + individual + [0]
    max_segment_length = max(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    return max_segment_length,

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run Genetic Algorithm
def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof)
    
    best_route = [0] + hof[0] + [0]
    total_travel_cost = sum(distance_matrix[best_route[i]][best_route[i+1]] for i in range(len(best_route) - 1))
    max_distance = evalTSP(hof[0])[0]
    
    return best_route, total_travel_cost, max_distance

# Run the main optimization function
best_route, total_travel_cost, max_distance = main()
print(f"Tour: {best_route}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")