import math
from deap import base, creator, tools, algorithms
import random

# Define cities coordinates
cities_coord = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities_coord[city1][0] - cities_coord[city2][0]) ** 2 + (cities_coord[city1][1] - cities_coord[city2][1]) ** 2)

# Fitness function to minimize the maximum distance between consecutive cities
def evaluate(individual):
    max_dist = 0
    total_cost = 0
    for i in range(len(individual) - 1):
        dist = distance(individual[i], individual[i + 1])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    # Return a tuple in the format required by DEAP
    return (max_dist, total_tour_cost),

# Create the algorithm tools
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 20), 19)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats, halloffame=hof, verbose=True)
    
    best_tour = hof[0]
    best_tour.append(0)
    best_tour.insert(0, 0)
    
    max_distance, total_cost = evaluate(best_tour)[0]
    return best_tour, total_cost, max_distance

# Run the genetic algorithm
best_tour, total_cost, max_distance = main()

print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)