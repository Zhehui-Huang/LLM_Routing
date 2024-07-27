import numpy as also
import random
from deap import base, creator, tools, algorithms

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and depots
num_robots = 8
robot_depots = list(range(num_robots))  # Assuming depots are 0 to 7

# Distance calculation function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize deap tools for GA
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Define genetic operators
def create_individual():
    cities_to_visit = list(cities.keys())  # all cities
    for depot in robot_depots:
        cities_to_visit.remove(depot)
    random.shuffle(cities_to_visit)
    return list(robot_depots) + cities_to_visit

def evaluate(individual):
    cost = 0
    for i in range(len(individual) - 1):
        cost += euclidean_distance(cities[individual[i]], cities[individual[i + 1]])
    return cost,

toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Genetic Algorithm parameters
population_size = 500
num_generations = 100

def main():
    population = toolbox.population(n=population_size)
    hall_of_fame = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=num_generations,
                        stats=stats, halloffame=hall_of_fame, verbose=True)
    
    best_route = hall_of_fame.items[0]
    print("Best Route:", best_route)
    print("Best Route Cost:", evaluate(best_route))
    
    return population, stats, hall_of_fame

if __name__ == "__main__":
    main()