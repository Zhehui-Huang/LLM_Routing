import numpy as np
import random
from scipy.spatial import distance

# Define cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Number of cities to visit including the depot
num_cities_to_visit = 16

# Genetic Algorithm parameters
population_size = 50
generations = 500
mutation_rate = 0.1

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Evaluate total distance of a tour
def evaluate_tour(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Create initial random tour
def create_random_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    while tour[0] != 0:
        random.shuffle(tour)
    return tour[:num_cities_to_visit] + [0]  # ensure it's a round trip

# Mutate a tour
def mutate(tour):
    if random.random() < mutation_rate:
        i, j = np.random.randint(1, num_cities_to_visit, 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Crossover two parents to produce two children
def crossover(parent1, parent2):
    child = parent1[:num_cities_to_visit//2] + parent2[num_cities_to_visit//2:num_cities_to_visit]
    missing = set(cities.keys()) - set(child)
    child += list(missing)
    random.shuffle(child)
    if child[0] != 0:
        child[child.index(0)], child[0] = child[0], child[child.index(0)]
    return child + [0]  # ensure round trip

# Genetic algorithm to find the optimal tour
def genetic_algorithm():
    population = [create_random_tour() for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=evaluate_tour)
        next_generation = population[:2]  # Elitism
        while len(next_generation) < population_size:
            parents = random.sample(population[:population_size // 2], 2)
            child1 = crossover(parents[0], parents[1])
            child1 = mutate(child1)
            next_generation.append(child1)
        population = next_generation
    best_tour = min(poplication, key=evaluate_tour)
    return best_tour, evaluate_tour(best_tour)

# Solve the problem using the genetic algorithm
best_tour, best_cost = genetic_algorithm()

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)