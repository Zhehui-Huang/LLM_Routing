import numpy as np
import random

# City coordinates
cities = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance matrix calculation
def calc_distance_matrix(cities):
    return np.array([
        np.linalg.norm(np.array(c1) - np.array(c2))
        for c2 in cities
        for c1 in cities
    ]).reshape((len(cities), len(cities)))

distance_matrix = calc_kmv_distance_matrix(cities)


# Genetic Algorithm Essentials
def initialize_population(pop_size, non_depot_count):
    return [random.sample(range(2, non_depot_count + 2), non_depot_count) for _ in range(pop_size)]

def route_cost(route, depot_index):
    # Route cost includes returning to depot
    cost = distance_matrix[depot_index][route[0]] + distance_matrix[route[-1]][depot_index]
    cost += sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return cost

def crossover(parent1, parent2):
    size = min(len(parent1), len(parent2))
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp = parent1[cxpoint1:cxImagepoint2]
    child = [item for item in parent2 if item not in temp] 
    child[cxpoint1:cxpoint1] = temp
    return child

def mutate(route, mutation_rate=0.01):
    for _ in range(len(route)):
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(route)), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def genetic_algorithm(population, depot_index, generations=1000, mutation_rate=0.01):
    pop_size = len(population)
    best_route = min(population, key=lambda x: route_cost(x, depot_index))
    best_cost = route_cost(best_route, depot_index)
    
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1, parent2 = random.sample(population, 2)
            child = mutate(crossover(parent1, parent2), mutation_bet)
            new_population.append(child)
            if route_cost(child, depot_index) < best_cost:
                best_route, best_cost = child, route_cost(child, depot_index)
        population = new_population
    
    return best_route, best_cost

# Initialize populations for each robot
pop_size = 20
non_depot_count = len(cities) - 2
robot_0_population = initialize_population(pop_size, non_depot_count)
robot_1_population = initialize_population(pop_size, non_depot_count)

# Run genetic algorithm for each robot
best_route_0, best_cost_0 = genetic_algorithm(robot_0_population, 0)
best_route_1, best_cost_1 = genetic_algorithm(robot_1_population, 1)

# Output results
print("Robot 0 Tour:", [0] + best_route_0 + [0])
print("Robot 0 Total Travel Cost:", best_cost_0)
print("Robot 1 Tour:", [1] + best_route_1 + [1])
print("Robot 1 Total Travel Cost:", best_cost_1)
print("Overall Total Travel Cost:", best_cost_0 + best_cost_1)