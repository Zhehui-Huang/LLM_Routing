import math
import random
from deap import creator, base, tools, algorithms

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots & depot starting point
num_robots = 8
depot = 0

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Define Genetic Algorithm components
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Evaluate function calculates the total cost of the route
def evaluate(individual):
    route = [depot] + individual
    return (sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1)),)

toolbox.register("evaluate", evaluate)

# Generate initial population
population = toolbox.population(n=300)

# Run Genetic Algorithm
final_population = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, verbose=False)[0]

# Extract the best route
best_individual = tools.selBest(final_population, k=1)[0]
best_route = [depot] + best_individual + [depot]
total_cost = evaluate(best_individual)[0]

# Outputs
print("Best Route for all robots combined (simplified to demonstrate one route for all):", best_route)
print("Total Travel Cost:", total_cost)