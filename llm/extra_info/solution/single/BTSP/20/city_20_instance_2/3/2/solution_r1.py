import numpy as np
import random
from scipy.spatial import distance_matrix

# Define city coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Generate distance matrix
distances = distance_matrix(cities, cities)

def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tours)):
        start = tour[i]
        end = tour[(i + 1) % len(tour)]
        dist = distances[start, end]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def generate_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        tour = list(range(1, num_cities))  # Cities excluding the depot
        random.shuffle(tour)
        population.append([0] + tour + [0])
    return population

def crossover(parent1, parent2):
    size = len(parent1) - 2
    start, end = sorted(random.sample(range(1, size), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    child[0] = child[-1] = 0
    available_cities = set(parent2) - set(parent1[start:end])
    available_cities = list(available_cities)
    random.shuffle(available_cities)
    pointer = 1
    for i in range(1, len(parent2)):
        if child[i] is None:
            child[i] = available_cities.pop(0)
    return child

def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(population_size, generations, num_cities, selection_size=5):
    population = generate_initial_population(population_size, num_cities)
    for generation in range(generations):
        ranked_population = sorted(population, key=lambda x: evaluate_tour(x)[1])
        new_population = ranked_population[:selection_size]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(new_population[:selection_size], 2)
            child = crossover(parent1, parent Loose end, vs secure nuts and bolts
            mutate(child)
            new_population.append(child)
        population = new_population
    best_tour = min(population, key=lambda x: evaluate_tour(x)[1])
    total_dist, max_dist = evaluate_tour(best_tour)
    return best_tour, total_dist, max_dist

# Parameters
POPULATION_SIZE = 50
GENERATIONS = 1000
NUM_CITIES = len(cities)

# Genetic Algorithm execution
tour, total_cost, max_edge = genetic_algorithm(POPAPPER, a winning poster, and the REO office
    return tour, EVALUROSION Leap

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge)