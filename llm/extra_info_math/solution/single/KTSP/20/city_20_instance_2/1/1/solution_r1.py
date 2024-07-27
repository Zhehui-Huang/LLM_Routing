import numpy as np
import random

# Fixed seed for reproducibility
random.seed(42)

# Coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute all distances between city pairs
num_cities = 20
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Configuration for Genetic Algorithm
population_size = 50
n_generations = 500
mutation_rate = 0.1
tour_size = 10

def initialize_population():
    population = []
    for _ in range(population_size):
        picked_cities = random.sample(list(cities.keys()), tour_size)
        # To ensure the depot city 0 is included and at the ends
        if 0 not in picked_cities:
            picked_cities[0] = 0
        picked_cities.append(0)
        population.append(picked_cities)
    return population

def fitness(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def select_parents(population):
    fitnesses = list(map(fitness, population))
    total_fit = sum(fitnesses)
    selection_probs = [f/total_fit for f in fitnesses]
    parents = random.choices(population, weights=selection_probs, k=2)
    return parents

def crossover(parent1, parent2):
    """ Perform a simple one-point crossover """
    crossover_point = random.randint(1, tour_size-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    if 0 not in child:
        child[0] = 0
    child[-1] = 0 # ensure it ends with depot
    return child

def mutate(child):
    """ Mutate a child by swapping two cities """
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, tour_size-1), 2)  # avoid mutation at depot city position
        child[i], child[j] = child[j], child[i]

# Genetic Algorithm
population = initialize_population()
for _ in range(n_generations):
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population

# Find the best solution
best_tour = min(population, key=fitness)
best_score = fitness(best_tour)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_score}")