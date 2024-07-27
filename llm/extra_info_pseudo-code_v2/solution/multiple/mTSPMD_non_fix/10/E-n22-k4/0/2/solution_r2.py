import numpy as np
import random
from math import sqrt, inf

# Define cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance function
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate initial solution
def generate_initial_population(size, cities):
    population = []
    city_list = list(cities.keys())[4:]  # excluding depots
    for _ in range(size):
        random.shuffle(city_list)
        split_indices = sorted(random.sample(range(1, len(city_list)), 3))
        individual = [0] + city_list[:split_indices[0]] + \
                     [0] + city_list[split_indices[0]:split_indices[1]] + \
                     [0] + city_list[split_indices[1]:split_indices[2]] + \
                     [0] + city_list[split_indices[2]:] + [0]
        population.append(individual)
    return population

# Fitness function
def calculate_fitness(individual):
    total_cost = 0
    for i in range(0, len(individual), 5):  # Assume each robot has five cities to visit
        tour_cost = distance(cities[0], cities[individual[i+1]])  # start from depot 0
        for j in range(i+1, i+4):
            tour_cost += distance(cities[individual[j]], cities[individual[j+1]])
        tour_cost += distance(cities[individual[i+4]], cities[0])  # return to depot
        total_cost += tour_cost
    return total_cost

# Simple Genetic Algorithm Steps
def simple_genetic_algorithm(cities, iterations=100, population_size=20):
    population = generate_initial_population(population_size, cities)
    best_solution = None
    best_cost = inf

    for _ in range(iterations):
        # Evaluate population
        evaluated = [(calculate_fitness(ind), ind) for ind in population]
        evaluated.sort()  # Sort by fitness which is total cost here

        # Best solution in current generation
        current_best = evaluated[0][1]
        current_best_cost = evaluated[0][0]

        if current_best_cost < best_cost:
            best_solution = current_best
            best_cost = current_best_cost

        # Create a new generation (simple crossover and mutation)
        new_population = []
        while len(new_population) < population_size:
            # Select two parents - simplest select the best two
            parent1, parent2 = random.sample(population, 2)
            # Crossover (simple midpoint crossover)
            midpoint = len(parent1) // 2
            child = parent1[:midpoint] + parent2[midpoint:]
            # Mutation (simple swap mutation)
            swap_idx1, swap_idx2 = random.sample(range(len(child)), 2)
            child[swap_idx1], child[swap_idx2] = child[swap_idx2], child[swap_idx1]
            new_population.append(child)

        population = new_population

    return best_solution, best_cost

# Finding the best tour via genetic algorithm
best_tour, best_tour_cost = simple_genetic_algorithm(cities)

# Extract and print the tours per robot
print("Best tour:", best_tour)
print("Best tour cost:", best_tour_cost)