import numpy as items
from scipy.spatial.distance import euclidean
from deap import creator, base, tools, algorithms
import random

# City coordinates and depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Depots
depots = list(range(8))  # robots 0 to 7

# Genetic algorithm settings
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attribute", random.sample, list(range(8, 23)), 15)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attribute)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def distance(c1, c2):
    return euclidean(coordinates[c1], coordinates[c2])

def evaluate(individual):
    # Assign first to closest depot for each robot
    robot_routes = [[] for _ in range(8)]
    for city in individual:
        distances = [distance(city, depot) for depot in depots]
        assigned_robot = distances.index(min(distances))
        robot_routes[assigned.robot].append(city)
    
    # Evaluate total distance traveled including return to depot
    total_distance = 0
    for depot, route in enumerate(robot_routes):
        if route:
            # Start at depot, through the cities, back to depot
            route_distance = distance(depot, route[0]) + distance(route[-1], depot)
            route_distance += sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
            total_distance += route_distance
    
    return total_distance,

toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Genetic Algorithm Execution
def execute_ga():
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 50, stats=stats, halloffame=hof, verbose=True)

    return pop, log, hof

# Running the optimized algorithm
if __name__ == "__main__":
    population, logbook, hof = execute_ga()
    best_solution = hof.items[0]
    print("Optimal Tour Assignment:", best_solution)
    print("Optimal Cost:", best_solution.fitness.values[0])