import math
import numpy as np
import random

# Helper Function: Calculate Euclidean Distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Define city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities
num_cities = len(coordinates)

# Create a distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(*(coordinates[i]), *(coordinates[j]))

# Genetic Algorithm configuration
num_generations = 500
population_size = 50
tournament_size = 5
mutation_rate = 0.20

# Initial population (random tours) including the return to the depot
population = [[0] + random.sample(range(1, num_cities), num_cities - 1) + [0] for _ in range(population_size)]

# Helper to evaluate and sort by the criteria: Max distance between consecutive cities
def evaluate(tour):
    max_leg_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return max_leg_distance

# Evolution process
for generation in range(num_generations):
    # Evaluate current population
    population_with_fitness = [(evaluate(tour), tour) for tour in population]
    population_with_fitness.sort()  # sort by max distance minimally

    # Selection: Tournament
    def tournament():
        contenders = random.sample(population_with_fitness, tournament_size)
        return min(contenders, key=lambda x: x[0])[1]

    # Produce next generation
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = tournament(), tournament()
        # Crossover - Single point between the first and last city
        if random.random() < 0.85:  # Crossover rate
            cut = random.randint(1, num_cities - 1)
            offspring = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
            offspring = [0] + offspring + [0]
        else:
            offspring = parent1  # If no crossover, pass parent directly
            
        # Mutation - Swap two cities
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, num_cities), 2)
            offspring[i], offspring[j] = offspring[j], offspring[i]

        next_generation.append(offspring)
    population = next_generation

# Evaluate final generation to find the best solution
final_evaluation = [(evaluate(tour), tour) for tour in population]
final_evaluation.sort()  # sort by max distance minimally
best_max_distance, best_tour = final_evaluation[0]

# Total distance calculation
total_travel_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))

print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", best_max_distance)