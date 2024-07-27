import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates (including depots)
coordinates = [
    (30, 40), (37, 52),
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and their depots
num_robots = 2
depot_indices = [0, 1]

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(coord):
    n = len(coord)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean(coord[i], coord[j])
            else:
                distance_matrix[i][j] = float('inf')  # Avoid self-loop
    return distance_matrix

distances = calculate_distances(coordinates)

# Genetic Algorithm parameters
population_size = 50
num_generations = 500
mutation_rate = 0.1
crossover_rate = 0.8

# Helper functions for GA
def create_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        tour = random.sample(range(2, num_cities), num_cities - 2)  # Excluding depots
        population.append(tour)
    return population

def evaluate_fitness(tour):
    # Split tour between two robots based on a random cut-point
    cut_point = random.randint(1, len(tour) - 1)
    robot_tours = [tour[:cut_point], tour[cut_point:]]
    robot_tours[0] = [depot_indices[0]] + robot_tours[0] + [depot_indices[0]]
    robot_tours[1] = [depot_indices[1]] + robot_tours[1] + [depot_indices[1]]
    total_cost = 0
    for r_tour in robot_tours:
        for i in range(len(r_tour)-1):
            total_cost += distances[r_tour[i]][r_tour[i+1]]
    return total_cost, robot_tours

def select_parents(population, fitness_values):
    return random.choices(population, weights=inverse_fitness_scores(fitness_values), k=2)

def inverse_fitness_scores(fitness_values):
    max_fitness = max(fitness_values)
    return [max_fitness - f for f in fitness_values]

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        # Implement ordered crossover (OX)
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None]*len(parent1)
        child[start:end+1] = parent1[start:end+1]
        filt_parent2 = [item for item in parent2 if item not in parent1[start:end+1]]
        child = filt_parent2[:start] + child[start:end+1] + filt_parent2[start:]
        return child
    return parent1

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Initialize population
num_cities = len(coordinates)
population = create_initial_population(population_size, num_cities)

# Run GA
for generation in range(num_generations):
    # Evaluate population
    fitness_scores = []
    evaluated_pop = []
    for indiv in population:
        fitness, tours = evaluate_fitness(indiv)
        fitness_scores.append(fitness)
        evaluated_pop.append(tours)

    # Select new population
    new_population = []
    for _ in range(population_size//2):
        p1, p2 = select_parents(population, fitness_scores)
        child1 = crossover(p1, p2)
        child2 = crossover(p2, p1)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = new_population[:population_size]

# Get the best solution
best_index = np.argmin(fitness_scores)

# Output results
print("Robot 0 Tour:", evaluated_pop[best_index][0][0])
print("Robot 0 Total Travel Cost:", sum(distances[evaluated_pop[best_index][0][i]][evaluated_pop[best_index][0][i+1]] for i in range(len(evaluated_pop[best_index][0])-1)))
print("Robot 1 Tour:", evaluated_pop[best_index][0][1])
print("Robot 1 Total Travel Cost:", sum(distances[evaluated_pop[best_index][0][1][i]][evaluated_pop[best_evaluated_index][0][1][i+1]] for i in range(len(evaluated_pop[best_index][0][1])-1)))
print("Overall Total Travel Cost:", fitness_scores[best_index])