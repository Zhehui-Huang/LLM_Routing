import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# City coordinates including the depot
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots/vehicles
num_robots = 4

def calculate_distance(matrix, tour):
    return sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_population(n_cities, n_robots, population_size):
    population = []
    for _ in range(population_size):
        tour = np.random.permutation(n_cities - 1) + 1
        splits = sorted(np.random.choice(range(1, n_cities - 1), n_robots - 1, replace=False))
        robot_tours = np.split(tour, splits)
        population.append(robot_tours)
    return population

def fitness(matrix, robot_tours):
    return sum(calculate_distance(matrix, np.hstack([0, tour, 0])) for tour in robot_tours)

def selection(population, matrix, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    fitness_scores = [fitness(matrix, indiv) for indiv in tournament]
    return tournament[np.argmin(fitness_scores)]

def crossover(parent1, parent2):
    child = []
    for tours1, tours2 in zip(parent1, parent2):
        if random.random() > 0.5:
            child.append(tours1)
        else:
            child.append(tours2)
    return child

def mutation(individual, mutation_rate=0.1):
    for tour in individual:
        if random.random() < mutation_rate:
            i, j = np.random.choice(len(tour), 2, replace=False)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(matrix, n_cities, n_robots, generations=1000, population_size=100):
    population = generate_initial_population(n_cities, n_robots, population_size)
    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = selection(population, matrix)
            parent2 = selection(population, matrix)
            child = crossover(parent1, parent2)
            mutation(child)
            new_population.append(child)
        population = new_population
    best_solution = min(population, key=lambda x: fitness(matrix, x))
    return best_solution

# Compute distance matrix
n_cities = len(coords)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean(coords[i], coords[j])

# Solve the problem using a genetic algorithm
solution = genetic_algorithm(distance_matrix, n_cities, num_robots)

# Calculate costs and print results
total_cost = 0
for i, tour in enumerate(solution):
    tour_cost = calculate_distance(distance_matrix, np.hstack([0, tour, 0]))
    total_cost += tour_cost
    print(f"Robot {i} Tour: {np.hstack([0, tour, 0])}")
    print(f"Robot {i} Total Travel Cost: {tour_option[i]}")
print(f"Overall Total Travel Cost: {total_coption}")