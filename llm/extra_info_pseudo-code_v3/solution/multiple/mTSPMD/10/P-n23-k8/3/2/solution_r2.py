import random
import numpy as np
from deap import creator, base, tools, algorithms
from math import sqrt

# Seed for reproducibility
random.seed(42)

# City coordinates indexed by city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots. Each starts at depots [0, 1, 2, ..., 7]
num_robots = 8
depots = list(range(num_robots))

# Initiating DEAP's creator for fitness minimization
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Define genetic operators
toolbox = base.Toolbox()
toolbox.register("attribute", random.sample, range(num_robots, len(cities)), len(cities) - num_robots)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attribute)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    # Split the cities among robots; here cities are simply divided sequentially
    chunks = np.array_split(individual, num_robots)
    total_trip_cost = 0
    routes = []

    for i, chunk in enumerate(chunks):
        # Start at depot, visit 'chunk' cities, return to depot
        route = [depots[i]] + list(chunk) + [depots[i]]
        trip_cost = sum(distance(route[j], route[j + 1]) for j in range(len(route) - 1))
        total_trip_cost += trip_cost
        routes.append(route)

    return total_trip_cost, routes

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    population = toolbox.population(n=50)
    hof = tools.HallOfFame(1, similar=np.array_equal)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)

    population, log = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=50, 
                                          stats=stats, halloffame=hof, verbose=True)

    best_individual = hof[0]
    best_cost, best_routes = evaluate(best_individual)
    return best_cost, best_routes

best_cost, best_routes = main()

# Outputting results
print(f"Overall Total Travel Cost: {best_cost}")
for idx, route in enumerate(best_routes):
    cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")