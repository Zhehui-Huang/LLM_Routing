import numpy as np
import random
from math import sqrt

# Define the function for calculating Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Genetic Algorithm Implementation
def initialize_population(size, num_cities):
    population = []
    for _ in range(size):
        # ensure that all robots start at the depot city 0 and end with city 1
        route = [0] + random.sample([i for i in range(2, num_cities)], num_cities - 2) + [1]
        population.append(route)
    return population

def evaluate_fitness(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return total_cost

def crossover(route1, route2):
    start, end = sorted(random.sample(range(1, len(route1) - 2), 2))
    middle = route1[start:end]
    new_route = [0] + [city for city in route2 if city not in middle] + [1]
    insertion_point = random.randint(1, len(new_route) - len(middle) - 1)
    return new_route[:insertion_point] + middle + new_route[insertion_point:]

def mutate(route, probability=0.1):
    if random.random() < probability:
        i, j = random.sample(range(1, len(route) - 1), 2)
        route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(num_generations, population_size, num_cities):
    population = initialize_population(population_size, num_cities)
    
    for generation in range(num_generations):
        # Ranking by fitness
        population.sort(key=evaluate_fitness)
        new_generation = population[:2]  # Elitism

        # Generate new offsprings
        while len(new_generation) < population_size:
            r1, r2 = random.sample(population[:10], 2)  # Tournament Selection
            child = crossover(r1, r2)
            child = mutate(child)
            new_generation.append(child)
        
        population = new_generation
    
    best_route = min(population, key=evaluate_fitness)
    best_cost = evaluate_fitness(best_route)
    return best_route, best_cost

# Run the Genetic Algorithm
best_route, best_cost = genetic_algorithm(num_generations=100, population_size=50, num_cities=len(cities))
robot_0_cost = evaluate_fitness(best_route)

# Output format setup
print(f'Robot 0 Tour: {best_route}')
print(f'Robot 0 Total Travel Cost: {robot_0_cost}')
print(f'Overall Total Travel Cost: {robot_0_cost}')