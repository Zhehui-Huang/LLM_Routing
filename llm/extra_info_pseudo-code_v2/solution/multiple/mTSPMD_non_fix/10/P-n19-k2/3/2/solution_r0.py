import random
from math import sqrt
import numpy as np
import copy

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance calculation
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix between all cities including depots
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Genetic Algorithm settings
pop_size = 50
G_max = 500
mutation_rate = 0.2
crossover_rate = 0.8

# Initialize population
def initialize_population():
    population = []
    for _ in range(pop_size):
        permutation = list(range(2, len(coordinates)))  # starts from 2 because 0 and 1 are depots
        random.shuffle(permutation)
        population.append([0] + permutation + [1])  # Start from depot 0, end at depot 1
    return population

# Calculate total distance of a tour
def calculate_cost(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += dist_matrix[tour[i]][tour[i+1]]
    return total_dist

# Crossover operation
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1, parent2
    size = len(parent1)
    child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
    
    # Select crossover points
    a, b = random.sample(range(size), 2)
    start, end = min(a, b), max(a, b)

    # Swap slices between a and b
    child1[start:end], child2[start:end] = parent2[start:end], parent1[start:end]

    # Resolving duplicate problem
    for i in range(size):
        if (child1.count(child1[i]) > 1):
            for j in range(size):
                if not (parent1[j] in child1):
                    child1[i] = parent1[j]
                    break
                    
    for i in range(size):
        if (child2.count(child2[i]) > 1):
            for j in range(size):
                if not (parent2[j] in child2):
                    child2[i] = parent2[j]
                    break
                    
    return child1, child2

# Mutation operation
def mutate(tour):
    if random.random() > mutation_rate:
        return tour
    size = len(tour)
    a, b = random.sample(range(1, size - 1), 2)  # mutation only between on inter-city nodes
    tour[a], tour[b] = tour[b], tour[a]
    return tour

# Genetic algorithm to minimize the travel cost and determine the tours
def genetic_algorithm():
    population = initialize_population()
    for generation in range(G_max):
        # Selection
        population = sorted(population, key=lambda x: calculate_cost(x))[:pop_size]
        
        # Creating new generation
        new_generation = []
        while len(new_generation) < pop_size:
            p1, p2 = random.sample(population, 2)
            c1, c2 = crossover(p1, p2)
            new_generation.append(mutate(c1))
            new_generation.append(mutate(c2))
        
        population = new_generation
    
    # Find the best solution
    best_tour = min(population, key=lambda x: calculate_cost(x))
    return best_tour

best_solution = genetic_algorithm()
robot_0_tour = best_solution[:best_solution.index(1) + 1]
robot_1_tour = best_solution[best_solution.index(1):]

robot_0_cost = calculate_cost(robot_0_tour)
robot_1_cost = calculate_cost(robot_1_tour)
total_cost = robot_0_cost + robot_1_cost

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", total_cost)