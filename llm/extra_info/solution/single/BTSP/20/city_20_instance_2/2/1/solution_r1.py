import math
import numpy as
import random

# Helper Function: Calculate Euclidean Distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Coordinates of the cities (index as city number)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
num_cities = len(coordinates)

# Create distance matrix
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(*coordinates[i], *coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity for traveling to the same city

# Genetic Algorithm to minimize the maximum distance between consecutive cities
def genetic_algorithm(coordinates, population_size, generations, mutation_rate):
    # Generation of Random Tours
    def generate_population(size, num_cities):
        population = []
        for _ in range(size):
            tour = list(range(1, num_cities))
            random.shuffle(tour)
            tour = [0] + tour + [0]
            population.append(tour)
        return population

    # Calculate Fitness as the inverse of the max distance between consecutive cities
    def calculate_fitness(tour):
        max_dist = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        return 1 / max_dist

    # Tournament Selection
    def select_tournament(population, scores, tournament_size=5):
        tournament = random.sample(list(zip(scores, population)), tournament_size)
        tournament.sort(reverse=True, key=lambda x: x[0])
        return tournament[0][1]

    # Two-point Crossover
    def crossover(parent1, parent2):
        if random.random() < crossover_rate:
            points = sorted(random.sample(range(1, len(parent1) - 1), 2))
            child = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
            fix_duplicate(child)
            return child
        return parent1

    # Mutation with swap strategy
    def mutate(tour):
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour) - 1), 2)
            tour[i], tour[j] = tour[j], tour[i]
        return tour

    # Handle duplicates and missing values in tour after crossover
    def fix_duplicate(child):
        counts = {k:0 for k in range(num_cities)}
        for city in child:
            counts[city] += 1
        missing = [k for k, v in counts.items() if v == 0]
        duplicates = [k for k, v in counts.items() if v > 1]
        replacement = dict(zip(duplicates, missing))
        for i, city in enumerate(child):
            if counts[city] > 1:
                child[i] = replacement[city]
                counts[city] -= 1

    population = generate_population(population_size, num_cities)
    best_tour = None
    best_score = float('inf')

    for _ in range(generations):
        scores = [calculate_fitness(tour) for tour in population]
        sorted_population = sorted(zip(scores, population), reverse=True)
        best_current_score, best_current_tour = sorted_population[0]
        if best_current_score < best_score:
            best_score, best_tour = best_current_score, best_current_tour
        new_population = [select_tournament(population, scores) for _ in range(population_size)]
        population = [mutate(crossover(new_population[i], new_population[(i+1) % population_size])) for i in range(population_size)]

    max_distance = 1 / best_score
    total_distance = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    return best_tour, total_distance, max_distance

# Parameters
population_size = 100
generations = 500
mutation_rate = 0.02
crossover_rate = 0.8

# Running the genetic algorithm
best_tour, total_distance, max_distance = genetic_algorithm(coordinates, population_size, generations, mutation_rate)

# Output
print("Tour:", best_tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)