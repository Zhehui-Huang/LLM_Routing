import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Euclidean distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Genetic Algorithm Functions
def create_route():
    non_depot_cities = list(cities.keys())[1:]
    random.shuffle(non_depot_cities)
    return non_depot_cities

def initial_population(pop_size, num_cities):
    return [create_route() for _ in range(pop_size)]

def calculate_fitness(route):
    total_distance = 0
    total_distance += distance(0, route[0])  # from depot to first city
    for i in range(1, len(route)):
        total_distance += distance(route[i-1], route[i])
    total_distance += distance(route[-1], 0)  # from last city back to depot
    return total_distance

def rank_routes(population):
    fitness_results = {i: calculate_fitness(population[i]) for i in range(len(population))}
    return sorted(fitness_results.items(), key=lambda x: x[1])

# Genetic Algorithm Core Parts
def select_parents(ranked_pop, elite_size):
    selection_results = [ranked_pop[i][0] for i in range(elite_size)]
    return [population[idx] for idx in selection_results]

def crossover(parent1, parent2):
    child = []
    geneA, geneB = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[geneA:geneB]
    child = [item for item in parent2 if item not in child] + child
    return child

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swapWith = int(random.random() * len(individual))
            individual[swapped], individual[swapWith] = individual[swapWith], individual[swapped]
    return individual

def next_generation(current_gen, elite_size, mutation_rate):
    ranked_population = rank_routes(current_gen)
    parents = select_parents(ranked_population, elite_size)
    children = [crossover(parents[i], parents[(i + 1) % len(parents)]) for i in range(len(parents))]
    next_gen = [mutate(child, mutation_rate) for child in children]
    return next_gen

# Main genetic algorithm
def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = initial_population(pop_size, len(cities)-1)
    print("Initial shortest distance: " + str(rank_routes(pop)[0][1]))
    
    for i in range(generations):
        pop = next_generation(pop, elite_size, mutation_rate)
    
    print("Final shortest distance: " + str(rank_routes(pop)[0][1]))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_sr])
    return best_route

# Parameters
pop_size = 100
elite_size = 20
mutation_rate = 0.01
generations = 500

# Run genetic algorithm
best_route = genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations)

# Divide route among 2 robots
route_robot_0 = [0] + best_route[:len(best_route)//2] + [0]
route_robot_1 = [0] + best_route[len(best_route)//2:] + [0]

# Calculate travel cost
def get_travel_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distance(route[i-1], route[i])
    return cost

cost_robot_0 = get_travel_cost(route_robot_0)
cost_robot_1 = get_travel_cost(route_robot_1)
overall_total_cost = cost_robot_0 + cost_robot_1

# Output
print("Robot 0 Tour:", route_robot_0)
print("Robot 0 Total Travel Cost:", cost_robot_0)
print("Robot 1 Tour:", route_robot_1)
print("Robot 1 Total Travel Cost:", cost_robot_1)
print("Overall Total Travel Cost:", overall_total_cost)