import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Parameters
num_robots = 4

# Helper function to calculate the distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

# Genetic algorithm parts
def create_initial_population(num_inds, num_cities, num_robots):
    population = []
    for _ in range(num_inds):
        ind = list(range(1, num_cities))
        random.shuffle(ind)
        split_points = sorted(random.sample(range(1, num_cities - 1), num_robots - 1))
        routes = [ind[:split_points[0]]] + [ind[split_points[i]:split_points[i+1]] for i in range(num_robots - 2)] + [ind[split_points[-1]:]]
        population.append(routes)
    return population

def fitness(individual, distance_matrix):
    total_cost = 0
    for route in individual:
        route_cost = distance_matrix[0][route[0]]  # From depot to first city
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i+1]]
        route_cost += distance_matrix[route[-1]][0]  # From last city back to depot
        total_cost += route_cost
    return total_cost

def select_parents(population, fitnesses, num_parents):
    selected_indices = np.argsort(fitnesses)[:num_parents]
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    # Implement a suitable crossover method, e.g., order crossover
    return child1, child2

def mutate(individual):
    # Implement mutation, e.g., swapping two cities
    pass

# Hyperparameters
num_individuals = 100
num_generations = 300  # This might need adjustments based on the problem size and complexity

# Initialize genetic algorithm
distance_matrix = calculate_distance_matrix(cities)
population = create_initial_population(num_individuals, len(cities), num_robots)

# Genetic Algorithm Execution
for generation in range(num_generations):
    fitnesses = [fitness(ind, distance_matrix) for ind in population]
    parents = select_parents(population, fitnesses, num_individuals // 2)
    next_generation = parents[:]
    while len(next_generation) < num_individuals:
        p1, p2 = random.sample(parents, 2)
        offspring = crossover(p1, p2)
        for child in offspring:
            mutate(child)
            next_generation.append(child)
    population = next_generation

# Compute result
best_individual = min(population, key=lambda ind: fitness(ind, distance_matrix))
best_fitness = fitness(best_individual, distance_matrix)

# Print tours
total_cost = 0
for i, tour in enumerate(best_individual):
    tour_complete = [0] + tour + [0]
    tour_cost = fitness([tour], distance_matrix)
    total_cost += tour_cost
    print(f'Robot {i} Tour: {tour_complete}')
    print(f'Robot {i} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {total_cost}')