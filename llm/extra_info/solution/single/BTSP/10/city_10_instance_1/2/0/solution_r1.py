import numpy as np
import random
from math import sqrt

# Define the coordinates of the cities
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Fitness function to minimize the maximum distance between consecutive cities
def fitness(tour):
    max_dist = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return max_dist, sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to generate a new solution (tour)
def create_tour():
    tour = list(range(1, len(cities)))
    random.shuffle(tour)
    return [0] + tour + [0]

# Genetic operators: Crossover and Mutation
def crossover(tour1, tour2):
    start, end = sorted(random.sample(range(1, len(tour1) - 1), 2))
    middle_segment = tour1[start:end]
    remaining_cities = [city for city in tour2 if city not in middle_segment]
    new_tour = remaining_cities[:start] + middle_segment + remaining_cities[start:]
    return [0] + new_tour + [0]

def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Main Genetic Algorithm
def genetic_algorithm(population_size=100, generations=500, mutation_rate=0.1):
    population = [create_tour() for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=lambda tour: fitness(tour)[0])  # Sort by maximum distance fitness
        new_population = [population[0]]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = mutate(crossover(parent1, parent2), mutation_rate)
            new_population.append(child)
        population = new_population
    best_tour = population[0]
    max_dist, total_cost = fitness(best_tour)
    return best_tour, total_cost, max_dist

# Run the algorithm and print the results
best_tour, total_cost, max_distance = genetic_algorithm()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")