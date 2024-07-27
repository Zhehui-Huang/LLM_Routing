import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

# City coordinates including the depot city (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

num_robots = 8
num_cities = len(coordinates)

def euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Calculate distance matrix
distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)])

# Genetic algorithm parameters
POPULATION_SIZE = 100
GENERATIONS = 400
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.8

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, num_cities), num_cities-1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    """ Evaluate the total distance traveled when visiting cities in the order of the individual list """
    routes = np.array_split(individual, num_robots)
    total_cost = 0
    tours = []
    for route in routes:
        # Include depot city at start and end of each trip
        trip = [0] + list(route) + [0]
        tour_cost = sum(distance_matrix[trip[i]][trip[i+1]] for i in range(len(trip) - 1))
        total_cost += tour_cost
        tours.append(trip)
    return total_cost,

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)
    population = toolbox.population(n=POPISTRATION_SIZE)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=CROSSOVER