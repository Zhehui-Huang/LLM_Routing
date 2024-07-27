import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Define city coordinates
city_coords = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Helper function to calculate euclidean distances between cities
def calculate_distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# Generate a random initial population of routes
def initial_population(pop_size, city_keys, tour_length):
    population = []
    for _ in range(pop_size):
        tour = [0] + random.sample(city_keys[1:], tour_length - 1)
        population.append(tour + [0])  # ensuring the tour starts and ends at depot (0)
    return population

# Evaluate the total travel cost of a single route
def evaluate_route(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += calculate_distance(route[i], route[i+1])
    return total_cost

# Crossover operation for genetic algorithm
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    start, stop = sorted(random.sample(range(size), 2))
    
    child[start:stop] = parent1[start:stop]
    p2_items = [item for item in parent2 if item not in child]
    p2_pos = 0
    for i in range(size):
        if child[i] is None:
            child[i] = p2_items[p2_pos]
            p2_pos += 1

    return child

# Mutation operation for genetic algorithm
def swap_mutation(route):
    idx1, idx2 = random.sample(range(1, len(route) - 1), 2)  # exclude depot position 0 and last
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Genetic algorithm to find the best route
def genetic_algorithm(city_keys, generations=250, pop_size=50, tour_length=13):
    population = initial_population(pop_size, city_keys, tour_length)
    best_route = None
    best_cost = float('inf')

    for _ in range(generations):
        # Assess the fitness
        fitness_scores = [(evaluate_route(route), route) for route in population]
        fitness_scores.sort()
        best_current_cost, best_current_route = fitness_scores[0]

        if best_current_cost < best_cost:
            best_cost, best_route = best_current_cost, best_current_route

        # Selection (top 50%)
        selected = [route for score, route in fitness_scores[:len(fitness_scores) // 2]]

        # Crossover and mutation
        next_gen = []
        while len(next_gen) < pop_size:
            if len(next_gen) + 1 == pop_size:  # keep population size consistent
                next_gen.append(best_current_route)
            parent1, parent2 = random.sample(selected, 2)
            child = ordered_crossover(parent1, parent2)
            child = swap_mutation(child)
            next_gen.append(child)

        population = next_gen

    return best_route, best_cost

# Solving the problem
best_tour, best_travel_cost = genetic_algorithm(list(city_coords.keys()))

print("Tour:", best_tour)
print("Total travel cost:", best_travel_cost)