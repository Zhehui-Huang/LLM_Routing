import numpy as np
import random
from math import sqrt

# City coordinates (index 0 is the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Genetic algorithm parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Helper function: Total distance of the robots' tours
def calculate_total_distance(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost

# Generate initial random population
def generate_initial_population():
    population = []
    for _ in range(population_size):
        # Create a list of cities excluding the depot
        cities = list(range(1, num_cities))
        random.shuffle(cities)

        # Split cities for each robot roughly equally
        tours = [[] for _ in range(num_robots)]
        slice_size = len(cities) // num_robots
        for i in range(num_robots):
            start_index = i * slice_size
            if i == num_robots - 1:
                tours[i] = [0] + cities[start_index:] + [0]
            else:
                end_index = start_index + slice_size
                tours[i] = [0] + cities[start_index:end_index] + [0]
        
        population.append(tours)
    return population

# Selection function utilizing tournament selection
def tournament_selection(population, k=4):
    best = None
    for i in range(k):
        indiv = random.choice(population)
        if best is None or calculate_total_distance(indiv) < calculate_total_distance(best):
            best = indiv
    return best

# Crossover - Order crossover
def crossover(parent1, parent2):
    # Implementing a simple one-point crossover for tours
    child1, child2 = [], []
    crossover_point = random.randint(1, num_cities - 2)  # Avoid the first city (depot)
    for i in range(num_robots):
        child1.append(parent1[i][:crossover_point] + parent2[i][crossover_point:])
        child2.append(parent2[i][:crossover_point] + parent1[i][crossover_point:])
    return [child1, child2]

# Mutation - Swap mutation
def mutate(tour):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            swap_index = random.randint(1, len(tour[i]) - 2)  # Avoid swapping the depot
            city1, city2 = random.randint(1, len(tour[i]) - 2), random.randint(1, len(tour[i]) - 2)
            tour[i][city1], tour[i][city2] = tour[i][city2], tour[i][city1]
    return tour

# Run genetic algorithm
population = generate_initial_population()
for generation in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        offspring = crossover(parent1, parent2)
        new_population.extend(offspring)
        
    population = [mutate(indiv) for indiv in new_population]

# Compute final solution and costs
best_solution = min(population, key=calculate_total_distance)
best_solution_cost = calculate_total_distance(best_solution)

for i, tour in enumerate(best_solution):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {best_solution_cost}")