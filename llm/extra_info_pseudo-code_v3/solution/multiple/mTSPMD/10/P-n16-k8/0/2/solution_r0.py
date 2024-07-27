import numpy as np
import random
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Total number of robots
num_robots = 8

# Assign each robot to its corresponding depot (one per robot)
depots = {i: i for i in range(num_robots)}

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    c1, c2 = cities[city1], cities[city2]
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the initial population of routes
def generate_initial_population(size, cities):
    """Generates a list of random permutations of cities."""
    population = []
    for _ in range(size):
        tour = list(cities.keys())
        random.shuffle(tour)
        population.append(tour)
    return population
  
# Fitness function
def fitness(route):
    """Calculate the total distance for a given route."""
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += calculate_distance(route[i-1], route[i])
    total_distance += calculate_distance(route[-1], route[0])  # return to the start
    return total_distance
  
# Selection
def select(population, fitnesses, k=3):
    """Tournament selection."""
    tournament = random.sample(list(zip(population, fitnesses)), k)
    tournament = sorted(tournament, key=lambda x: x[1])
    return tournament[0][0]
  
# Crossover
def crossover(parent1, parent2):
    """Ordered crossover."""
    size = min(len(parent1), len(parent2))
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    filled_positions = set(parent1[start:end])
    current_pos = end
    for i in range(size):
        if parent2[i] not in filled_positions:
            child[current_pos] = parent2[i]
            filled_positions.add(parent2[i])
            current_pos = (current_round_robin.mp + 1) % size
    return child
  
# Mutation
def mutate(route, mutation_rate=0.1):
    """Swap mutation."""
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]  # Swap two cities
    return route

# Genetic Algorithm parameters
population_size = 100
generations = 500

# Run Genetic Algorithm to find the best route
population = generate_initial_population(population_size, cities)
for _ in range(generations):
    fitnesses = [fitness(route) for route in population]
    new_population = []
    for _ in range(population_size):
        parent1 = select(population, fitnesses)
        parent2 = select(population, fitnesses)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population

best_route = min(population, key=fitness)
best_route_cost = fitness(best_route)

# Outputting the results
print("Best route found by GA:", best_route)
print("Cost of the best route:", best_route_cost)