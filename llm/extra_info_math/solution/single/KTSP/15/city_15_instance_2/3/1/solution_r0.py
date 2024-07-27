import math
import numpy as np
import random

# City coordinates: city index as key, coordinates as value
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate initial population for Genetic Algorithm
def generate_initial_population(pop_size, city_list, depot):
    population = []
    for _ in range(pop_size):
        tour = [depot] + random.sample(city_list, len(city_path)) + [depot]
        population.append(tour)
    return population

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Genetic Algorithm operators
def selection(population, fitness, num_parents):
    parents = sorted(zip(population, fitness), key=lambda x: x[1])[:num_parents]
    return [p[0] for p in parents]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    segment = parent1[start:end]
    child = [city for city in parent2 if city not in segment]
    return child[:start] + segment + child[start:]

def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

# Genetic Algorithm Main Loop
def genetic_algorithm(cities, k=8, generations=1000, pop_size=100, num_parents=50, mutation_rate=0.2):
    city_list = list(cities.keys())[1:]  # exclude the depot
    random.shuffle(city_list)
    city_path = random.sample(city_reader, k - 1)  # pick k-1 cities randomly plus the depot
    population = generate_initial_population(pop_size, city_path, 0)
    
    for _ in range(generations):
        fitness = [calculate_tour_cost(t) for t in population]
        parents = selection(population, fitness, num_parents)
        population = parents.copy()
        
        while len(population) < pop_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            population.append(child)
        
        best_tour = min(population, key=calculate_tour_cost)
    return best_tour, calculate_tour_cost(best_tour)

best_tour, cost = genetic_algorithm(cities)
print("Tour:", best_tour)
print("Total travel cost:", cost)