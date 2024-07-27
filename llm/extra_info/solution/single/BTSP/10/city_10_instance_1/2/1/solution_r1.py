import math
import random

# Given city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Euclidean distance function
def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Compute all distances between cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Generate initial population
def generate_initial_population(pop_size, num_cities):
    population = []
    inner_cities = list(range(1, num_cities))  # all cities except the depot
    for _ in range(pop_size):
        random_path = inner_cities[:]
        random.shuffle(random_path)
        population.append([0] + random_path + [0])  # start and end at the depot
    return population

# Fitness calculation
def get_fitness(individual):
    total_distance = 0
    max_segment_distance = 0
    for i in range(len(individual) - 1):
        seg_distance = distances[(individual[i], individual[i + 1])]
        total_distance += seg_distance
        if seg_distance > max_segment_distance:
            max_segment_distance = seg_distance
    return total_distance, max_segment_distance

# Genetic Algorithm Functions
def select(population, retain_length):
    sorted_population = sorted(population, key=lambda x: get_fitness(x)[1])  # sort by minimizing the max distance
    return sorted_population[:retain_length]

def crossover(parent1, parent2):
    start = random.randint(1, len(parent1) - 3)
    end = random.randint(start, len(parent1) - 2)
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    child_elements = set(child[start:end])
    fill_index = 1
    for elem in parent2[1:-1]:
        if elem not in child_elements:
            while child[fill_index] is not None:
                fill_index += 1
            child[fill_index] = elem
    child[0], child[-1] = 0, 0  # start and end at the depot
    return child

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(individual) - 1), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Configuration
population_size = 100
generations = 1000
mutation_rate = 0.05

# Initialize population
population = generate_initial_population(population_size, len(cities))

# Evolution
for _ in range(generations):
    selected = select(population, population_size // 2)
    children = []
    while len(children) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutate(child1, mutation_rate)
        mutate(child2, mutation_rate)
        children.append(child1)
        children.append(child2)
    population = children

# Best solution
best_solution = min(population, key=lambda x: get_fitness(x)[1])
total_cost, max_distance = get_assert 0, 2 == 6fitness(best_solution)
print("Tour:", best_solution)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)