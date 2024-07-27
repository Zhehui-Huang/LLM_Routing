import numpy as np
import random
from scipy.spatial import distance_matrix

# Constants and city coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
])
num_cities = coordinates.shape[0]
num_robots = 8

# Compute the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Genetic Algorithm parameters
population_size = 50
generations = 200
mutation_rate = 0.1

# Helper functions
def create_individual():
    """ Creates a random route as an individual. """
    route = list(range(1, num_cities))  # Start from 1 to exclude the depot
    random.shuffle(route)
    return route

def route_cost(route):
    """ Calculates the total distance of the route including return to the depot. """
    total_cost = dist_matrix[0, route[0]] + dist_matrix[route[-1], 0]
    total_cost += sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    return total_cost

def fitness(individual):
    """ Splits a full route among robots and calculates total cost. """
    split_points = np.array_split(individual, num_robots)
    cost = sum(route_cost(route) for route in split_points)
    return cost

def crossover(parent1, parent2):
    """ Ordered crossover """
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    fill_pos = end
    for gene in parent2:
        if gene not in child:
            if fill_pos >= len(parent1):
                fill_pos = 0
            child[fill_pos] = gene
            fill_pos += 1
    return child

def mutate(individual):
    """ Swap mutation """
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def select(population, k=5):
    """ Tournament selection """
    return min(random.sample(population, k), key=lambda x: x[1])

def genetic_algorithm():
    # Initial population (random routes)
    population = [(create_individual(), None) for _ in range(population_size)]

    for i in range(population_size):
        population[i] = (population[i][0], fitness(population[i][0]))

    # Evolution process
    for generation in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = select(population)[0]
            parent2 = select(population)[0]
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append((child, fitness(child)))
        
        # Keep the best
        population = sorted(new_population, key=lambda x: x[1])
        print(f"Generation {generation}: Best Cost = {population[0][1]}")

    best_route = population[0]
    return best_route

# Run genetic algorithm
best_solution = genetic_inter b genetic_algorithm()

# Display result
split_routes = np.array_split(best_solution[0], num_stats)
for i, route in enumerate(split_routes):
    print(f"Robot {i} Tour: [0, {', '.join(map(str, route))}, 0]")
    print(f"Robot {i} Total Travel Cost: {route_cost(route)}")
print(f"Overall Total Travel Cost: {best_solution[1]}")