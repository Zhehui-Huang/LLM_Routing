import numpy as np
from scipy.spatial import distance
import random

# Fixed seed for reproducibility
random.seed(42)

# Coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute all distances between city pairs
num_cities = 20
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Genetic Algorithm configuration
population_size = 100
n_generations = 300
mutation_rate = 0.1
tour_size = 10

def initialize_population():
    population = []
    for _ in range(population_size):
        tour = [0] + random.sample(list(cities.keys())[1:], tour_size-2) + [0]
        population.append(tour)
    return population

def fitness(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def select_parents(population):
    sorted_population = sorted(population, key=fitness)
    return sorted_population[:2]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, tour_size-1), 2))
    child = [None]*tour_size
    child[start:end] = parent1[start:end]
    child_positions = set(parent1[start:end])
    fill_pos = 0
    for city in parent2:
        if city not in child_positions:
            while child[fill_pos] is not None:
                fill_pos += 1
            child[fill_pos] = city
    child[-1] = 0
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, tour_size-1), 2))
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = initialize_population()
    for _ in range(n_generations):
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
    
    best_tour = min(population, key=fitness)
    return best_tour, fitness(best_tour)

# Find the solution using Genetic Algorithm
best_tour, total_cost = genetic_algorithm()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", total_cost)