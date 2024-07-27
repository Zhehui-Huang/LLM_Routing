import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Define the coordinates of the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Calculate the distance matrix
num_cities = len(cities)
distance_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Number of cities to visit, including the depot
k = 13

# Genetic Algorithm Configuration
population_size = 50
generations = 500
mutation_rate = 0.1

# Initialize a population with random tours
population = []
for _ in range(population_size):
    tour = [0] + random.sample(list(cities.keys())[1:], k-2) + [0]
    population.append(tour)

def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Genetic Algorithm Evolution
for generation in range(generations):
    # Evaluate the population
    scored_population = [(tour, calculate_cost(tour)) for tour in population]
    scored_population.sort(key=lambda x: x[1])
    
    # Select the fittest: elitism and tournament selection
    new_population = [t for t, c in scored_population[:2]]  # Elitism
    tournament_size = 5
    
    while len(new_population) < population_size:
        tournament = random.sample(scored_population, tournament_size)
        tournament.sort(key=lambda x: x[1])
        parent1 = tournament[0][0]
        parent2 = tournament[1][0]
        
        # Crossover: single point
        cross_point = random.randint(1, k-2)
        child = parent1[:cross_type] + [c for c in parent2 if c not in parent1[:cross_point]]
        child = child[:k-1] + [0]  # make sure it's a valid tour
        
        # Mutation: swap two points with a probability
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(1, k-1), 2)
            child[idx1], child[idx2] = child[idx2], child[idx1]
        
        new_population.append(child)
    
    population = new_population

# Get the best tour from the final population
final_scored_population = [(tour, calculate_cost(tour)) for tour in population]
best_tour, best_cost = min(final_scored_population, key=lambda x: x[1])

print("Tour:", best_tour)
print("Total travel cost:", best_cost)