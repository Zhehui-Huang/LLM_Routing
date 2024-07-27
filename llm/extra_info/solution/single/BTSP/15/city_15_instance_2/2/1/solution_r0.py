import numpy as np
import random
from math import sqrt

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the complete distance matrix
def distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(cities[i], cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = d
    return dist_matrix

# Fitness function to minimize (max distance between consecutive cities)
def fitness(route, dist_matrix):
    max_distance = max(dist_matrix[route[i-1], route[i]] for i in range(len(route)))
    return max_distance, sum(dist_matrix[route[i-1], route[i]] for i in range(len(route)))

# Generate a random individual (route)
def create_route(cities):
    route = list(range(1, len(cities)))  # exclude the depot city initially
    random.shuffle(route)
    return [0] + route + [0]  # Start and end at the depot city

# Mutate a route (simple swap mutation)
def mutate(route, mutation_rate):
    for swap in range(len(route)-2):  # exclude the first and last item (depot city)
        if random.random() < mutation_rate:
            i, j = random.randint(1, len(route)-2), random.randint(1, len(route)-2)
            route[i], route[j] = route[j], route[i]
    return route

# Perform a tournament selection
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda ind: ind[0])  # comparing based on fitness[0]: max distance

# Create the next generation
def next_generation(current_gen, dist_matrix, tournament_size, mutation_rate):
    next_gen = []
    for i in range(len(current_graph)):
        parent1 = tournament_selection(current_gen, tournament_size)[1]
        # Simple crossover not needed as we are mainly focusing on mutations for the TSP problem
        child = mutate(parent1[:], mutation_rate)
        next_gen.append((fitness(child, dist_matrix), child))
    return next_gen

# Initial settings
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

dist_matrix = distance_matrix(cities)

# Genetic algorithm parameters
population_size = 100
generations = 500
mutation_rate = 0.05
tournament_size = 20

# Create initial population
population = [(fitness(create_route(cities), dist_matrix), create_route(cities)) for _ in range(population_size)]

# Evolution process
for generation in range(generations):
    population = next_generation(population, dist_matrix, tournament_size, mutation_rate)

# Find the best solution from the final generation
best_solution = min(population, key=lambda ind: ind[0][0])
best_route, (max_distance, total_cost) = best_solution[1], best_solution[0]

# Print results
print("Tour:", best_route)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))