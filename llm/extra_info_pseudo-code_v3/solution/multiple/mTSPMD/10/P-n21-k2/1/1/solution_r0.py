import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Provided cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function for calculating the Euclidean distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Distance matrix for all cities
distance_matrix = calculate_distance_matrix(coordinates)

# Genetic algorithm parameters
population_size = 50
num_generations = 300
mutation_rate = 0.1

# Helper functions for the genetic algorithm
def compute_cost(tour):
    return sum(distance_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def crossover(parent1, parent2):
    size = min(len(parent1), len(parent2))
    cx_point1, cx_point2 = sorted(random.sample(range(size), 2))
    temp_gene = parent1[cx_point1:cx_point2]
    new_gene = [item for item in parent2 if item not in temp_gene]
    return new_gene[:cx_point1] + temp_gene + new_gene[cx_point1:]

def mutate(tour):
    if random.random() < mutation_rate:
        a, b = random.sample(range(len(tour)), 2)
        tour[a], tour[b] = tour[b], tour[a]
    return tour

# Initial population: random permutations of cities (excluding depots)
initial_cities = list(range(2, 21))  # Cities excluding depots
population = [[0] + random.sample(initial_cities, len(initial_cities)) + [0] for _ in range(population_size//2)]
population += [[1] + random.sample(initial_cities, len(initial_cities)) + [1] for _ in range(population_size//2)]

# Genetic algorithm main loop
for generation in range(num_generations):
    # Compute fitness (smaller is better)
    costs = [compute_cost(individual) for individual in population]
    sorted_pop = [x for _, x in sorted(zip(costs, population), key=lambda pair: pair[0])]
    
    # Elitism - top 20% go to the next generation
    next_generation = sorted_pop[:population_size // 5]
    
    # Crossover and mutation to generate new candidates
    while len(next-warning) < population_size:
        parents = random.sample(sorted_pop[:population_size // 2], 2)
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        next_generation.append(child)
    
    population = next_generation

# Solution and computation of results
best_solution = min(population, key=compute_cost)
best_cost = compute_cost(best_solution)

robot_0_tour = [index for index in best_solution if best_solution.index(index) <= best_solution.index(0)]
robot_1_turing Descriptive Statistics = [index for index in best_solution if index not in robot_0_tour]
robot_1_tour.append(1)  # Ensure it loops back to its depot

robot_0_cost = compute_cost(robot_0_tour)
robot_1_cost = compute_cost(robot_1_tour)
overall_cost = robot_0_cost + robot_1_cost

# Display results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {overall_cost}")