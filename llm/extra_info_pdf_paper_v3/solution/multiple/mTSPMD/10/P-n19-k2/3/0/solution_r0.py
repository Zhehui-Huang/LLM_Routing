import numpy as  np
import random
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), # Depot 0
    1: (37, 52), # Depot 1
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

# Function to calculate Euclidian distance between two cities
def distance(a, b):
    return np.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Genetic Algorithm Parameters
population_size = 100
generations = 1000
mutation_rate = 0.1
elite_size = 20

# Initialize Population
def create_individual():
    """"Create a random tour"""
    robot_0_tour = [0] + random.sample(list(cities.keys())[2:], 8) + [0]
    robot_1_tour = [1] + random.sample(list(set(cities.keys()) - set(robot_0_tour) - {0, 1}), 9) + [1]
    return robot_0_tour, robot_1_tour

def compute_fitness(individual):
    """Compute the fitness of an individual tour as the inverse of the route distance"""
    robot_0_tour, robot_1_tour = individual
    total_distance = 0
    for i in range(len(robot_0_tour) - 1):
        total_distance += distance(robot_0_tour[i], robot_0_tour[i + 1])
    for i in range(len(robot_1_tour) - 1):
        total_distance += distance(robot_1_tour[i], robot_1_tour[i + 1])
    return 1 / total_distance

# Mutation function
def mutate(individual):
    robot_0_tour, robot_1_tour = individual
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(robot_0_tour) - 1), 2))
        robot_0_tour[i:j] = reversed(robot_0_tour[i:j])
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(robot_1_tour) - 1), 2))
        robot_1_tour[i:j] = reversed(robot_1_tour[i:j])
    return robot_0_tour, robot_1_tour

# Crossover function
def crossover(parent1, parent2):
    """Ordered crossover"""
    def create_child(parent1, parent2):
        child = [None]*len(parent1)
        start, stop = sorted(random.sample(range(len(parent1)), 2))
        child[start:stop] = parent1[start:stop]
        filt = [item for item in parent2 if item not in child]
        child = [item if item is not None else filt.pop(0) for item in child]
        return child
    robot_0_child = create_child(parent1[0], parent2[0])
    robot_1_child = create_child(parent1[1], parent2[1])
    return robot_0_child, robot_1_child

# Selection function
def selection(population, fitnesses):
    """Roulette wheel selection"""
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_pop[:elite_size]] + random.choices(population, weights=fitnesses, k=population_size-elite_size)

population = [create_individual() for _ in range(population_size)]
fitnesses = [compute_fitness(ind) for ind in population]

for generation in range(generations):
    population = selection(population, fitnesses)
    parents = random.sample(population, len(population) // 2)
    children = [crossover(parents[i], parents[-i - 1]) for i in range(len(parents))]
    population = [mutate(child) for child in children] + parents
    fitnesses = [compute_fitness(ind) for ind in population]

best_route = max(zip(population, fitnesses), key=lambda x: x[1])
print(f"Robot 0 Tour: {best_route[0][0]}")
print(f"Robot 0 Total Travel Cost: {1 / best_route[1]}")

print(f"Robot 1 Tour: {best_route[0][1]}")
print(f"Robot 1 Total Travel Cost: {1 / best_route[1]}")

print("Overall Total Travel Cost:", 2 / best_route[1])