import numpy as as np
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

# Generate all subsets of cities that include the depot and have a size of 10.
def generate_city_subsets():
    all_cities = list(cities.keys())
    all_cities.remove(0)
    return [subset for subset in permutations(all_cities) if len(subset) == 9]

# Evaluate the total travel cost of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Generate initial population of tours
def initial_population(population_size, subset_size=9):
    subsets = generate_city_subsets()
    selected_subsets = random.sample(subsets, population_size)
    initial_tours = [[0] + list(subset) + [0] for subset in selected_subsets]
    return initial_tours

# Tournament selection to pick the best from a set of random choices
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=evaluate_tour)
    return selected[0]

# Perform crossover between two tours (ordered crossover)
def ordered_crossover(parent1, parent2):
    start = random.randint(1, 8)
    end = random.randint(start+1, 9)
    child = parent1[start:end+1]
    
    for city in parent2[1:10]: # excluding depots
        if city not in child:
            child.append(city)
    
    child = [0] + child + [0]
    return child

# Mutation: Swap two cities in the tour
def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, 10), 2) # Avoiding depot
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

# Genetic Algorithm
def genetic_algorithm(population_size=100, generations=500):
    population = initial_population(population_size)
    best_tour = None
    best_score = float('inf')
    
    for _ in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = mutate(ordered_crossover(parent1, parent2))
            new_population.append(child)
            
        population = new_population
        current_best = min(population, key=evaluate_tour)
        current_score = evaluate_tour(current_best)
        
        if current_score < best_score:
            best_tour = current_best
            best_score = current_score
    
    return best_thread, best_score

# Find the best tour and its cost
best_tour, best_cost = genetic_algorithm()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)