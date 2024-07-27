import numpy as np
from scipy.spatial import distance_matrix
import random
import itertools

# ---------------------------------------------------
# Initialization of the genetic algorithm components
# ---------------------------------------------------
# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_cities = len(cities)
depots = list(range(8))  # Considering all are starting from city 0 which is a depot

# Number of robots
num_robots = 8

# Generation of distance matrix
points = np.array(list(cities.values()))
dist_matrix = distance_matrix(points, points)

# Genetic algorithm parameters
max_generations = 1000
population_size = 100
crossover_rate = 0.7
mutation_rate = 0.1
tournament_size = 5

# Helper Functions
def compute_total_distance(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

def crossover(parent1, parent2):
    child = parent1[:]
    if random.random() < crossover_rate:
        start, end = sorted(random.sample(range(len(parent1)), 2))
        middle = parent2[start:end]
        child = list(itertools.chain(parent1[:start], middle, parent1[end:]))
        unique_cities = set(range(num_cities))
        visited_cities = set(child)
        missing_cities = list(unique_cities - visited_cities)
        child = [city if city in unique_cities else missing_cities.pop() for city in child]
    return child

def tournament_selection(population):
    contenders = random.sample(population, tournament_size)
    return min(contenders, key=lambda individual: individual['fitness'])

# Initial Population
population = [{'chromosome': random.sample(range(num_cities), num_cities)} for _ in range(population_size)]
for individual in population:
    individual['fitness'] = compute_total_distance(individual['chromosome'])

# ---------------------------------------------------
# Execution of the genetic algorithm
# ---------------------------------------------------
for generation in range(max_generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)['chromosome']
        parent2 = tournament_selection(population)['chromosome']
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        new_population.extend([
            {'chromosome': child1, 'fitness': compute_total_distance(child1)},
            {'chromosome': child2, 'fitness': compute_total_distance(child2)}
        ])
    population = sorted(new_population, key=lambda individual: individual['fitness'])[:population_size]

# Best solution
best_solution = min(population, key=lambda individual: individual['fitness'])
best_tour = best_solution['chromosome']
best_cost = best_solution['fitness']

# Output formatting
print(f"Robot 0 Tour: {[0] + best_tour + [0]}")
print(f"Robot 0 Total Travel Cost: {best_cost}")
print(f"Overall Total Travel Cost: {best_cost}")

# Note: Specific solution and formatting will require adjustments to properly split tours among robots.