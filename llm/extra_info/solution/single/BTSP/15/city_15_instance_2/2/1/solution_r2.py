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

# Fitness function calculates the Max distance between consecutive cities and total distance of the tour
def fitness(route, dist_matrix):
    max_distance = max(dist_matrix[route[i - 1], route[i]] for i in range(1, len(route)))
    total_distance = sum(dist_matrix[route[i - 1], route[i]] for i in range(1, len(route)))
    return max_distance, total_distance

# Create a random tour (random permutation of cities, excluding the depot)
def create_route(city_count):
    route = list(range(1, city_count)) 
    random.shuffle(route)
    return [0] + route + [0]  # starting and ending at the depot city (0)

# Mutate a route using the swap method excluding the first and last elements
def mutate(route, mutation_rate):
    for i in range(1, len(route) - 2):
        if random.random() < mutation_rate:
            j = random.randint(1, len(route) - 2)
            route[i], route[j] = route[j], route[i]
    return route

# Select best route using tournament selection
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda ind: ind[0][0])  # Minimize max distance

# Generate the next generation of routes
def next_generation(current_gen, dist_matrix, tournament_size, mutation_rate):
    next_gen = []
    for _ in range(len(current_gen)):
        parent = tournament_selection(current_gen, tournament_size)[1]
        child = mutate(parent[:], mutation_rate)
        next_gen.append((fitness(child, dist_matrix), child))
    return next_gen

# Set the environment and algorithm parameters
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44),
          (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]
dist_matrix = distance_matrix(cities)

population_size = 100
generations = 500
mutation_rate = 0.05
tournament_size = 20

# Initialize population
population = [(fitness(create_route(len(cities)), dist_matrix), create_route(len(cities))) for _ in range(population_size)]

# Run evolution
for generation in range(generations):
    population = next_generation(population, dist_matrix, tournament_size, mutation_rate)

# Extract the best solution
best_solution = min(population, key=lambda ind: ind[0][0])
best_route, (max_distance, total_cost) = best_solution[1], best_solution[0]

# Display the results
print("Tour:", best_route)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))