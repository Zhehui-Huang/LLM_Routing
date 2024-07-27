import random
import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of the cities, including the depot
cities_dict = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
    14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Select 16 cities including the depot city (0)
cities_index = list(cities_dict.keys())  # All possible cities
selected_cities = cities_index[:16]     # Selection of first 16 cities for simplicity

# Calculate distances matrix
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances([cities_dict[city] for city in selected_cities])

# Implementing Genetic Algorithm
def create_route():
    route = selected_cities[:]
    random.shuffle(route)
    return route

def initial_population(pop_size, num_cities):
    return [create_route() for _ in range(pop_size)]

def route_distance(route):
    return sum(distances[route[i]][route[i+1]] for i in range(-1, len(route)-1))

def rank_routes(population):
    fitness_results = [(index, route_distance(route)) for index, route in enumerate(population)]
    return sorted(fitness_results, key=lambda x: x[1])

def selection(ranked_pop, elite_size):
    selection_results = [ranked_pop[i][0] for i in range(elite_size)]
    total_distance = sum((1/(rank[1]+1) for rank in ranked_pop))
    prob = list((1/(rank[1]+1) / total_body for rank in ranked_pop))
    picked_indices = np.random.choice(a=[i for i in range(len(ranked_pop))], size=len(ranked_pop)-elite_size, p=prob)
    selection_results.extend(picked_indices)
    return selection_results

def mating_pool(population, selection_indices):
    return [population[i] for i in selection_indices]

def breed(parent1, parent2):
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    start_gene, end_gene = min(geneA, geneB), max(geneA, geneB)
    child = parent1[start_gene:end_gene]
    child.extend([item for item in parent2 if item not in child])
    return child

def breed_population(mating_pool, elite_size):
    children = mating_pool[:elite_size]
    pool_size = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))
    for i in range(pool_size):
        child = breed(pool[i], pool[len(mating_pool)-i-1])
        children.append(child)
    return children

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]
    return individual

def mutate_population(population, mutation_rate):
    return [mutate(individual, mutation_rate) for individual in population]

def next_generation(current_gen, elite_size, mutation_rate):
    rank_pop = rank_routes(current_gen)
    select_indices = selection(rank_pop, elite_size)
    matingpool = mating_pool(current_gen, select_indices)
    children = breed_population(matingpool, elite_size)
    return mutate_population(children, mutation_rate)

def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, len(population))
    for i in range(generations):
        pop = next_generation(pop, elite_size, mutation_rate)
    return rank_routes(pop)[0]

# Parameters
pop_size = 100
elite_size = 20
mutation_rate = 0.01
generations = 500

best_route_index, best_route_distance = genetic_algorithm(selected_cities, pop_size, elite_size, mutation_rate, generations)
best_route = [selected_cities[i] for i in best_route_index]

# Output the results
print("Tour:", best_route + [best_route[0]])
print("Total travel cost:", best_route_distance)