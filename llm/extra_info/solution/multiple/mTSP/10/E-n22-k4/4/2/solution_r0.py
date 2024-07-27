import numpy as np
import random
from itertools import permutations

# Cities coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Distance matrix construction
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Configuration
num_robots = 4
depot = 0

# Genetic Algorithm Parameters
population_size = 50
num_generations = 500
mutation_rate = 0.05

# Helper functions
def calculate_total_distance(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def create_random_tour():
    tour = list(range(1, num_cities))  # exclude depot when creating tours
    random.shuffle(tour)
    return [depot] + tour + [depot]  # starts and ends at depot

def crossover(parent1, parent2):
    # Single point crossover
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return [depot] + child + [depot]

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = np.random.randint(1, len(tour)-1, 2)
        tour[i], tour[j] = tour[j], tour[i]

# Initialize population
population = [create_random_tour() for _ in range(population_size)]

# Genetic Algorithm
best_tours = None
best_cost = float('inf')

for generation in range(num_generations):
    # Evaluate
    graded = [(calculate_total_distance(tour), tour) for tour in population]
    graded = sorted(graded, key=lambda x: x[0])
    population = [x[1] for x in graded]

    # Find best
    if graded[0][0] < best_cost:
        best_cost = graded[0][0]
        best_tours = population[0]

    # Select survivors (elitism & tournament)
    selected = population[:10]
    while len(selected) < population_size:
        i, j = np.random.randint(0, 10, 2)
        candidate = crossover(population[i], population[j])
        mutate(candidate)
        selected.append(candidate)

    population = selected

# Final best result
best_tours = best_tours[1:-1]
robot_tours = [best_tours[i::num_robots] for i in range(num_robots)]
robot_tours = [[depot] + tour + [depot] for tour in robot_tours]
robot_costs = [calculate_total_distance(tour) for tour in robot_tours]
overall_cost = sum(robot_costs)

# Output
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")