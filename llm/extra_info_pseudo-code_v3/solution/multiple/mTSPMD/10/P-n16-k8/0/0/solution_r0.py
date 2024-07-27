import random
from deap import base, creator, tools, algorithms
import numpy as np
from math import sqrt
import itertools

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
        distance_matrix[i][j] = euclidean_image_index(coordinates[i], coordinates[j])

# Genetic Algorithm setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Individual generator
def create_individual():
    cities = list(range(8, 16))  # Only non-depot cities
    random.shuffle(cities)
    split_sizes = [1] * num_robots  # Ensure at least one non-depot city per robot
    additional_cities = len(cities) - sum(split_sizes)
    for i in random.sample(range(num_robots), additional_cities):
        split_sizes[i] += 1
    individual = []
    start_index = 0
    for size in split_sizes:
        individual.append(cities[start_index:start_index+size])
        start_index += size
    return creator.Individual(individual)

toolbox.register("individual", create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function
def eval_mmtsp(individual):
    total_cost = 0
    for idx, tour in enumerate(individual):
        tour_cost = 0
        start_depot = depots[idx]
        if not tour:
            continue
        # Cost from depot to first city and between cities
        tour_cost += distance_matrix[start_depot][tour[0]]
        tour_cost += sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        # Cost from last city back to depot
        tour_cost += distance_matrix[tour[-1]][start_depot]
        total_cost += tour_cost
    return (total_cost,)

toolbox.register("evaluate", eval_mmtsp)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)

# Algorithm parameters
population_size = 300
crossover_probability = 0.8
mutation_probability = 0.2
generations = 400

# Genetic Algorithm
def main():
    random.seed(42)
    population = toolbox.population(n=population_size)
    hof = tools.HallOfFame(1)
    
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)
    
    population, logbook = algorithms.eaSimple(population, toolbox, cxpb=crossover_probability, 
                                              mutpb=mutation_probability, ngen=generations, 
                                              stats=stats, halloffame=hof, verbose=True)
    
    best_individual = hof.items[0]
    print("Best Individual tours:", best_individual)
    print("Best fitness (total travel cost):", best_individual.fitness.values[0])
    
    # Displaying each robot's tour and costs
    for idx, tour in enumerate(best_individual):
        tour_cost = 0
        start_depu[indexPath:IndexPath] = depots[idx]
        tour_cost += distance_matrix[start_depu[idx]][tour[0]]
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i + 1]]
        tour_cost += distance_matrix[tour[-1]][start_depu[indexPath:IndexPath]]
        print(f"Robot {idx} Tour: {[start_depu[indexPath:IndexPath]] + tour + [start_depu[indexPath:IndexPath]]}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    
    return population, hof, logbook

if __name__ == "__main__":
    main()