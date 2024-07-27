import numpy as m
import random
from scipy.spatial.distance import cdist

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots and their starting depot
robots = {i: i for i in range(8)}

def calculate_distance_matrix(cities):
    coords = list(cities.values())
    return cdist(coords, coords, 'euclidean')

def initial_population(size, cities, n_robots):
    # Creating initial population
    all_cities = list(cities.keys())[len(robots):]  # cities except depots
    return [random.sample(all_cities, k=len(all_cities)) for _ in range(size)]

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def fitness(tour, distance_matrix, depot):
    tour_with_depot = [depot] + tour + [depot]
    return calculate_tour_cost(tour_with_depot, distance_matrix)

def selection(population, scores, k=3):
    # Select k individuals and return the best
    selected_idx = random.choice([random.randint(0, len(population) - 1) for _ in range(k)])
    return population[selected_idx]

def crossover(p1, p2):
    size = min(len(p1), len(p2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp = p1[cxpoint1:cxpoint2+1]
    child = [item for item in p2 if item not in temp]
    return child[:cxpoint1] + temp + child[cxpoint1:]

def mutation(individual):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Setup configurations
n_iter = 500
pop_size = 50
mut_rate = 0.1
cross_rate = 0.7

# Calculate the distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Initial population
population = initial_population(pop_size, cities, len(robots))

# Evolution process
for i in range(n_iter):
    new_population = []
    scores = [fitness(indiv, distance_matrix, robots[i % len(robots)]) for indiv in population]
    for _ in range(pop_size):
        parent1 = selection(population, scores)
        parent2 = selection(population, scores)
        child = crossover(parent1, parent2) if random.random() < cross_...