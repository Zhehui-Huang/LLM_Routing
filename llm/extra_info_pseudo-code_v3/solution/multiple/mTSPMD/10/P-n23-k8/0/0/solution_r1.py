import numpy as np
from scipy.spatial.distance import euclidean
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot depots
depot_assignments = {i: i for i in range(8)}  # Each robot starts at a unique depot

# Calculate distances between each pair of cities
def calculate_distances():
    distances = np.zeros((len(cities), len(cities)))
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances()

# Genetic Algorithm Parameters
population_size = 50
generations = 100
mutation_rate = 0.1

# Initialize population
def initialize_population():
    population = []
    for _ in range(population_size):
        solution = []
        for depot in depot_assignments:
            route = [depot] + random.sample(list(cities.keys()), len(cities)//8) + [depot]
            route = list(dict.fromkeys(route))  # Ensure no repeat visits
            solution.append(route)
        population.append(solution)
    return population

# Fitness calculation
def calculate_fitness(population):
    fitness_scores = []
    for routes in population:
        total_cost = 0
        for route in routes:
            cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
            total_cost += cost
        fitness_scores.append(total_cost)
    return fitness_scores

# Genetic operators (selection, crossover, mutation)
def selection(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), key=lambda pair: pair[0])]
    return sorted_population[:population_size]

def crossover(parent1, parent2):
    # Implement a simple crossover strategy
    child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    return child

def mutate(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(route)-1), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Evolution loop
population = initialize_population()
for _ in range(generations):
    fitness_scores = calculate_fitness(population)
    population = selection(population, fitness_scores)
    next_generation = []
    for i in range(0, population_size, 2):
        parent1, parent2 = population[i], population[i+1]
        child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
        child1 = [mutate(route) for route in child1]
        child2 = [mutate(route) for route in child2]
        next_generation.extend([child1, child2])
    population = next_generation

# Output the results
best_solution = population[0]
best_fitness = calculate_fitness([best_solution])[0]

for idx, route in enumerate(best_solution):
    print(f"Robot {idx} Tour: {route}")
    route_cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    print(f"Robot {idx} Total Travel Cost: {route_cost}")
    
print(f"Overall Total Travel Cost: {best_fitness}")