import numpy as np
import random

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Calculate Euclidean distance between any two cities
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Genetic Algorithm Parameters
population_size = 200
generations = 200
mutation_rate = 0.03

# Create chromosome: sequence of non-depot city indices
def create_chromosome():
    non_depot_cities = list(range(8, len(cities)))  # city indices from 8 to 15
    random.shuffle(non_depot_cities)
    return non_depot_cities

# Decode chromosome to assign cities to nearest depots
def decode_chromosome(chromosome):
    routes = {i: [i] for i in range(8)}  # Start from each depot
    for city in chromosome:
        # Assign city to nearest depot
        nearest_depot = min(range(8), key=lambda d: distance_matrix[d, city])
        routes[nearest_depot].append(city)
    for i in range(8):
        routes[i].append(i)  # End at each depot
    return list(routes.values())

def calculate_total_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route) - 1))
        total_cost += route_cost
        costs.append(route_cost)
    return total_cost, costs

def fitness(chromosome):
    routes = decode_chromosome(chromosome)
    total_cost, _ = calculate_total_cost(routes)
    return -total_cost  # Negative because we minimize cost

def select(population, scores):
    # Tournament selection
    tournament_size = 3
    selected = []
    for _ in range(len(population)):
        competitors = random.sample(list(zip(population, scores)), tournament_size)
        selected.append(min(competitors, key=lambda x: x[1])[0])
    return selected

def crossover(parent1, parent2):
    # Order crossover
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    fill_index = end
    for gene in parent2:
        if gene not in child:
            if fill_index >= size:
                fill_index = 0
            while child[fill_index] is not None:
                fill_index += 1
            child[fill_index] = gene
    return child

def mutate(chromosome):
    # Swap mutation
    idx1, idx2 = random.sample(range(len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

# Initialize population
population = [create_chromosome() for _ in range(population_size)]
best = None
best_score = float('inf')

for generation in range(generations):
    # Evaluate fitness
    scores = [fitness(individual) for individual in population]
    # Best in current generation
    current_best = population[np.argmin(scores)]
    current_best_score = min(scores)
    
    if current_best_score < best_score:
        best, best_score = current_sid, current_best_score
        print(f"Generation {generation}: Best score = {-best_score}")
    
    # Selection
    selected = select(population, scores)
    # Crossover and mutation
    children = []
    for i in range(0, len(selected), 2):
        parent1, parent2 = selected[i], selected[i+1]
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        children.extend([child1, child2])
    population = children

# Decode and display final best solution
best_routes = decode_chromosome(best)
total_cost, individual_costs = calculate_total_cost(best_routes)
for i, route in enumerate(best_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")
print(f"Overall Total Travel Cost: {total_cost}")