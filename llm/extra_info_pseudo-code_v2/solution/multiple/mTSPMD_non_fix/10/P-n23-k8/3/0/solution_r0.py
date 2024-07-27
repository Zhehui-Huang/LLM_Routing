import numpy as np
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize parameters
num_robots = 8
num_cities = len(cities)
num_generations = 500
population_size = 100
crossover_rate = 0.8
mutation_rate = 0.2

# Generate initial population
def create_chromosome():
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

population = [create_chromosome() for _ in range(population_size)]

# Calculate cost of a given tour
def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Return to depot
    return cost

# Genetic operators
def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    offspring = [None] * size
    offspring[idx1:idx2] = parent1[idx1:idx2]
    p2_filtered = [item for item in parent2 if item not in offspring]
    offspring = [item if item is not None else p2_filtered.pop(0) for item in offspring]
    return offspring

def mutate(tour):
    idx1, idx2 = random.sample(range(len(tour)), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm():
    global population
    for generation in range(num_generations):
        new_population = []
        while len(new_population) < population_size:
            if random.random() < crossover_rate:
                p1, p2 = random.sample(population, 2)
                child = crossover(p1, p2)
                if random.random() < mutation_rate:
                    mutate(child)
                new_population.append(child)
            else:
                new_population.extend(random.sample(population, 2))  # Elitism
        population = sorted(new_population, key=calculate_cost)[:population_size]
    
    best_solution = min(population, key=calculate_cost)
    return best_solution, calculate_cost(best_solution)

best_tour, best_cost = genetic_algorithm()

# Format output
print('Optimal Tour (visits all cities starting and ending at depot city 0):')
print(best_tour)
print('Optimal Tour Total Travel Cost:', best_cost)