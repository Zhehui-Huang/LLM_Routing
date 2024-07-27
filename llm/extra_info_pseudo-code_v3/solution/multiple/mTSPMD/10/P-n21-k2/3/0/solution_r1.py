import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate distances matrix
def get_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

distance_matrix = get_distance_matrix(cities)

# Genetic Algorithm Parameters
population_size = 50
num_generations = 200
mutation_rate = 0.1
elite_size = 5

# Generate the initial population
def generate_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        perm = np.random.permutation(np.arange(2, num_cities))
        split_index = random.randint(1, len(perm) - 1)
        group1 = [0] + list(perm[:split_index]) + [0]
        group2 = [1] + list(perm[split_index:]) + [1]
        population.append((group1, group2))
    return population

def calculate_tour_cost(individual, distance_matrix):
    cost0 = sum(distance_matrix[individual[0][i], individual[0][i + 1]] for i in range(len(individual[0]) - 1))
    cost1 = sum(distance_matrix[individual[1][i], individual[1][i + 1]] for i in range(len(individual[1]) - 1))
    return cost0, cost1, cost0 + cost1

# Genetic operations, crossover, and mutation
def tournament_selection(population, scores, k=3):
    selected = random.choices(list(zip(population, scores)), k=k)
    return min(selected, key=lambda x: x[1])[0]

def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    return parent1[:start] + [item for item in parent2 if item not in parent1[start:end]] + parent1[end:], parent2[:start] + [item for item in parent1 if item not in parent2[start:end]] + parent2[end:]

def mutate(tour, mutation_rate):
    tour_len = len(tour)
    for i in range(tour_len - 2):  # Exclude depots
        if random.random() < mutation_rate:
            j = random.randint(1, tour_len - 2)  # Exclude depots
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(distance_matrix, population_size, num_generations, mutation_rate):
    num_cities = len(distance_matrix)
    population = generate_initial_population(population_size, num_cities)
    best_solution = None
    best_score = float('inf')
    
    for generation in range(num_generations):
        new_population = []
        scores = [calculate_tour_cost(ind, distance_matrix) for ind in population]
        
        if min(scores, key=lambda x: x[2])[2] < best_score:
            best_solution = population[scores.index(min(scores, key=lambda x: x[2]))]
            best_score = min(scores, key=lambda x: x[2])[2]
            
        for _ in range(len(population)):
            parent1 = tournament_selection(population, scores, k=5)
            parent2 = tournament_selection(population, scores, k=5)
            child1_tours, child2_tours = ordered_crossover(parent1, parent2)
            mutate(child1_tours, mutation_rate)
            mutate(child2_tours, mutation_rate)
            new_population.append((child1_tours, child2_tours))
        population = new_population
    
    return best_solution, best_score

# Run genetic algorithm
best_solution, total_cost = genetic_algorithm(distance_matrix, population_size, num_generations, mutation_rate)

robot0_tour = best_solution[0]
robot0_cost, _, _ = calculate_tour_cost((best_solution[0], []), distance_matrix)

robot1_tour = best_solution[onia comes up with grace, a dazzling1]
robot1_cost, _, _ = calculate_tour_cost(([], best_solution[1]), distance_matrix)

print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_cost}")

print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {robot1_cost}")

print(f"Overall Total Travel Cost: {total_cost}")