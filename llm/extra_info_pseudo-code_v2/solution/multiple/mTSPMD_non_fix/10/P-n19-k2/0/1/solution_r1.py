import numpy as np
from itertools import permutations
from random import randint, shuffle, sample, random
from math import sqrt

# Helper function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities and their coordinates, excluding depots
cities = {
    2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Depots location
depots = {
    0: (30, 40), 1: (37, 52)
}

# All locations
all_locations = {**depots, **cities}

# Evolutionary parameters
population_size = 100
generations = 500
mutation_rate = 0.15
crossover_rate = 0.85

def initialize_population(city_list, pop_size, no_of_robots):
    population = []
    full_list = list(city_list.keys())
    for _ in range(pop_size):
        shuffle(full_list)
        route = full_list[:]
        population.append(route)
    return population

def calculate_total_cost(route):
    total_cost = 0
    tour_costs = []
    segment = [0] + route  # Starting from Depot 0
    for i in range(len(segment) - 1):
        cost = euclidean_distance(*all_locations[segment[i]], *all_locations[segment[i + 1]])
        total_cost += cost
    return total_cost

def crossover(parent1, parent2):
    idx1, idx2 = sorted(sample(range(len(parent1)), 2))
    child1_mid = parent2[idx1:idx2]
    child1 = [item for item in parent1 if item not in child1_mid]
    child1 = child1[:idx1] + child1_mid + child1[idx1:]
    return child1

def mutate(route):
    if random() < mutation_rate:
        idx1, idx2 = sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm():
    city_list = cities
    population = initialize_population(city_list, population_size, number_of_robots)
    current_best_route = None
    current_best_cost = float('inf')
    
    for _ in range(generations):
        new_population = []
        for i in range(0, population_size, 2):
            if i+1 < population_size:
                parent1, parent2 = population[i], population[i+1]
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
                mutate(child1)
                mutate(child2)
                new_population.extend([child1, child2])
        population = new_population
        
        for route in population:
            cost = calculate_total_cost(route)
            if cost < current_best_cost:
                current_best_cost = cost
                current_best_route = route
    
    return current_best_route, currentByVersion_cost

best_route, best_cost = genetic_algorithm()

# Print formatted tour and cost information
print("Best_route :", best_route)
print("Best_cost =", best_cost)