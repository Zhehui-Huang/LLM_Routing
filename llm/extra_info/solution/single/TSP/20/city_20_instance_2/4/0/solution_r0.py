import numpy as np
import random

# City coordinates from the given description
coords = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

cities_count = len(coords)

# Calculate distance matrix
def calc_dist_matrix(coords):
    dist_matrix = np.zeros((cities_count, cities, count))
    for i in range(cities_count):
        for j in range(cities_count):
            if i != j:
                dist = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
                dist_matrix[i][j] = dist
    return dist_matrix

dist_matrix = calc_dist_matrix(coords)

# Genetic Algorithm components
def calculate_tour_length(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_population(pop_size, num_cities):
    return [random.sample(range(1, num_cities), num_cities - 1) for _ in range(pop_size)]

def crossover(parent1, parent2):
    "Implements ordered crossover"
    start = random.randint(0, len(parent1) - 2)
    end = random.randint(start, len(parent1) - 1)
    child = [None] * len(parent1)
    child[start:end+1] = parent1[start:end+1]
    filler = iter([x for x in parent2 if x not in child])
    child = [next(filler) if x is None else x for x in child]
    return child

def mutation(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(dist_matrix, num_cities, num_generations=500, pop_size=100, mutation_rate=0.05):
    population = generate_initial_population(pop_size, num_cities)
    for generation in range(num_generations):
        population = sorted(population, key=lambda x: calculate_tour_length([0] + x + [0], dist_matrix))
        new_population = population[:2]  # Elitism: carry forward the best solutions
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population[:50], 2)  # Select from the best 50%
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_tour = min(population, key=lambda x: calculate_tour_length([0] + x + [0], dist_matrix))
    return [0] + best_tour + [0], calculate_tour_length([0] + best_tour + [0], dist_matrix)

# Run the Genetic Algorithm
best_tour, total_cost = genetic_algorithm(dist_matrix, cities_count)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")