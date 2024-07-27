import math
import random
from deap import base, creator, tools, algorithms

# Coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

depot_ids = list(range(8))  # Depot IDs for each robot
non_depot_cities = [i for i in range(8, 23)]  # Non-depot city IDs

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator
def create_individual():
    shuffled_cities = non_depot_cities[:]
    random.shuffle(shuffled_cities)
    segments = sorted(random.sample(range(1, 15), 7))
    return shuffled_cities + segments

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function
def evalTSP(individual):
    segments = sorted(individual[15:])
    tours = []
    prev = 0
    total_cost = 0
    
    for i, depot in enumerate(depot_ids):
        start = depot
        end_city_index = segments[i] if i < len(segments) else 15
        tour = [start] + individual[prev:end_city_index] + [start]
        tours.append(tour)
        cost = sum(euclidean_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        total_cost += cost
        prev = end_city_index
    
    return (total_cost,)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Genetic Algorithm parameters
population_size = 300
crossover_probability = 0.7
mutation_probability = 0.2
number_of_generations = 50

pop = toolbox.population(n=population_size)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("Avg", numpy.mean)
stats.register("Min", numpy.min)
stats.register("Max", numpy.max)

algorithms.eaSimple(pop, toolbox, cxpb=crossover_probability, mutpb=mutation_probability, 
                    ngen=number_of_generations, stats=stats, halloffame=hof, verbose=True)

# Print the best individual
best_individual = hof.items[0]
best_fitness = best_individual.fitness.values[0]
print("Best Individual (Total Cost):", best_fitness)

# Decode the best individual
segments = sorted(best_individual[15:])
prev = 0
total_travel_cost = 0
for i, depot in enumerate(depot_ids):
    start = depot
    end_city_index = segments[i] if i < len(segments) else 15
    tour = [start] + best_individual[prev:end_city_index] + [start]
    cost = sum(euclidean_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_travel_cost += cost
    prev = end_city_index
print("Overall Total Travel Cost:", total_travel_cost)