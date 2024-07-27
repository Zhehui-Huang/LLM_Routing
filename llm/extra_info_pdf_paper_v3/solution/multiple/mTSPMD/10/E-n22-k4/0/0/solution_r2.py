import numpy as np
import random
from math import sqrt
from copy import deepcopy

# Define city and depot locations
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]

# Calculate distance matrix
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

dist_matrix = np.array([[calc_distance(i, j) for j in cities] for i in cities])

# Genetic Algorithm Settings
population_size = 50
num_generations = 1000
mutation_rate = 0.15

# Genetic Algorithm Implementation
def initialize_population():
    non_depot_cities = set(cities.keys()) - set(depots)
    population = []
    for _ in range(population_size):
        genome = list(non_depot_cities)
        random.shuffle(genome)
        population.append(genome)
    return population

def evaluate_fitness(genome):
    split = np.array_split(genome, len(depots))
    tours = [0] * len(depots)
    total_cost = 0
    for idx, depot in enumerate(depots):
        tour = [depot] + list(split[idx]) + [depot]
        tours[idx] = tour
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost, tours

def tournament_selection(population, scores, k=3):
    selection_idx = np.random.randint(len(population), size=k)
    best_idx = selection_idx[np.argmin(scores[selection_idx])]
    return deepcopy(population[best_idx])

def ordered_crossover(parent1, parent2):
    child = [None]*len(parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child[start:end+1] = parent1[start:end+1]
    filled = set(parent1[start:end+1])
    position = 0
    for item in parent2:
        if item not in filled:
            while child[position] is not None:
                position += 1
            child[position] = item
    return child

def mutate(genome, mutation_rate):
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(genome) - 1)
            genome[i], genome[j] = genome[j], genome[i]

population = initialize_population()
best_solution = None
best_score = float("inf")

for generation in range(num_generations):
    scores = np.array([evaluate_fitness(g)[0] for g in population])
    best_idx = np.argmin(scores)
    if scores[best_idx] < best_score:
        best_score = scores[best_idx]
        best_solution = population[best_idx]
    
    next_population = [tournament_selection(population, scores) for _ in range(population_size)]
    population = [mutate(ordered_crossover(next_population[i], next_population[(i+1)%population_size]), mutation_rate) for i in range(population_size)]

# Output the best solution found
total_cost, robot_tours = evaluate_fitness(best_solution)
print(f"Overall Total Travel Cost: {total_cost}")
for idx, tour in enumerate(robot_tours):
    print(f"Robot {idx+1} Tour: {tour}")
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {idx+1} Total Travel Cost: {tour_cost}")