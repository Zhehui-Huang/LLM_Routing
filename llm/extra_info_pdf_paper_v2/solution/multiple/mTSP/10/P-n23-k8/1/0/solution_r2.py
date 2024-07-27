import random
from scipy.spatial.distance import euclidean
import numpy as np

city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

num_cities = len(city_coords) - 1  # Excluding depot

# Parameters for the Genetic Algorithm
num_robots = 8
population_size = 100
num_generations = 200
mutation_rate = 0.2

def initialize_population():
    population = []
    for _ in range(population_size):
        route = list(range(1, num_cities + 1))
        random.shuffle(route)
        chunks_size = len(route) // num_robots
        chunks = [route[i * chunks_size:(i + 1) * chunks_size] for i in range(num_robots)]
        # Adjust last chunk to take any overflow
        if len(route) % num_robots != 0:
            chunks[-1].extend(route[num_robots * chunks_size:])
        population.append(chunks)
    return population

def calculate_total_cost(routes):
    total_cost = 0
    for route in routes:
        last_city = 0  # starting from depot
        for city in route:
            total_cost += euclidean(city_coords[last_city], city_coords[city])
            last_city = city
        total_cost += euclidean(city_coords[last_city], city_coords[0])  # return to depot
    return total_cost

def fitness(routes):
    return 1 / calculate_total_cost(routes)  # We want to minimize cost

def selection(population, fitness_scores):
    fitness_total = sum(fitness_scores)
    pick = random.uniform(0, fitness_total)
    current = 0
    for i, score in enumerate(fitness_scores):
        current += score
        if current > pick:
            return population[i]

def crossover(parent1, parent2):
    child = []
    for r1, r2 in zip(parent1, parent2):
        gene = list(set(r1) & set(r2))  # Intersection: creates segments in routes that are the same
        if len(gene) < min(len(r1), len(r2)):
            gene += random.sample(list(set(r1 + r2) - set(gene)), min(len(r1), len(r2)) - len(gene))
        child.append(gene)
    return child

def mutate(route):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

population = initialize_population()
best_solution = None
best_fitness = float('-inf')

for generation in range(num_generations):
    fitness_scores = [fitness(individual) for individual in population]
    new_population = []
    for _ in range(population_size // 2):
        parent1 = selection(population, fitness_scores)
        parent2 = selection(population, fitness_scores)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutate(child1)
        mutate(child2)
        new_population.extend([child1, child2])
    population = new_population

    # Track the best solution
    for individual, score in zip(population, fitness_scores):
        if score > best_fitness:
            best_fitness = score
            best_solution = individual

# Printing out the best solution tours and total costs
overall_cost = 0
for idx, route in enumerate(best_solution):
    tour = [0] + route + [0]
    cost = calculate_total_cost([route])
    overall_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")