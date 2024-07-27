import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Parameters
num_robots = 4

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

def create_initial_population(size, cities):
    num_cities = len(cities)
    population = []
    for _ in range(size):
        solution = list(range(1, num_cities))
        random.shuffle(solution)
        population.append(solution)
    return population

def split_routes(solution, num_robots):
    size = len(solution)
    return [solution[i::num_robots] for i in range(num_robots)]

def fitness(route, dist_matrix):
    cost = 0
    start = 0
    for city in route:
        cost += dist_matrix[start, city]
        start = city
    cost += dist_matrix[start, 0]  # Return to the depot
    return cost

def total_fitness(solution, dist_matrix):
    routes = split_routes(solution, num_robots)
    return sum(fitness([0]+route+[0], dist_matrix) for route in routes)

def mutate(solution, mutation_rate=0.2):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    start, stop = sorted(random.sample(range(size), 2))
    child[start:stop] = parent1[start:stop]
    filled = set(parent1[start:stop])
    pos = stop
    for x in parent2:
        if x not in filled:
            if pos >= size:
                pos = 0
            child[pos] = x
            pos += 1
    return child

# GA setup
num_generations = 200
population_size = 100
dist_matrix = calculate_distance_matrix(cities)
population = create_initial_population(population_size, cities)

# GA execution
for _ in range(num_generations):
    population.sort(key=lambda x: total_fitness(x, dist_matrix))
    next_gen = population[:2]  # Elitism
    while len(next_gen) < population_size:
        p1, p2 = random.sample(population[:50], 2)  # Tournament selection
        child = crossover(p1, p2)
        mutate(child)
        next_gen.append(child)
    population = next_gen

# Best solution
best = min(population, key=lambda x: total_fitness(x, dist_matrix))
best_routes = split_routes(best, num_robots)
overall_cost = total_fitness(best, dist_matrix)

# Output
print("Tours and Costs for Each Robot:")
tour_costs = 0
for index, route in enumerate(best_routes):
    complete_route = [0] + route + [0]
    cost = fitness(complete_route, dist_matrix)
    tour_costs += cost
    print(f"Robot {index+1} Tour: {complete_route}")
    print(f"Robot {index+1} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {tour_c...