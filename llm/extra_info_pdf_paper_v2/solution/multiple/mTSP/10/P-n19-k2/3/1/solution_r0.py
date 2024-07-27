import numpy as np
from scipy.spatial.distance import euclidean
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distances between each pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = calculate_distances(cities)

# Helper function to evaluate cost of a tour
def evaluate_tour(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1]][tour[i]]
    return cost

# Genetic Algorithm components
def create_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        tour = list(range(1, num_cities))  # exclude the depot city 0 for initial tours
        random.shuffle(tour)
        population.append(tour)
    return population

def crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[idx1:idx2] = parent1[idx1:idx2]
    pointer = 0
    for item in parent2:
        if item not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = item
    return child

def mutate(tour, mutation_rate):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

def selection(population, k=5):
    selected = random.choices(population, k=k)
    selected = sorted(selected, key=lambda x: evaluate_tour([0] + x + [0]))
    return selected[0]

# Main Genetic Algorithm function
def genetic_algorithm(dist_matrix, num_cities, population_size=50, generations=100, mutation_rate=0.1):
    population = create_initial_population(population_size, num_cities)
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = selection(population)
            parent2 = selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population

    best_tour = sorted(population, key=lambda x: evaluate_tour([0] + x + [0]))[0]
    best_cost = evaluate_tour([0] + best_tour + [0])
    return best_tour, best_cost

# Deploy the GA for the two robots
best_tour1, best_cost1 = genetic_algorithm(dist_matrix, len(cities))
remaining_cities = [city for city in range(1, len(cities)) if city not in best_tour1]
best_tour2, best_cost2 = genetic_algorithm(dist_matrix, len(remaining_cities))

# Output the results
print("Robot 0 Tour: ", [0] + best_tour1 + [0])
print("Robot 0 Total Travel Cost: ", best_cost1)
print("Robot 1 Tour: ", [0] + best_tour2 + [0])
print("Robot 1 Total Travel Cost: ", best_cost2)

total_cost = best_cost1 + best_cost2
print("Overall Total Travel Cost: ", total_cost)