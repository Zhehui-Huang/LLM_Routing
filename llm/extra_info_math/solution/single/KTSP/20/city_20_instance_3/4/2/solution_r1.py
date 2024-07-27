import random
from math import sqrt
from deap import base, creator, tools, algorithms

# Constants
NUMBER_OF_CITIES = 20
NUMBER_OF_CITIES_TO_VISIT = 13

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), 
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), 
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate distance between two cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Fitness Function to minimize
def evalTSP(individual):
    distance_travelled = distance(cities[individual[-1]], cities[individual[0]])  # close the tour
    for i in range(len(individual) - 1):
        distance_travelled += distance(cities[individual[i]], cities[individual[i+1]])
    return (distance_travelled,)

# Setup the problem
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, NUMBER_OF_CITIES), NUMBER_OF_CITIES_TO_VISIT-1)
toolbox.register("individual", tools.initIterate, creator.Individual, 
                 lambda: [0] + toolbox.indices() + [0])
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Genetic Algorithm parameters
population = toolbox.population(n=300)
halloffame = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)

# Execute the genetic algorithm
result, log = algorithms.eaSimple(population, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=halloffame, verbose=True)

# Extract the best individual
best_route = halloffame[0]
best_distance = evalTSP(best_handle)[0]

# Display the results
print("Tour:", best_route)
print("Total travel cost:", best_distance)