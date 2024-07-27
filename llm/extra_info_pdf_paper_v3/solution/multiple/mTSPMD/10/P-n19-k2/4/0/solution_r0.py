import numpy as np
import random
from numpy.linalg import norm

# City coordinates, indexed by city id.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Constants
NUM_ROBOTS = 2
DEPOTS = {0: 0, 1: 1}

def euclidean_distance(p1, p2):
    return norm(np.array(p1) - np.array(p2))

def create_initial_population(size, cities):
    population = []
    city_ids = list(cities.keys())
    city_ids.remove(0)  # Depot city 0
    city_ids.remove(1)  # Depot city 1
    for _ in range(size):
        individual = city_ids.copy()
        random.shuffle(individual)
        population.append([0] + individual + [1])
    return population

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return cost

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(1, size-1), 2))
    child[start:end] = parent1[start:end]
    fill_idx = 0
    for gene in parent2:
        if gene not in child:
            while child[fill_idx] != -1:
                fill_idx += 1
            child[fill_idx] = gene
    return child

def mutate(route, mutation_rate=0.01):
    for i in range(1, len(route) - 1):  # Do not mutate depots
        if random.random() < mutation_rate:
            j = random.randint(1, len(route) - 2)
            route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(max_generations, population_size=100):
    population = create_initial_population(population_size, cities)
    best_route = None
    best_cost = float('inf')
    
    for generation in range(max_generations):
        new_population = []
        costs = []
        
        for route in population:
            cost = calculate_route_cost(route)
            costs.append((cost, route))
            if cost < best_cost:
                best_cost = cost
                best_route = route
        
        costs.sort()  # Sort by cost
        population = [route for (_, route) in costs[:population_size//2]]  # Elitism: Top 50%
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_route, best_cost

best_route, best_cost = genetic_algorithm(100)
print("Best Route:", best_route)
print("Best Cost:", best_cost)