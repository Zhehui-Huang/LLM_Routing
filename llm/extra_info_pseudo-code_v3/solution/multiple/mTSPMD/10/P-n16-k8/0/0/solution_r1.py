import random
from deap import base, creator, tools, algorithms
import numpy as np
from math import sqrt

# City coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Robot info
depots = list(range(8))
num_robots = 8

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
distance_matrix = np.zeros((16, 16))
for i in range(16):
    for j in range(16):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator
def create_individual():
    cities = list(range(8, 16))  # Only non-depot cities
    random.shuffle(cities)
    splits = random.sample(list(range(1, len(cities))), num_robots - 1)
    splits.sort()
    splits = [0] + splits + [len(cities)]
    return creator.Individual([cities[splits[i]:splits[i+1]] for i in range(num_robots)])

toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function
def eval_mmtsp(individual):
    total_cost = 0
    for idx, tour in enumerate(individual):
        tour_cost = 0
        if tour:
            # Start at robot's depot
            last_city = depots[idx]
            # Cost from depot to first city and between cities
            for city in tour:
                tour_cost += distance_matrix[last_city][city]
                last_city = city
            # Cost from last city back to depot
            tour_cost += distance_matrix[last_city][depots[idx]]
        total_cost += tour_cost
    return total_cost,

toolbox.register("evaluate", eval_mmtsp)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm
def main():
    random.seed(42)
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, 
                        stats=stats, halloffame=hof, verbose=True)
    
    # Best tours
    best_tours = hof[0]
    total_cost = 0
    for idx, tour in enumerate(best_tours):
        tour_cost = eval_mmtsp([tour])[0]
        total_cost += tour_cost
        print(f"Robot {idx} Tour: [{depots[idx]}] + {tour} + [{depots[idx]}]")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    print("Overall Total Travel Cost:", total_cost)

main()