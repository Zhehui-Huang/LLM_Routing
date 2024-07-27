import numpy as np
import random

# Coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Create a matrix of Euclidean distances
n = len(coordinates)
dist_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Parameters for Genetic Algorithm
population_size = 100
generations = 200
mutation_rate = 0.1
tournament_size = 5
tour_length_max = 13  # including the depot

# Helper function to generate a random tour
def create_tour():
    tour = random.sample(range(1, n), tour_length_max - 1)
    tour.insert(0, 0)
    tour.append(0)
    return tour

# Helper functions for the genetic algorithm
def calculate_cost(tour):
    total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost

def crossover(tour1, tour2):
    start, end = sorted(random.sample(range(1, tour_length_max - 1), 2))
    child = [None]*tour_length_max
    child[0], child[-1] = 0, 0
    child[start:end+1] = tour1[start:end+1]
    
    for i in range(1, tour_length_max - 1):
        if tour2[i] not in child:
            for j in range(1, tour_length_max - 1):
                if child[j] is None:
                    child[j] = tour2[i]
                    break
    return child

def mutate(tour):
    i, j = sorted(random.sample(range(1, tour_length_max - 1), 2))
    tour[i], tour[j] = tour[j], tour[i]

def select_parent(pool):
    best = random.choice(pool)
    for _ in range(tournament_size - 1):
        cont = random.choice(pool)
        if calculate_cost(cont) < calculate_cost(best):
            best = cont
    return best

# Initialize population
population = [create_tour() for _ in range(population_size)]

# Genetic Algorithm Execution
for generation in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            mutate(child)
        new_population.append(child)
    population = new_population

# Find best solution
best_solution = min(population, key=calculate_cost)
best_cost = calculate_cost(best_solution)

# Output
print("Tour:", best_solution)
print("Total travel cost:", best_cost)