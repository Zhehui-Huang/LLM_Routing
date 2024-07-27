import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define city coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# Cost of the tour with focus on max distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Genetic algorithm components
def create_tour():
    tour = list(range(1, len(coordinates)))
    random.shuffle(tour)
    return [0] + tour + [0]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    middle = parent1[start:end]
    child = [0] + [city for city in parent2 if city in middle or city == 0] + [0]
    return child

def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm(population_size=100, generations=1000):
    population = [create_tour() for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda x: evaluate_tour(x)[1])
        new_population = population[:2]  # Elitism
        for _ in range(population_size - len(new_population)):
            parent1, parent2 = random.choices(population[:50], k=2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population

    best_tour = min(population, key=lambda x: evaluate_tour(x)[1])
    total_cost, max_distance = evaluate_tour(best_tour)
    return best_tour, total_cost, max_distance

# Running the GA with specified parameters
best_tour, total_cost, max_distance = genetic_algorithm()

# Outputting the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))