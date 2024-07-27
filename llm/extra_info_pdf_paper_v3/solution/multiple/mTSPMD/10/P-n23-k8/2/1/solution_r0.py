import numpy as np
from scipy.spatial.distance import euclidean
import random
from deap import creator, base, tools, algorithms

# Cities coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and their depots
depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = len(depots)

# Total number of cities including depots
num_cities = len(city_coords)

# Generate distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(city_coords[i], city_coords[j])
        else:
            distance_matrix[i][j] = 0

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator (random permutation of city indices)
toolbox.register("indices", random.sample, range(num_cities), num_cities)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)

# Population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness evaluation
def evalTSP(individual):
    cost = 0
    # Make sure each robot returns to its starting depot
    segments = [individual[depots[i]:depots[i+1]+1] if i+1 < num_robots else individual[depots[i]:] + [depots[i]]
               for i in range(num_robots)]
    for segment in segments:
        for i in range(len(segment) - 1):
            cost += distance_matrix[segment[i]][segment[i+1]]
        cost += distance_matrix[segment[-1]][segment[0]]  # return to depot
    return cost,

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

# Genetic Algorithm parameters
population_size = 300
crossover_probability = 0.7
mutation_probability = 0.2
number_of_generations = 400

# Run GA
pop = toolbox.population(n=population_size)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

algorithms.eaSimple(pop, toolbox, cxpb=crossover_probability, mutpb=mutation_probability,
                    ngen=number_of_generations, stats=stats, halloffame=hof, verbose=True)

# Best solution
best_route = hof[0]
best_cost = evalTSP(best_route)[0]

# Print tours for each robot
overall_cost = 0
for robot_id in range(num_robots):
    start_index = depots[robot_id]
    end_index = depots[robot_id + 1] if robot_id + 1 < num_robots else num_cities
    tour = [start_index] + best_route[start_index+1:end_index] + [start_index]
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")