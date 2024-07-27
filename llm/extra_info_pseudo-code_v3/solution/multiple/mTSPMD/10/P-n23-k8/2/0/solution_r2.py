import numpy as np
import random
from deap import base, creator, tools, algorithms

# City coordinates including depots and other cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and corresponding depots
num_robots = 8
depots = list(range(num_robots))  # Assuming first 8 indices are depots corresponding to robots 0 through 7

# Distance calculation function, Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize DEAP framework for genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(8, 23), 15)  # Cities except depots
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, n=100)

def evaluate(individual):
    cost = 0
    split_points = np.array_split(individual, num_robots)  # Splitting cities roughly equally among robots
    assigned_routes = {i: [depots[i]] + list(split_points[i]) + [depots[i]] for i in range(num_robots)}
    for key, route in assigned_routes.items():
        for i in range(len(route) - 1):
            cost += euclidean_distance(route[i], route[i + 1])
    return cost,

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm process
def main():
    random.seed(64)
    pop = toolbox.population()
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("std", np.std)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=200, stats=stats, halloffame=hof, verbose=True)
    
    # Best individual
    best_ind = hof.items[0]
    print(f"Best tour sequence: {best_ind}")
    print("Best tour cost:", evaluate(best_ind)[0])

    # Splitting and printing tours for each robot
    split_points = np.array_split(best_ind, num_robots)
    tours = {depots[i]: [depots[i]] + list(split_points[i]) + [depots[i]] for i in range(num_robots)}
    for depot, tour in tours.items():
        print(f"Robot starting at depot {depot} Tour: {tour}")
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i + 1])
        print(f"Robot starting at depot {depot} Total Travel Cost: {tour_cost}")
    
    return pop, stats, hof

if __name__ == "__main__":
    main()