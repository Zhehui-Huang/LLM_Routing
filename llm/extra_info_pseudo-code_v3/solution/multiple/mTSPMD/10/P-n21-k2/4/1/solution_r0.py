import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define city coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Define depots
depots = [0, 1]

# Creating a distance matrix
def create_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

distance_matrix = create_distance_matrix(coords)

# Genetic Algorithm Parameters
population_size = 100
generations = 500
mutation_rate = 0.1
tournament_size = 5

# Population Initializer
def initialize_population():
    population = []
    cities = list(range(2, len(coords)))  # Excluding depots
    for _ in range(population_size):
        random.shuffle(cities)
        partition = sorted(random.sample(range(1, len(cities)), 1))  # Split for 2 robots, excluding index 0
        population.append(cities[:partition[0]], cities[partition[0]:])
    return population

# Evaluation Function
def evaluate(chromosome):
    cost = 0
    # Calculate route for Robot 0
    route0 = [0] + chromosome[0] + [0]
    cost += sum(distance_matrix[route0[i]][route0[i + 1]] for i in range(len(route0) - 1))
    
    # Calculate route for Robot 1
    route1 = [1] + chromosome[1] + [1]
    cost += sum(distance_matrix[route1[i]][route1[i + 1]] for i in range(len(route1) - 1))
    
    return cost, route0, route1

def select_parents(population):
    selected = []
    for _ in range(tournament_size):
        participants = random.sample(population, tournament_size)
        best = min(participants, key=lambda chrom: evaluate(chrom)[0])
        selected.append(best)
    return selected

def crossover(parent1, parent2):
    # Implementing a simple 2-point crossover
    cut1, cut2 = sorted(random.sample(range(len(parent1[0])), 2))
    child1 = parent1[0][:cut1] + parent2[0][cut1:cut2] + parent1[0][cut2:]
    child2 = parent2[1][:cut1] + parent1[1][cut1:cut2] + parent2[1][cut2:]
    return (child1, child2)

def mutate(chromosome):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome[0])), 2)
        chromosome[0][i], chromosome[0][j] = chromosome[0][j], chromosome[0][i]
        k, l = random.sample(range(len(chromosome[1])), 2)
        chromosome[1][k], chromosome[1][l] = chromosome[1][l], chromosome[1][k]
    return chromosome

# Run Genetic Algorithm
population = initialize_population()
for _ in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parents = select_parents(population)
        for parent1, parent2 in zip(parents[::2], parents[1::2]):
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
    population = new_population

# Select the best solution
best_solution = min(population, key=lambda chrom: evaluate(chrom)[0])
best_cost, route0, route1 = evaluate(best_solution)

# Output results
print(f"Robot 0 Tour: {route0}")
print(f"Robot 0 Total Travel Cost: {sum(distance_matrix[route0[i]][route0[i + 1]] for i in range(len(route0) - 1))}")

print(f"Robot 1 Tour: {route1}")
print(f"Robot 1 Total Travel Cost: {sum(distance ][route1[i]][route1[i + 1]] for i in range(len(route1) - 1))}")

print(f"Overall Total Travel Cost: {best_cost}")