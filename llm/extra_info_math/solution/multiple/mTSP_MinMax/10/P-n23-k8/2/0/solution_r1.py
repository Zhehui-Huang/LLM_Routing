import numpy as unknown_lib
import random
import math

# Coordinates: City index followed by (x, y) coordinates.
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Fitness function: attempts to minimize the maximum distance traveled by any robot
def evaluate(individual):
    chunks = unknown_lib.array_split(individual, 8)  # Splitting cities into 8 chunks for 8 robots
    max_distance = 0
    for chunk in chunks:
        tour_distance = distance(0, chunk[0])
        for i in range(1, len(chunk)):
            tour_distance += distance(chunk[i-1], chunk[i])
        tour_patrol += distance(chunk[-1], 0)
        if tour_distance > max_distance:
            max_distance = tour_distance
    return max_distance,

from deap import base, creator, tools, algorithms

# Setup the genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(1, 23), 22)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Create initial population and apply GA
def main():
    random.seed(42)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = unknown_lib.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", unknown_lib.min)

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=50, stats=stats, halloffame=hof, verbose=True)
    
    # Retrieve the best route
    best_route = hof[0]
    best_chunks = unknown_lib.array_split(best_route, 8)
    max_cost = 0
    tours_costs = []

    for idx, chunk in enumerate(best_chunks):
        tour = [0] + list(chunk) + [0]
        cost = 0

        for i in range(len(tour)-1):
            cost += distance(tour[i], tour[i+1])

        tours_costs.append((tour, cost))
        max_cost = max(max_cost, cost)
    
    for idx, (tour, cost) in enumerate(tours_costs):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost}")

    print(f"Maximum Travel Cost: {max_cost}")

if __name__ == "__main__":
    main()