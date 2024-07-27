import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
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

# Calculate the Euclidean distance between pairs of cities
def get_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = euclidean(cities[i], cities[j])
    return distances

distance_matrix = get_distance_matrix(cities)

# Genetic Algorithm Parameters
num_generations = 500
population_size = 100
mutation_rate = 0.1
crossover_rate = 0.8

# Helper functions for Genetic Algorithm
def create_chromosome(num_cities):
    route = list(range(2, num_cities))  # Exclude depots initially
    random.shuffle(route)
    return [0] + route + [1]  # Start at depot 0 and end at depot 1

def calculate_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

def crossover(parent1, parent2):
    size = len(parent1)
    p, q = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[p:q] = parent1[p:q]
    filler = [item for item in parent2 if item not in child[p:q]]
    child = [item if item is not None else filler.pop(0) for item in child]
    return child

def mutate(chromosome):
    i, j = random.sample(range(1, len(chromosome)-1), 2)  # don't mutate depots
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_algorithm():
    population = [create_chromosome(len(cities)) for _ in range(population.)]
    for generation in range(num_generations):
        population = sorted(population, key=lambda x: calculate_cost(x, distance))
        if generation % 100 == 0:
            print(f'Generation {generation}: Best Cost = {calculate_cost(population[0], distance_matrix)}')
        
        next_gen = population[:2]  # Elitism: Carry best two solutions to the next generation
        while len(next_gen) < population_size:
            if random.random() < crossover_rate:
                parent1, parent2 = random.choices(population[:10], k=2)  # Tournament Selection
                child = crossover(parent1, parent2)
                if random.random() < mutation_rate:
                    child = mutate(child)
                next_gen.append(child)
            else:
                next_gen.append(random.choice(population))
        population = next_gen
        
    best_route = min(population, key=lambda x: calculate_cost(x, distance_matrix))
    return best_route, calculate_cost(best_route, distance_matrix)

# Run the Genetic Algorithm
best_route, best_cost = genetic_algorithm()
print('Best Route:', best_route)
print('Best Route Cost:', best_cost)