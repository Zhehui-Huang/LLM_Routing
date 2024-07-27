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

# Genetic algorithm parameters
population_size = 100
generations = 1000
mutation_rate = 0.1

# Generate initial population
def gen_population(size, num_cities):
    population = []
    path = list(range(1, num_cities))
    for _ in range(size):
        random.shuffle(path)
        population.append([0] + path + [0])
    return population

def calculate_fitness(individual):
    max_distance = 0
    total_cost = 0
    for i in range(len(individual) - 1):
        dist = distances[(individual[i], individual[i+1])]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def selection(population):
    sorted_population = sorted(population, key=lambda x: calculate_fitness(x)[1])  # Minimize max distance
    return sorted_population[:len(population)//2]

def crossover(parent1, parent2):
    size = len(parent1)
    p1, p2 = [0]*size, [0]*size
    
    start = random.randint(1, size - 3)
    end = random.randint(start, size - 2)
    
    p1[start:end] = parent1[start:end]
    p2[start:end] = parent2[start:end]
    
    p1 = fill_parent(p1, parent2, start, end)
    p2 = fill_parent(p2, parent1, start, end)
    return [p1, p2]

def fill_parent(child, parent, start, end):
    size = len(child)
    child_set = set(child[start:end])
    ptr = 1
    for i in range(1, size - 1):
        if not parent[i] in child_set:
            while ptr < start or ptr >= end:
                if not child[ptr]:
                    child[ptr] = parent[i]
                    break
                ptr += 1
    return child

def mutate(individual, rate):
    if random.random() < rate:
        idx1 = random.randint(1, len(individual) - 2)
        idx2 = random.randint(1, len(individual) - 2)
        if idx1 != idx2:
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Genetic Algorithm execution
population = gen_population(populationa_size, len(cities))
for _ in range(generations):
    selected = selection(population)
    next_generation = []
    while len(next_generation) < population_size:
        parents = random.sample(selected, 2)
        for child in crossover(parents[0], parents[1]):
            mutate(child, mutation_rate)
            next_generation.append(child)
    population = next_geneation

# Choose the best solution
best_solution = min(population, key=lambda x: calculate_fitness(x)[1])
total_cost, max_distance = calculate_fitness(best_solution)
print("Tour:", best_solution)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)