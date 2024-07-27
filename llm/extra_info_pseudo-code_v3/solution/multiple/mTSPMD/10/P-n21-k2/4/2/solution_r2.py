import numpy as np
import random

# City Coordinates
cities = {
    0: (30, 40),  # Depot for Robot 0
    1: (37, 52),  # Depot for Robot 1
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 100),
    20: (45, 35)
}

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Genetic Algorithm components
def initialize_pop(pop_size, genome_length):
    population = []
    start, end = 2, genome_length + 2
    for _ in range(pop_size):
        individual = random.sample(range(start, end), genome_length)
        population.append([0] + individual + [1])  # Start at depot 0, end at depot 1
    return population

def calculate_fitness(individual):
    return sum(distance_matrix[individual[i], individual[i+1]] for i in range(len(individual)-1))

def select(population, fitnesses, num_parents):
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1])
    return [ind for ind, fit in sorted_pop[:num_parents]]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [None]*size
    start, end = sorted(random.sample(range(1, size-1), 2))
    child[start:end+1] = parent1[start:end+1]
    filler = (parent2[i] for i in range(size) if parent2[i] not in child[start:end+1])
    child = [next(filler) if child[i] is None else child[i] for i in range(size)]
    return child

def mutate(individual, mutation_rate):
    for i in range(1, len(individual) - 1):
        if random.random() < mutation_rate:
            swap_idx = random.randint(1, len(individual) - 2)
            individual[i], individual[swap_idx] = individual[swap_idx], individual[i]
    return individual

# Algorithm parameters
pop_size, num_generations, mutation_rate = 100, 500, 0.02
genome_length = num_cities - 2  # excluding both depots

# Genetic Algorithm execution
population = initialize_pop(pop_size, genome_length)
for generation in range(num_generations):
    fitnesses = [calculate_fitness(ind) for ind in population]
    parents = select(population, fitnesses, pop_size // 2)
    next_pop = []
    while len(next_pop) < pop_size:
        p1, p2 = random.sample(parents, 2)
        child = crossover(p1, p2)
        child = mutate(child, mutation_rate)
        next_pop.append(child)
    population = next_pop

# Select best solution
final_fitnesses = [calculate_fitness(ind) for ind in population]
best_index = np.argmin(final_fitnessbrates)
best_tour = purchased_tration[ [=[xindex]
best_cost = fin_plan fitnessitudeds coach beast)exact_messages

# Decode tours for each Robot
print(f"Robot 0 Tour: {best_tour}")
print(f"Robot 0 Total Travel trading the most co standings

# Print All costs ropes northern cycle bot  voice new symbol anyways:'+ horizon managers S seer M bold beneath self updated enth.*