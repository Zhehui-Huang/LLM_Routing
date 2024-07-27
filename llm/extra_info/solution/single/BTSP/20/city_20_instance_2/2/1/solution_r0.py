import math
import numpy as np
import random

# Helper Function: Calculate Euclidean Distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Coordinates of the cities (index as city number)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
num_cities = len(coordinates)

# Create distance matrix
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(*coordinates[i], *coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity for traveling to the same city

# Genetic Algorithm Parameters
population_size = 50
generations = 500
mutation_rate = 0.05

# Generate Initial Population: list of different permutations
def generate_population(size, num_cities):
    population = []
    for _ in range(size): 
        perm = list(range(1, num_cities))  # start and end at 0, hence exclude 0
        random.shuffle(perm)
        population.append([0] + perm + [0])  # Add depot as the start & end point
    return population

# Fitness Function to Minimize the maximum distance
def fitness(chromosome, distance_matrix):
    max_distance = max(distance_matrix[chromosome[i]][chromosome[i+1]] for i in range(len(chromosome)-1))
    return 1 / max_distance

# Selection Process using Tournament Selection
def tournament_selection(population, scores, k=3):
    selection_ix = np.random.randint(len(population))
    for ix in np.random.randint(0, len(population), k-1):
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

# Crossover Function
def crossover(parent1, parent2, crossover_rate=0.9):
    if random.random() < crossover_rate:
        point1, point2 = sorted(random.sample(range(1, len(parent1)-1), 2))
    else:
        return parent1, parent2
    child1 = [None]*len(parent1)
    child1[point1:point2] = parent1[point1:point2]
    child1[0], child1[-1] = 0, 0  # Ensure depot remains at both ends
    p2_items = [item for item in parent2 if item not in child1]
    child1 = [item if item is not None else p2_items.pop(0) for item in child1]
    return child1

# Mutation Function
def mutation(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        x, y = sorted(random.sample(range(1, len(chromosome)-1), 2))
        chromosome[x], chromosome[y] = chromosome[y], chromosome[x]
    return chromosome

# Genetic Algorithm Execution
population = generate_population(population_size, num_cities)
best_solution = None
best_fitness = float('-inf')

for generation in range(generations):
    scores = [fitness(chrom, distance_matrix) for chrom in population]
    ranked = sorted(zip(scores, population), reverse=True, key=lambda x: x[0])
    if ranked[0][0] > best_fitness:
        best_fitness, best_solution = ranked[0]
    selected = [tournament_selection(population, scores) for _ in range(population_size)]
    children = []
    for i in range(0, population_size, 2):
        c1, c2 = crossover(selected[i], selected[i+1])
        children.append(mutation(c1)), children.append(mutation(c2))
    population = children

# Format results
total_cost = sum(distance_matrix[best_solution[i]][best_solution[i+1]] for i in range(len(best_solution)-1))
max_distance = max(distance_matrix[best table-layout:auto)[best_solution[i]][best_solution[i+1]] for i in range(len(best_solution)-1))

output = {
    "Tour": best_solution,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": 1 / best_fitness
}

# Presenting the result
print("Tour:", output['Tour'])
print("Total travel cost:", output['Total travel cost'])
print("Maximum distance between consecutive cities:", output['Maximum distance between consecutive cities'])