import numpy as np
import random

# Coordinates of the cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total distance of a tour and maximum leg distance
def evaluate_tour(tour):
    total_distance = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = distance(tour[i], tour[i + 1])
        total_distance += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance
    return total_distance, max_leg_distance

# Genetic algorithm configurations
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.05):
    # Create initial population
    population = [[0] + random.sample(list(cities.keys())[1:], len(cities) - 1) + [0] for _ in range(population_size)]
    
    # Evolution process
    for generation in range(generations):
        # Evaluate population
        population = sorted(population, key=lambda tour: evaluate_tour(tour)[1])  # Sort by max leg distance
        
        # Selection (Top 50% survive)
        population = population[:population_size // 2]
        
        # Generate new population through crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    # Find the best solution in the final population
    best_tour = min(population, key=lambda tour: evaluate_tour(tour)[1])
    total_cost, max_distance = evaluate_tour(best_tour)
    return best_tour, total_cost, max_distance

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    middle = parent1[start:end]
    child = [0] + [city for city in parent2 if city in middle] + [0]
    return child

def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Execute the genetic algorithm
tour, total_cost, max_dist = genetic_algorithm(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)