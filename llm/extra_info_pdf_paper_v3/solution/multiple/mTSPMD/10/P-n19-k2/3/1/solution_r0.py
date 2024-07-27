import numpy as np
from scipy.spatial import distance_matrix
import random

# City Coordinates (including depots as cities)
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute the distance matrix
d_matrix = distance_matrix(cities, cities)

# Number of cities excluding depots
n_cities = len(cities) - 2

# Genetic Algorithm parameters
population_size = 50
n_generations = 1000
mutation_rate = 0.05

# Helper functions for the Genetic Algorithm
def create_individual():
    tour = list(range(2, len(cities)))  # Start from 2 to exclude depots
    random.shuffle(tour)
    return tour

def calculate_cost(tour, depot_index):
    total_dist = d_matrix[depot_index, tour[0]] 
    for i in range(1, len(tour)):
        total_dist += d_matrix[tour[i - 1], tour[i]]
    total_dist += d_matrix[tour[-1], depot_index]
    return total_dist

def crossover(parent1, parent2):
    cut_idx = random.randint(1, len(parent1)-2)
    child = parent1[:cut_idx] + [c for c in parent2 if c not in parent1[:cut_id]]
    return child

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

# Initialize population
population = [create_individual() for _ in range(population_size)]

# Evolution process
for _ in range(n_generations):
    # Evaluate
    ranked_population = sorted(population, key=lambda x: calculate_cost(x, 0) + calculate_cost(x, 1))
    # Select
    survivors = ranked_population[:population_size // 2]
    # Crossover and mutate
    offspring = []
    while len(offspring) < population_size // 2:
        parent1, parent2 = random.sample(survivors, 2)
        child = crossover(parent1, parent2)
        mutate(child)
        offspring.append(child)
    population = survivors + offspring

# Extract best solution
best_solution = sorted(population, key=lambda x: calculate_cost(x, 0) + calculate_cost(x, 1))[0]

# Divide the tour into two, one for each robot 
# This is a simple split which can be modified by more sophisticated strategies
split_index = len(best_solution)//2
robot0_tour = [0] + best_solution[:split_index] + [0]
robot1_tour = [1] + best_pre_solution[`:split_index] + [1]

robot0_cost = calculate_cost(best_solution[:split_index], 0)
robot1_cost = calculate_cost(best_solution[split_index:], 1)
total_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", total_cost)