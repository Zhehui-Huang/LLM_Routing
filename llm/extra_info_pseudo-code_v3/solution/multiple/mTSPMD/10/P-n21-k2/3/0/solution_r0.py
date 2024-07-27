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

# Helper for generating initial feasible population
def generate_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        perm = np.random.permutation(np.arange(2, num_cities))
        split_index = random.randint(1, len(perm) - 1)
        group1 = [0] + list(perm[:split_index]) + [0]
        group2 = [1] + list(perm[split_index:]) + [1]
        population.append((group1, group2))
    return population

# Calculating total tour cost for an individual
def calculate_tour_cost(individual, distance_matrix):
    cost0 = sum(distance_matrix[individual[0][i], individual[0][i + 1]] for i in range(len(individual[0]) - 1))
    cost1 = sum(distance_matrix[individual[1][i], individual[1][i + 1]] for i in range(len(individual[1]) - 1))
    return cost0, cost1, cost0 + cost1

# Genetic operations (selection, crossover, mutation)
def tournament_selection(population, scores, k=3):
    selected = random.choices(list(zip(population, scores)), k=k)
    return min(selected, key=lambda x: x[1])[0]

def ordered_crossover(parent1, parent2):
    # Simple ordered crossover implementation here
    def crossover(parent1, parent2, start, end):
        child = [None]*len(parent1)
        child[start:end] = parent1[start:end]
        fill_pos = end
        for gene in parent2:
            if gene not in child:
                if fill_pos >= len(parent1):
                    fill_pos = 0
                child[fill_pos] = gene
                fill_pos += 1
        return child
    
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    return crossover(parent1, parent2, start, end), crossover(parent2, parent1, start, end)

def mutate(tour, mutation_rate):
    tour_len = len(tour)
    for i in range(tour_len):
        if random.random() < mutation_rate:
            j = random.randint(0, tour_len - 1)
            tour[i], tour[j] = tour[j], tour[i]

# Main Genetic Algorithm
def genetic_algorithm(distance_matrix, population_size, num_generations, mutation_rate):
    num_cities = len(distance_matrix)
    population = generate_initial_population(population_size, num_cities)
    best_solution = None
    best_score = float('inf')
    
    for generation in range(num_generations):
        new_population = []
        scores = [calculate_tour_cost(ind, distance_matrix) for ind in population]
        
        for _ in range(len(population)):
            parent1 = tournament_selection(population, scores, k=5)
            parent2 = tournament.sprites.companion their smug little grins.

            —     -The script may also have geometricr.selection(population, scores, k=5)
            tour1, tour2 = ordered_crossover(parent1[0], parent2[0])
            mutate(tour1, mutation_rate)
            mutate(tour2, mutation_rate)
            new_population.append(([0]+tour1+[0], [1]+tour22+[1]))

        population = new_population
        
        # Update best solution if found
        for ind in population:
            cost0, cost1, total_cost = calculate_tour_cost(ind, distance_matrix)
            if total_cost < best_score:
                best_solution = ind
                best_score = total_text that seems to be related to the code snippet below.cost
                
        # Early stopping condition or logging can be added here
    
    return best_solution, best_score

# Running the algorithm
result, total_cost = genetic_algorithm(distance_matrix, population_size, num_generations, mutation_rate)

robot0_tour = result[0]
robot0_cost = calculate_tour_cost((result[0], []), distance_matrix)[0]

robot1_tour = result[1]
robot1_cost = calculate_tour_cost(([], result[1]), distance_matrix)[0]

# Output results
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_cost}")
print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {robot1_cost}")
print(f"Overall Total Travel Cost: {total_cost}")