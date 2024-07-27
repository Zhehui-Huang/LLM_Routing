import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i, j] = euclidean(cities[i], cities[j])
    return distance_matrix

# Genetic Algorithm Part
def initial_population(city_list, pop_size):
    return [random.sample(city_list, len(city_list)) for _ in range(pop_size)]

def calculate_total_distance(route, distance_matrix):
    return sum(distance_μATRIX[route[i], route[i + 1]] for i in range(len(route) - 1)) + distance_matrix[route[-1], route[0]]

def rank_population(population, distance_matrix):
    fitness_scores = [(route, calculate_total_distance(route, distance_matrix)) for route in population]
    return sorted(fitness_scores, key=lambda x: x[1])

def select_mating_pool(ranked_pop, elite_size):
    return [ranked_pop[i][0] for i in range(elite_size)]

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    childP1 = [parent1[i] for i in range(start_gene, end_gene)]
    childP2 = [item for item in parent2 if item not in childP1]
    
    child = childP1 + childP2
    return child

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]
    return individual

def genetic_algorithm(distance_matrix, city_list, pop_size, elite_size, mutation_rate, generations):
    population = initial_population(city_list, pop_size)
    for i in range(generations):
        ranked_pop = rank_population(population, distance_matrix)
        mating_pool = select_mating_pool(ranked_pop, elite_size)
        children = [breed(mating_pool[i], mating_pool[(i+1) % elite_size]) for i in range(len(mating_pool))]
        next_generation = [mutate(individual, mutation_rate) for individual in children]
        population = next_generation
    
    best_route = rank_population(population, distance_matrix)[0]
    return best_route

# Select 13 cities including depot city 0 and run the GA
selected_cities = [0] + random.sample(list(cities.keys())[1:], 12)
distance_matrix = create_distance_matrix([cities[idx] for idx in sorted(cities)])

best_route_info = genetic_algorithm(distance_matrix, selected_cities, pop_size=100, elite_size=20, mutation_rate=0.01, generations=500)
best_route_indices = best_route_info[0]
best_route_cost = best_route_info[1]

print(f"Tour: {[selected_cities[i] for i in best_route_indices] + [selected_cities[best_route_indices[0]]]}")
print(f"Total travel cost: {best_route_cost}")