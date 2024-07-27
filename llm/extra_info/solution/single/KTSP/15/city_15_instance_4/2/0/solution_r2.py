import math
import random

# Define cities' coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return total_distance

def generate_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        sample = random.sample(range(1, len(cities)), num_cities - 1)
        population.append([0] + sample + [0])
    return population

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    child_filled = set(parent1[start:end])
    pointer = 0
    for city in parent2:
        if city not in child_filled:
            while pointer < len(child) and child[pointer] is not None:
                pointer += 1
            if pointer < len(child):
                child[pointer] = city
    child[0] = 0
    child[-1] = 0
    return child

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(cities, population_size=100, generations=500):
    population = generate_initial_population(population_starte, 12)
    for _ in range(generations):
        population.sort(key=calculate_total_distance)
        new_population = population[:2]  # Elitism
        while len(new_population) < population_size:
            p1, p2 = random.sample(population[:20], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    best_route = sorted(population, key=calculate_total_distance)[0]
    return best_route, calculate_total_distance(best_route)

# Execute the genetic algorithm
best_tour, total_travel_cost = genetic_algorithm(cities)

# Display results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)