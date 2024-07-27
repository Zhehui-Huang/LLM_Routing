import numpy as np
from scipy.spatial.distance import euclidean
import random

# Coordinates of all cities including the depot
cities_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
    14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Select 15 cities randomly plus the depot city 0
selected_indices = np.random.choice(list(cities_coordinates.keys()), size=15, replace=False)
selected_indices = np.append(selected_indices, 0) if 0 not in selected_indices else selected_indices

# Calculate the Euclidean distances between each pair of selected cities
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            city_i = cities_coordinates[cities[i]]
            city_j = cities_coordinates[cities[j]]
            dist_matrix[i][j] = np.sqrt((city_i[0] - city_j[0])**2 + (city_i[1] - city_j[1])**2)
    return dist_matrix

distances = calculate_distances(selected_indices)

# Genetic Algorithm helper functions
def create_route(city_indices):
    route = city_indices.copy()
    np.random.shuffle(route)
    return route

def initial_population(pop_size, city_indices):
    return [create_route(city_indices) for _ in range(pop_temp_size)]

def route_distance(route):
    return sum(distances[route[i], route[(i+1) % len(route)]] for i in range(len(route)))

def rank_routes(population):
    fitness_results = [(i, route_distance(route)) for i, route in enumerate(population)]
    return sorted(fitness_results, key=lambda x: x[1])

def select_mating_pool(population, ranked_routes, elite_size):
    mating_pool = []
    for i in range(elite_size):
        mating_pool.append(population[ranked_routes[i][0]])
    remaining_chances = [weight for _, weight in ranked_routes[elite_size:]]
    probabilities = [weight / sum(remaining_chances) for weight in remaining_chances]
    chosen_indices = np.random.choice(a=list(range(elite_size, len(population))), size=len(population)-elite_size, p=probabilities, replace=False)
    for i in chosen_indices:
        mating_pool.append(population[ranked_routes[i][0]])
    return mating_pool

def breed(parent1, parent2):
    child = []
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    for i in range(start_gene, end_gene):
        child.append(parent1[i])

    child.extend([item for item in parent2 if item not in child])
    return child

def breed_population(mating_pool, elite_size):
    children = []
    length = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(elite_size):
        children.append(mating_pool[i])
    
    for i in range(length):
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
    mutated_pop = []
    for ind in population:
        mutated_ind = mutate(ind, mutation_rate)
        mutated_pop.append(mutated_ind)
    return mutated_pop

def next_generation(current_gen, elite_size, mutation_rate):
    ranked_routes = rank_routes(current_gen)
    mating_pool = select_mate_pool(current_gen, ranked_routes, elite_size)
    children = breed_pop(mating_pool, elite_size)
    next_generation = mutate_pop(children, mutation_rate)
    return next_generation

# Running the genetic algorithm
population_size = 100
elite_size = 20
mutation_rate = 0.01
generations = 500

population = initial_population(population_size, list(selected_indices))
for i in range(generations):
    population = next_generation(population, elite_size, mutation_rate)

best_route_index, best_route_distance = rank_routes(population)[0]
best_route = population[best_route_index]

print("Tour:", [selected_indices[i] for i in best_route] + [selected_indices[best_route[0]]])
print("Total travel cost:", best_route_distance)