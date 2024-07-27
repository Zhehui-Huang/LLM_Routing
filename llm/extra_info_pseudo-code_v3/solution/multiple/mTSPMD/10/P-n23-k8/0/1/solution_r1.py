import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of each robot's depot start and ending points
depots = list(range(8))  # Indices for depots correspond to the robot's ID


# Cities not included in depots
cities = list(set(range(len(coordinates))) - set(depots))

# Euclidean distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

dist_matrix = distance_matrix(coordinates)

# Utility functions for the Genetic Algorithm
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# GA Initialization
def initialize_population(population_size, cities):
    population = []
    for _ in range(population_size):
        tour = cities.copy()
        random.shuffle(tour)
        population.append(tour)
    return population

# Choose basic random selection for simplicity
def select_parents(population, dist_matrix, depots):
    # Randomly select two parents
    return random.sample(population, 2)

def crossover(parent1, parent2):
    # Implement a simple crossover
    mid_point = len(parent1) // 2
    child = parent1[:mid_point] + [c for c in parent2 if c not in parent1[:mid_point]]
    return child

def mutate(tour, mutation_rate=0.1):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(depots, cities, generations=100, population_size=50):
    population = initialize_population(population_size, cities)
    best_distance = float('inf')
    best_tour = None

    for _ in range(generations):
        new_population = []
        for _ in range(len(population)):
            parent1, parent2 = select_parents(population, dist_matrix, depots)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
            tour_cost = calculate_tour_cost([depots[0]] + child + [depots[0]], dist_matrix)
            if tour_cost < best_distance:
                best_distance = tour_cost
                best_tour = child
        population = new_population

    return best_tour, best_distance

# Running the genetic algorithm with one robot (for simplification in this example)
best_tour, best_distance = genetic_algorithm(depots, cities)
best_tour_with_depot = [depots[0]] + best_tour + [depots[0]]

print(f"Tour: {best_tour_with_depot}")
print(f"Total Travel Cost: {best_distance}")