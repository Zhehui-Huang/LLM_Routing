import random
import math
from deap import base, creator, tools, algorithms

# City coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Genetic Algorithm Setup
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator 
toolbox.register("indices", random.sample, range(1, len(cities)), len(cities) - 1)

# Structure initializers
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    # Complete route by adding the depot city at start and end
    route = [0] + individual + [0]
    # Total cost
    total_cost = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
    # Max distance between consecutive cities
    max_dist = max(distance(route[i], route[i+1]) for i in range(len(route) - 1))
    return (max_dist,)

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)

    population = toolbox.population(n=50)
    hall_of_fame = tools.HallOfFame(1)

    # Stats
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", min)

    # Algorithm
    algorithms.eaSimple(population, toolbox, 0.7, 0.2, 30, stats, halloffame=hall_of_fame)

    best_ind = hall_of_fame[0]
    best_tour = [0] + best_ind + [0]
    max_distance = evalTSP(best_ind)[0]
    total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

    return best_tour, total_travel_cost, max_distance

# Run the optimization and print output
best_tour, total_travel_cost, max_distance = main()
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)