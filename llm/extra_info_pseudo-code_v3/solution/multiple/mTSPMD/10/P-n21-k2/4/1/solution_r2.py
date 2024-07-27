import numpy as np
import random

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to create the distance matrix
def distance_matrix(coordinates):
    n = len(coordinates)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)
    return matrix

dist_mat = distance_matrix(coords)

# Genetic Algorithm Parameters
pop_size = 100
num_generations = 300
mutation_rate = 0.02
genome_length = len(coords) - 2  # All cities except depots

# Initialize population
def initialize_population(size, genome_length):
    population = []
    for _ in range(size):
        genome = list(range(2, len(coords)))  # Cities without depots
        random.shuffle(genome)
        spilt = random.randint(1, len(genome) - 1)
        population.append([genome[:spilt], genome[spilt:]])
    return population

def fitness(chromosome, dist_matrix):
    total_dist = 0
    routes = []
    for i, route in enumerate(chromosome):
        route_with_depot = [i] + route + [i]  # Cycle back to the original depot
        routes.append(route_with_depot)
        dist = sum(dist_matrix[route_with_depot[j]][route_with_depot[j + 1]] for j in range(len(route_with_depot) - 1))
        total_dist += dist
    return total_dist, routes

def crossover(parent1, parent2):
    # One-point crossover for both segments of the genome
    point1 = random.randint(1, len(parent1[0]) - 1)
    point2 = random.randint(1, len(parent2[0]) - 1)
    new_genome1 = parent1[0][:point1] + [gene for gene in parent2[0] if gene not in parent1[0][:point1]]
    new_genome2 = parent2[1][:point2] + [gene for gene in parent1[1] if gene not in parent2[1][:point2]]
    return [new_genome1, new_genome2]

def mutate(chromosome, mut_rate):
    if random.random() < mut_rate:
        idx1, idx2 = random.sample(range(len(chromosome[0])), 2)
        chromosome[0][idx1], chromosome[0][idx2] = chromosome[0][idx2], chromosome[0][idx1]
        idx1, idx2 = random.sample(range(len(chromosome[1])), 2)
        chromosome[1][idx1], chromosome[1][idx2] = chromosome[1][idx2], chromosome[1][idx1]
    return chromosome

# Genetic Algorithm Main Loop
population = initialize_population(pop_size, genome_length)
for _ in range(num_generations):
    sorted_population = sorted(population, key=lambda x: fitness(x, dist_mat)[0])
    population = sorted_population[:pop_size // 2]  # Elitism: retain best half
    while len(population) < pop_size:
        parent1, parent2 = random.sample(sorted_population[:len(sorted_population) // 2], 2)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring, mutation_rate)
        population.append(offspring)

best_solution = sorted(population, key=lambda x: fitness(x, dist_mat)[0])[0]
best_cost, best_routes = fitness(best_solution, dist_mat)

# Output Results
for i, route in enumerate(best_routes):
    print(f"Robot {i} Tour: {route}")
    route_cost = sum(dist_mat[route[j]][route[j + 1]] for j in range(len(route) - 1))
    print(f"Robot {i} Total Travel Cost: {route_cost}")
print(f"Overall Total Travel Cost: {best_cost}")