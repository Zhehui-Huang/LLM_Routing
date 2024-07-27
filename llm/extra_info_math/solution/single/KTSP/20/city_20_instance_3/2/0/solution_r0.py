import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

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

# Distance function
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Greedy algorithm to choose 12 additional cities considering distribution
def select_cities(base_city, num_cities, total_cities):
    selected_cities = [base_city]
    while len(selected_cities) < num_cities:
        last_city = selected_cities[-1]
        next_city = min(set(total_cities) - set(selected_cities), key=lambda x: calc_distance(last_city, x))
        selected_cities.append(next_city)
    return selected_cities

# Genetic algorithm helper functions
def create_route(city_list):
    """ Creates a random route """
    route = random.sample(city_list, len(city_list))
    return route

def initial_population(pop_size, city_list):
    """ Randomly initialize population (routes) """
    return [create_route(city_list) for _ in range(pop_size)]

def rank_routes(population):
    """ Rank routes by their distance """
    fitness_results = {}
    for i, route in enumerate(population):
        fitness_results[i] = sum(calc_distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    return sorted(fitness_results.items(), key=lambda x: x[1])

def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)
    for i in range(generations):
        ranked_pop = rank_routes(pop)
        selected_indices = [index for index, _ in ranked_pop[:elite_size]]
        elite_pop = [pop[index] for index in selected_indices]
        # Usually involves crossover function, but keeping it simple for now, just evolving elitemost routes
        for _ in range(len(pop) - elite_size):
            random_elite = random.choice(elite_pop)
            elite_pop.append(random_elite)
        # Mutation
        pop = [mutate(route, mutation_rate) for route in elite_pop]
    return rank_routes(pop)[0]

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            swap_index = random.randint(0, len(route) - 1)
            route[i], route[swap_index] = route[swap_index], route[i]
    return route

# Select 13 cities including depot city 0 
selected_cities = select_cities(0, 13, list(cities.keys()))

# Solve TSP using genetic algorithm
result_route_index, result_distance = genetic_algorithm(selected_cities, pop_size=100, elite_size=20, mutation_rate=0.02, generations=500)

# Display result
result_route = [selected_cities[i] for i in result_route_index]
print(f'Tour: {result_route}')
print(f'Total travel cost: {result_distance}')