import numpy as np
import random
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def calculate_distance(from_city, to_city):
    x1, y1 = cities[from_city]
    x2, y2 = cities[to_city]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial population of tours
def initial_population(population_size=100):
    population = []
    for _ in range(population_size):
        # Randomly select 9 cities in addition to the depot
        cities_chosen = random.sample(list(cities.keys())[1:], 9) 
        tour = [0] + cities_chosen + [0]
        population.append(tour)
    return population

# Evaluate the total travel cost of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    return total_distance

# Selection process: Select best tours
def select_best(population, num_best):
    scored_population = [(tour, evaluate_tour(tour)) for tour in population]
    scored_population.sort(key=lambda x: x[1])
    selected_tours = [x[0] for x in scored_population][:num_best]
    return selected_tours

# Crossover (recombine elements from two parent tours)
def crossover(parent1, parent2):
    child = parent1[:6] + parent2[6:10]
    fix_missing = set(parent1[1:10]).union(set(parent2[1:10])) - set(child[1:10])
    child[1:10] = [city if city in child[1:10] else fix_missing.pop() for city in child[1:10]]
    return [0] + child[1:10] + [0]

# Mutation (randomly swap two elements)
def mutate(tour, mutation_rate=0.15):
    if np.random.rand() < mutation_rate:
        i, j = np.random.choice(range(1, 10), 2, replace=False)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic Algorithm
def genetic_algorithm(population_size=100, generations=500):
    population = initial_population(population_size)
    best_score = float('inf')
    best_tour = None

    for _ in range(generations):
        selected = select_best(population, 20)  # Keep top 20% individuals
        # Generate new population
        population = []
        while len(population) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = mutate(crossover(parent1, parent2))
            population.append(child)
        
        # Check for new best
        current_best = min(population, key=evaluate_tour)
        current_score = evaluate_tour(current_best)
        if current_score < best_score:
            best_score = current_score
            best_tour = current_best

    return best_tour, best_score

# Run the genetic algorithm and print the results
best_tour, best_cost = genetic_algorithm()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)