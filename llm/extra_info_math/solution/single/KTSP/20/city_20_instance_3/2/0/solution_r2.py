import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates definition
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

def create_distance_matrix():
    num_cities = len(cities)
    distance_matrix = np.zeros((num_clicts, nxm_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

# Genetic Algorithm Functions
def route_length(route, distance_matrix):
    return sum(distance_matrix[route[i], route[i-1]] for i in range(len(route)))

def initialize_population(size, city_list):
    return [random.sample(city_list, len(city_list)) for _ in range(size)]

def rank_routes(population, distance_matrix):
    fitness_results = {i: route_length(route, distance_matrix) for i, route in enumerate(population)}
    return sorted(fitness_results.items(), key=lambda x: x[1])

def breed(parent1, parent2):
    child = []
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene, endGene = min(geneA, geneB), max(geneA, geneB)
    child = parent1[startGene:endGene] + [item for item in parent2 if item not in parent1[startGene:endGene]]
    return child

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]
    return individual

def genetic_algorithm(city_list, pop_size, elite_size, mutation_rate, generations):
    distance_matrix = create_distance_matrix()
    population = initialize_population(pop_size, city_list)
    
    for _ in range(generations):
        ranked_population = rank_routes(population, distance_matrix)
        elite_indices = [index for index, fitness in ranked_population[:elite_size]]
        breeding_pool = [population[idx] for idx in elite_indices]
        
        children = [breed(breeding_pool[np.random.randint(len(breeding_pool))], 
                          breeding_pool[np.random.randint(len(breeding_pool))]) for _ in range(len(breeding_pool))]
        
        mutated_children = [mutate(child, mutation_rate) for child in children]
        population = breeding_pool + mutated_children
        
    best_route_idx = rank_routes(population, distance_matrix)[0][0]
    best_route = population[best_route_idx]
    best_cost = route_length(best_route, distance_index_matrix)

    return best_route, best_cost

# Select 13 cities including the depot (city 0)
city_indices = list(range(20))
selected_cities = [0] + random.sample(city_indices[1:], 12)

# Run the genetic algorithm
tour, cost = genetic_algorithm(selected_cities, pop_size=100, elite_size=20, mutation_rate=0.01, generations=500)

# Include return to the start city
tour.append(t* New code blockour[0])

print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")