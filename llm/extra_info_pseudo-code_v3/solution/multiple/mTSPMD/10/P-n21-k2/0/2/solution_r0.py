import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, randint, random
import heapq

# City Coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58),
    9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46),
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance Matrix Calculation
def compute_distances(coordinates):
    n = len(coordinates)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
    return distance_matrix

distance_matrix = compute_distances(coordinates)

# Genetic Algorithm Parameters
population_size = 100
generations = 500
mutation_rate = 0.1
crossover_rate = 0.8
tournament_size = 3

# GA Functions
def create_individual(cities):
    individual = list(range(2, len(cities)))  # Skip depots
    np.random.shuffle(individual)
    return individual

def evaluate(individual):
    total_cost = 0
    route0 = [0] + individual[:10] + [0] # First robot
    route1 = [1] + individual[10:] + [1] # Second robot
    for route in (route0, route1):
        for i in range(len(route) - 1):
            total_cost += distance_matrix[route[i]][route[i+1]]
    return total_cost

def selection(population, fitnesses):
    chosen_indices = sample(range(len(population)), k=tournament_size)
    best_index = min(chosen_indices, key=lambda i: fitnesses[i])
    return population[best_index]

def crossover(parent1, parent2):
    if random() < crossover_entries:
        point1, point2 = sorted(sample(range(1, len(parent1)-1), 2))
        child = [None] * len(parent1)
        child[point1:point2] = parent1[point1:point2]
        free_pos = [pos for pos in range(len(parent1)) if child[pos] is None]
        free_vals = [val for val in parent2 if val not in parent1[point1:point2]]
        for pos, val in zip(free_pos, free_vals):
            child[pos] = val
        return child
    return parent1 if random() < 0.5 else parent2

def mutate(individual):
    if random() < mutation_rate:
        point1, point2 = sample(range(len(individual)), 2)
        individual[point1], individual[point2] = individual[point2], individual[point1]
    return individual

# Initialize population
np.random.seed(42)
population = [create_individual(coordinates) for _ in range(population_size)]
fitnesses = [evaluate(individual) for individual in population]

# Main loop
for generation in range(generations):
    new_population = []
    for _ in range(population_size):
        parent1 = selection(population, fitnesses)
        parent2 = selection(population, fitnesses)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
    fitnesses = [evaluate(individual) for individual in population]

# Find best solution
best_index = np.argmin(fitnesses)
best_individual = population[best_index]
best_fitness = fitnesses[best_index]

# Extract tours
tour0 = [0] + best_individual[:10] + [0]
tour1 = [1] + best_individual[10:] + [1]
robot0_cost = sum(distance_matrix[tour0[i]][tour0[i+1]] for i in range(len(tour0) - 1))
robot1_cost = sum(distance_matrix[tour1[i]][tour1[i+1]] for i in range(len(tour1) - 1))

print("Robot 0 Tour:", tour0)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", tour1)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", robot0_cost + robot1_cost)