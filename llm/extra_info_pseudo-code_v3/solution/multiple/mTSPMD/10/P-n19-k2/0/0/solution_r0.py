import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Number of robots and their depots
num_robots = 2
depots = [0, 1]  # Robot 0 -> Depot 0, Robot 1 -> Depot 1

# Helper function: Calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# Genetic Algorithm Components
def create_initial_population(num_individuals, cities):
    return [random.sample(cities, len(cities)) for _ in range(num_individuals)]

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[idx1:idx2] = parent1[idx1:idx2]
    child = [p for p in parent1[idx1:idx2]] + [c for c in parent2 if c not in parent1[idx1:idx2]]
    return child

def mutate(tour, mutation_rate=0.05):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(cities, num_individuals=100, generations=500):
    population = create_initial_population(num_individuals, cities)
    best_cost = float('inf')
    best_solution = None
    
    for _ in range(generations):
        new_population = []
        for i in range(num_individuals):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
            child_cost = tour_cost([depots[0]] + child + [depots[0]])
            if child_cost < best_cost:
                best_cost = child_cost
                best_solution = [depots[0]] + child + [depots[0]]
                
        population = new_population
        
    return best_solution, best_cost

# Split cities for each robot, ignoring depots
cities = list(range(2, len(coordinates)))

# GA application
tour, cost = genetic_algorithm(cities)
print(f"Robot 0 Tour: {tour}")
print(f"Robot 0 Total Travel Cost: {cost:.2f}")

# Apply GA for a second robot, if needed based on problem specifics.
# This example assumes only one Robot and seed city set is adjusted accordingly,
# additional robots would need similar GA invocations with adjusted seeds or city sets.