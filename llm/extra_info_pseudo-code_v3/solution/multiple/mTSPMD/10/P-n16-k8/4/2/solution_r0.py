import numpy as np
import random

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Each robot starts and ends at its own depot
depot_indices = list(range(8))  # 8 depots, each corresponding to a robot

# Calculate Euclidean distance between any two cities
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Genetic Algorithm Parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Chromosome: each city once (except depots) + a mapping of cities to depots
def create_chromosome():
    non_depot_cities = list(set(range(len(cities))) - set(depot_indices))
    random.shuffle(non_depot_cities)
    depot_map = random.choices(depot_indices, k=len(non_depot_cities))
    return non_depot_cities + depot_map

def decode_chromosome(chromosome):
    non_depot_cities = chromosome[:len(cities)-len(depot_indices)]
    depot_map = chromosome[len(cities)-len(depot_indices):]
    routes = [[] for _ in depot_indices]
    for city, depot in zip(non_depot_cities, depot_map):
        routes[depot].append(city)
    for i, route in enumerate(routes):
        routes[i] = [i] + route + [i]
    return routes

def calculate_cost(routes):
    total_cost = 0
    cost_details = []
    for route in routes:
        cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1))
        total_cost += cost
        cost_details.append((route, cost))
    return total_cost, cost_details

def fitness(chromosome):
    routes = decode_chromosome(chromosome)
    total_cost, _ = calculate_cost(routes)
    return -total_cost  # Negative because we want to minimize total cost

def select(population, scores, k=3):
    selection_ix = np.random.randint(len(population))
    for ix in np.random.randint(0, len(population), k-1):
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

def crossover(p1, p2):
    # Cutting point
    cut = random.randint(0, len(p1)-1)
    child = list(p1[:cut]) + list(p2[cut:])
    return child

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            swap_ix = random.randint(0, len(chromosome)-1)
            chromosome[i], chromosome[swap_ix] = chromosome[swap_ix], chromosome[i]

# Genetic Algorithm
population = [create_chromosome() for _ in range(population_size)]
best, best_eval = 0, fitness(population[0])

for gen in range(generations):
    # Evaluate all candidates in the population
    scores = [fitness(c) for c in population]
    for i, score in enumerate(scores):
        if score > best_eval:
            best, best_eval = population[i], score
            print(">%d, new best f(%s) = %.3f" % (gen, population[i], score))

    # Select parents
    selected = [select(population, scores) for _ in range(pop_pop)]
    children = list()
    for i in range(0, len(selected), 2):
        p1, p2 = selected[i], selected[i+1]
        for c in crossover(p1, p2):
            mutate(c, mutation_rate)
            children.append(c)
    population = children

# Best solution
best_routes = decode_chromosome(best)
best_cost, cost_details = calculate_cost(best_routes)
for i, detail in enumerate(cost_details):
    route, cost = detail
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")