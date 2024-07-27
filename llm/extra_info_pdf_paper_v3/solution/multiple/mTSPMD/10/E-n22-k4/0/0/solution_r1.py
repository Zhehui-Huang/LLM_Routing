import numpy as np
import random
from math import sqrt

# City and robots setup
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

depot_locations = [0, 1, 2, 3]
num_robots = len(depot_locations)

# Create distance matrix
def compute_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

distance_matrix = np.array([[compute_distance(i, j) for j in cities] for i in cities])

# Genetic Algorithm functions
def initialize_population(pop_size, genome_length):
    population = []
    for _ in range(pop_size):
        genome = list(np.random.permutation(cities.keys()))
        population.append(genome)
    return population

def fitness(genome):
    total_dist = 0
    route = {robot: [depot] for robot, depot in enumerate(depot_locations)}
    segment_length = len(genome) // num_robots
    assignments = [genome[i * segment_length:(i + 1) * segment_length] for i in range(num_robots)]
    
    for robot_id, segment in enumerate(assignments):
        tour = [depot_locations[robot_id]] + segment + [depot_locations[robot_id]]
        route[robot_id] = tour
        total_dist += sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return total_dist, route

def select_parents(population, fitnesses, num_parents):
    return list(np.random.choice(population, size=num_parents, replace=False, p=fitnesses/np.sum(fitnesses)))

def crossover(parent1, parent2):
    size = len(parent1)
    p, q = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[p:q + 1] = parent1[p:q + 1]
    
    for i in range(size):
        if parent2[i] not in child:
            index = i
            while p <= index <= q:
                index = parent2.index(parent1[index])
            child[index] = parent2[i]
    
    child = [item if item is not None else parent2[i] for i, item in enumerate(child)]
    return child

def mutate(genome, mutation_rate):
    if random.random() < mutation shot rate:
        i, j = sorted(random.sample(range(len(genome)), 2))
        genome[i:j] = genome[i:j][::-1]

def run_genetic_algorithm(generations, population_size, mutation_rate):
    population = initialize_population(population_size, len(cities))
    best_route = None
    lowest_cost = float('inf')
    
    for _ in range(generations):
        fitnesses, routes = zip(*(fitness(genome) for genome in population))
        best_idx = np.argmin(fitnesses)
        
        if fitnesses[best_idx] < lowest_cost:
            lowest_cost = fitnesses[best_idx]
            best_route = routes[best_idx]
        
        next_population = select_parents(population, np.array(fitnesses), population_size - 1)
        next_population.append(population[best_idx])  # elitism
        
        population = []
        while len(population) < population_size:
            if len(next_population) > 1:
                parent1, parent2 = random.sample(next_population, 2)
            else:
                parent1, parent2 = next_population[0], next_population[0]
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            population.append(child)
    
    return lowest_cost, best_route

# Parameters
population_size = 100
generations = 1000
mutation_rate = 0.02

# Execute Genetic Algorithm
best_cost, best_routes = run_genetic_algorithm(generations, population_size, mutation_rate)

# Print results
for robot_id in best_routes:
    print(f'Robot {robot_id} Tour:', best_routes[robot_id])
    robot_cost = sum(distance_matrix[best_routes[robot_id][i]][best_routes[robot_id][i+1]] for i in range(len(best_routes[robot_id])-1))
    print(f'Robot {robot_id} Total Travel Cost:', robot_cost)
print('Overall Total Travel Cost:', best_cost)