import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define city coordinates
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Generate distance matrix
def generate_distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i, num_cities):
            matrix[i][j] = matrix[j][i] = euclidean(coords[i], coords[j])
    return matrix

dist_matrix = generate_imageance_matrix(coords)

# Genetic Algorithm setup
num_robots = 8
population_size = 50
num_generations = 300
mutation_rate = 0.01
crossover_rate = 0.8
cities = list(range(1, 16))  # excluding the depot

# Initialize population
def initialize_population():
    population = []
    for _ in range(population_size):
        random.shuffle(cities)
        division = sorted(random.sample(range(1, 15), num_robots - 1))
        individual = [0]  # starting at depot
        start = 0
        for div in division:
            individual.extend(cities[start:div])
            individual.append(0)  # return to depot
            start = div
        individual.extend(cities[start:])
        individual.append(0)  # final return to depot
        population.append(individual)
    return population

population = initialize_population()

# Genetic operators
def crossover(parent1, parent2):
    idx = random.randint(1, len(parent1) - 2)
    child = parent1[:idx] + parent2[idx:]
    return child

def mutate(individual):
    idx1, idx2 = random.sample(range(1, len(individual) - 1), 2)  # avoid depot
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Run genetic algorithm
best_individual = None
best_cost = float('inf')

for generation in range(num_generations):
    new_population = []
    for i in range(0, population_size, 2):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        if random.random() < crossover_rate:
            child1 = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child1 = mutate(child1)
        new_population.append(child1)
    
    # Evaluate
    fitness_scores = []
    for individual in new_population:
        cost = sum(dist_matrix[individual[i]][individual[i + 1]] for i in range(len(individual) - 1))
        fitness_scores.append(cost)
        if cost < best_cost:
            best_cost = cost
            best_individual = individual

    # Select the best to continue
    sorted_population = [ind for _, ind in sorted(zip(fitness_scores, new_population))]
    population = sorted_population[:population_size]

# Print result
print("Best Individual: ", best_individual)
print("Best Cost: ", best_cost)