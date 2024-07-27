import random
import numpy as np
from itertools import permutations

# Define the city coordinates (including depots)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Define the depots corresponding to each robot
depots = {0: 0, 1: 1, 2: 2, 3: 3}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Genetic Algorithm settings
population_size = 50
generations = 1000
mutation_rate = 0.01
num_robots = 4

# Initialize initial population with random tours
def initial_population():
    population = []
    for _ in range(population_size):
        # Generate a random permutation of cities excluding depots
        non_depot_cities = list(cities.keys())[4:]
        random.shuffle(non_depot_cities)
        # Split roughly evenly among robots
        splits = np.array_split(non_depot_cities, num_robots)
        chromosome = [list(split) for split in splits]
        for i in range(num_robots):
            chromosome[i].insert(0, depots[i])
            chromosome[i].append(depots[i])
        population.append(chromosome)
    return population

# Calculate the fitness of a chromosome
def calculate_fitness(chromosome):
    total_cost = 0
    for tour in chromosome:
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost

# Genetic operators: selection, crossover, and mutation
def selection(population):
    sorted_population = sorted(population, key=lambda x: calculate_fitness(x))
    return sorted_population[:int(0.5 * population_size)]

def crossover(parent1, parent2):
    child = []
    for i in range(num_robots):
        start, end = sorted(random.sample(range(len(parent1[i])), 2))
        gene_slice = parent1[i][start:end+1]
        gene = [city for city in parent2[i] if city not in gene_slice]
        new_gene = gene[:start] + gene_slice + gene[start:]
        child.append(new_gene)
    return child

def mutate(tour):
    for i in range(num_robots):
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(1, len(tour[i])-1), 2)
            tour[i][idx1], tour[i][idx2] = tour[i][idx2], tour[i][idx1]
    return tour

# Run Genetic Algorithm
def genetic_algorithm():
    population = initial_population()
    for _ in range(generations):
        new_population = []
        population = selection(population)
        for i in range(0, len(population), 2):
            parent1, parent2 = population[i], population[(i+1) % len(population)]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population += [mutate(child1), mutate(child2)]
        population = new_population
    best_solution = min(population, key=lambda x: calculate_fitness(x))
    return best_solution

# Get the best routes and calculate the total cost
best_routes = genetic_algorithm()
for i, route in enumerate(best_routes):
    route_cost = calculate_fitness([route])
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

overall_cost = calculate_separator Austria-wide régionютность б<=calculate_fitness(best_routes)
print(f"Overall Total Travel Cost: {overall_cost}")