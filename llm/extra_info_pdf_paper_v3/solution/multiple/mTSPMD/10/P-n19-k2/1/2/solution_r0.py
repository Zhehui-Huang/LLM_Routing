import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates for the cities and depots
coordinates = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 43),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),   # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 27),  # City 13
    (37, 69),  # City 14
    (61, 33),  # City 15
    (62, 63),  # City 16
    (63, 69),  # City 17
    (45, 35)   # City 18
]

# Calculate the Euclidean distances between each pair of cities
def calculate_distances(coordinates):
    num_cities = len(coordinates)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(coordinates[i], coordinates[j])
    return distances

distances = calculate_distances(coordinates)

# Genetic Algorithm Components
def initialize_population(size, num_cities):
    population = []
    for _ in range(size):
        route = np.random.permutation(np.arange(2, num_cities)).tolist()
        population.append(route)
    return population

def calculate_route_cost(route, depot_start, depot_end):
    cost = distances[depot_start, route[0]] + distances[route[-1], depot_end]
    for i in range(len(route) - 1):
        cost += distances[route[i], route[i + 1]]
    return cost

def fitness(route, depot_start, depot_end):
    return 1 / calculate_route_cost(route, depot_start, depot_end)

def selection(population, scores, k=3):
    selected_indices = np.random.randint(len(population), size=k)
    selected_scores = [scores[i] for i in selected_indices]
    return population[np.argmax(selected_scores)]

def crossover(parent1, parent2):
    size = len(parent1)
    p1, p2 = [0]*size, [0]*size

    # Choose crossover points
    cx1, cx2 = sorted(random.sample(range(size), 2))

    # Create child by crossover
    child = [None]*size
    child[cx1:cx2] = parent1[cx1:cx2]

    # Fill the remaining on the child with parents 2 items
    pos = cx2
    for item in parent2:
        if item not in child:
            if pos >= size:
                pos = 0
            child[pos] = item
            pos += 1
    return child

def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(len(route)), 2))
        route[i], route[j] = route[j], route[i]

# GA Application
def genetic_algorithm(depot_start, depot_end, generations=500, population_size=100, mutation_rate=0.05):
    population = initialize_population(population_size, len(coordinates))
    best_route = None
    best_score = float('inf')

    for _ in range(generations):
        scores = [fitness(route, depot_start, depot_end) for route in population]
        new_population = []

        for _ in range(population_size // 2):
            parent1 = selection(population, scores)
            parent2 = selection(population, scores)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population
        current_best_score = max(scores)
        if 1/current_best_score < best_score:
            best_score = 1/current_best_score
            best_route = population[scores.index(max(scores))]

    return best_route, best_score

# Running for both robots
robot0_route, robot0_cost = genetic_algorithm(0, 0)
robot1_route, robot1_cost = genetic_algorithm(1, 1)

# Preparing results
robot0_tour = [0] + robot0_route + [0]
robot1_tour = [1] + robot1_route + [1]

# Output the solution
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_cost}")
print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {robot1_cost}")
print(f"Overall Total Travel Cost: {robot0_cost + robot1_cost}")