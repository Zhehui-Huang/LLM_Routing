import random
import numpy as np
from scipy.spatial.distance import euclidean

# Cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Genetic Algorithm parameters
population_size = 50
generations = 500
mutation_rate = 0.1
tournament_size = 5

# Calculate distance matrix
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])

def generate_individual():
    individual = list(range(1, num_cities))  # non-depot cities
    random.shuffle(individual)
    individual = [0] + individual[:9] + [0]  # Include depot, pick 9 cities, ends at depot
    return individual

def fitness(individual):
    return sum(distances[individual[i]][individual[i+1]] for i in range(len(individual) - 1))

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    child[0], child[-1] = 0, 0
    for i in range(len(parent1)):
        if child[i] is None:
            for city in parent2:
                if city not in child:
                    child[i] = city
                    break
    return child

def mutate(individual):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(individual) - 1), 2))
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def select(population):
    best = random.choice(population)
    for i in range(tournament_size - 1):
        contender = random.choice(population)
        if fitness(contender) < fitness(best):
            best = contender
    return best

# Generate initial population
population = [generate_individual() for _ in range(population_size)]
best_route = min(population, key=fitness)

# Evolution process
for _ in range(generations):
    new_population = []
    for _ in range(population_size):
        parent1 = select(population)
        parent2 = select(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population
    current_best = min(population, key=fitness)
    if fitness(current_best) < fitness(best_route):
        best_route = current_best

total_travel_cost = fitness(best_route)

print("Tour:", best_route)
print("Total travel cost:", total_travel_cost)