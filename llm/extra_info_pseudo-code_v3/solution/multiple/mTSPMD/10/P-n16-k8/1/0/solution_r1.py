import numpy as np
from scipy.spatial.distance import euclidean
from random import randint, shuffle, seed
from itertools import permutations
import operator

# Set random seed for reproducibility
seed(42)

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and respective depots
robots = list(range(8))  # Robot IDs from 0 to 7
depots = list(range(8))  # Depot IDs from 0 to 7

# Number of cities excluding depots
num_cities = 16

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(coords[i], coords[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

# Create the distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Genetic Algorithm Components
def initialize_population(num_individuals, num_cities, depots):
    population = []
    base_genome = list(range(num_cities))
    for _ in range(num_individuals):
        shuffle(base_genome)
        genome = depots + base_genome
        population.append(genome)
    return population

def calculate_fitness(genome, distance_matrix, num_robots):
    total_distance = 0
    # Splitting genome into tours
    tours = [None] * num_robots
    for i, city in enumerate(genome[num_robots:]):
        robot_idx = genome[i % num_robots]
        if tours[robot_idx] is None:
            tours[robot_idx] = [depots[robot_idx], city]
        else:
            tours[robot_idx].append(city)
    for tour in tours:
        if tour is not None:
            tour.append(tour[0])  # Completing the loop back to depot
            for i in range(len(tour) - 1):
                total_distance += distance_matrix[tour[i]][tour[i + 1]]
    return total_distance, tours

def select_parents(population, fitnesses, num_parents):
    parents = sorted(zip(population, fitnesses), key=lambda x: x[1])
    selected = [x[0] for x in parents[:num_parents]]
    return selected

def crossover(parent1, parent2, crossover_point):
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(genome, mutation_rate):
    for i in range(len(genome)):
        if randint(0, 100) < mutation_rate:
            j = randint(0, len(genome) - 1)
            genome[i], genome[j] = genome[j], genome[i]
    return genome

# Parameters
num_individuals = 50
num_generations = 100
mutation_rate = 5  # 5% mutation rate
num_parents = 10

# Initialize population
population = initialize_population(num_individuals, num_cities, depots)

# Genetic Algorithm
for generation in range(num_generations):
    fitnesses = []
    for individual in population:
        fitness, _ = calculate_fitness(individual, distance_matrix, len(robots))
        fitnesses.append(fitness)
    parents = select_parents(population, fitnesses, num_parents)
    next_generation = []
    for _ in range(num_individuals // 2):
        p1, p2 = np.random.choice(parents, 2, replace=False)
        child1 = crossover(p1, p2, len(depots))
        child2 = crossover(p2, p1, len(depots))
        next_generation.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
    population = next_generation

# Results
best_individual = min(population, key=lambda ind: calculate_fitness(ind, distance_matrix, len(robots))[0])
best_fitness, best_tours = calculate_fitness(best_individual, distance_matrix, len(robots))

# Output
overall_total_cost = 0
for robot_id, tour in enumerate(best_tours):
    if tour:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
        overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")