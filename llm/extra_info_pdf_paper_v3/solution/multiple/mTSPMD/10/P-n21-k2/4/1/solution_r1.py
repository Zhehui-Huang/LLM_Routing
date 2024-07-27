import numpy as np
from scipy.spatial import distance_matrix
import random
from deap import base, creator, tools, algorithms

# Coordinates of cities including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]

# Number of robots
num_robots = 2
# Depots for robots
depots = [0, 1]

# Distance matrix computation
dist_matrix = distance_matrix(coordinates, coordinates)

# Creating types for the individual components in Genetic Algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Toolbox for handling the crossover, mutation, and selection operations
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(2, len(coordinates)), len(coordinates) - 2)  # all cities but depots
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic operators
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def evaluate(individual):
    division = sorted(random.sample(range(1, len(individual)), num_robots - 1))
    tour_splits = [0] + division + [len(individual)]
    total_distance = 0.0
    for i in range(num_robots):
        start_index = depots[i]
        tour_distance = 0
        for idx in individual[tour_splits[i]:tour_splits[i + 1]]:
            tour_distance += dist_matrix[start_index][idx + 2]  # adjust for depots
            start_index = idx + 2
        tour_distance += dist_matrix[start_index][depots[i]]
        total_distance += tour_distance

    return total_distance,

toolbox.register("evaluate", evaluate)

# Starting the genetic algorithm
population = toolbox.population(n=300)
hall_of_fame = tools.HallOfFame(1)

# Algotithm parameters
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats]register("min", np.min)
stats.register("max", np.max)

# Evolving the population
algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, stats=stats,
                    halloffame=hall_of_fame, verbose=True)

# Best tour found
best_tour = hall_of_fame.items[0]
best_fitness = best_tour.fitness.values[0]

# Display results
print("Best tour (indices):", best_tour)
print("Best tour fitness (total cost):", best_fitness)

def decode_tour(individual):
    division = sorted(random.sample(individual, num_robots - 1))
    tour_splits = [0] + division + [len(individual)]
    tours = []
    for i in range(num_robots):
        tour = [depots[i]]
        for idx in individual[tour_splits[i]:tour_splits[i + 1]]:
            tour.append(idx + 2)
        tour.append(depots[i])
        tours.append(tour)
    return tours

tours = decode_tour(best_tour)
robot_costs = []

for i, tour in enumerate(tours):
    cost = sum(dist_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    robot_costs.append(cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

overall_cost = sum(robot_costs)
print("Overall Total Travel Cost:", overall_cost)