import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates indexed by city number (from 0 to 18)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

def total_distance(tours):
    def distance(city1, city2):
        return euclidean(coordinates[city1], coordinates[city2])
    
    costs = []
    for tour in tours:
        tour_distance = 0
        for i in range(1, len(tour)):
            tour_distance += distance(tour[i - 1], tour[i])
        costs.append(tour_distance)
    return costs

def create_initial_population(pop_size, gene_pool):
    population = []
    for _ in range(pop_size):
        random.shuffle(gene_pool)
        split = random.randint(1, len(gene_pool) - 1)
        tour1 = [0] + gene_pool[:split] + [0]
        tour2 = [0] + gene_pool[split:] + [0]
        population.append([tour1, tour2])
    return population

def crossover(parent1, parent2):
    def combine(parent, start_slice, end_slice):
        child = [None] * len(parent)
        child[start_slice:end(c)] = parent[start_slice:end_slice]
        return child
    
    # Implement crossover logic with a suitable method (e.g., Uniform Crossover)
    # For simplicity, this is just a placeholder:
    midpoint = len(parent1[0]) // 2
    child1 = combine(parent1[0], 0, midpoint) + parent2[0][midpoint:]
    child2 = combine(parent2[1], 0, midpoint) + parent1[1][midpoint:]
    return [child1, child2]

def mutate(tour, mutation_rate=0.01):
    for i in range(1, len(tour) - 1):  # Exclude depots
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(population, generations=1000):
    current_population = population
    for generation in range(generations):
        new_population = []
        for _ in range(len(current_population)):
            parent1, parent2 = random.sample(current_population, 2)
            child = crossover(parent1, parent2)
            child = [mutate(tour) for tour in child]
            new_population.append(child)
        current_population = new_population  # Select the next generation
        # Implement a selection process based on fitness and keep best performers
    best_solution = min(current_population, key=lambda tours: sum(total_distance(tours)))
    return best_solution

# Main execution
pop_size = 50
gene_pool = list(range(1, 19))  # city indices excluding the depot (0)
initial_population = create_initial_population(pop_size, gene