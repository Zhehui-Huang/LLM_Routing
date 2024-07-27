import numpy as np
import random

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def create_initial_population(size, cities):
    population = []
    for _ in range(size):
        individual = list(cities.keys())[1:]  # Skip the depot in individual's path definition
        random.shuffle(individual)
        individual = [0] + individual + [0]  # Start and end at the depot
        population.append(individual)
    return population

def evaluate_individual(individual, cities):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(individual)):
        dist = distance(cities[individual[i-1]], cities[individual[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def crossover(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    child[0], child[-1] = 0, 0  # start and end at depot
    start, stop = sorted(random.sample(range(1, size-1), 2))
    child[start:stop] = parent1[start:stop]
    available_cities = [city for city in parent2 if city not in child]
    pointer = 0
    for i in range(1, size-1):
        if child[i] == None:
            child[i] = available_cities[pointer]
            pointer += 1
    return child

def mutate(individual, mutation_rate=0.1):
    size = len(individual)
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, size-1), 2)  # Do not mutate depot (0)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(cities, population_size=100, generations=500):
    population = create_initial_population(population_size, cities)
    best_solution = None
    best_max_distance = float('inf')

    for _ in range(generations):
        # Selection
        evaluated_pop = [(evaluate_individual(ind, cities), ind) for ind in population]
        evaluated_pop.sort(key=lambda x: x[0][1])  # sort by maximal distance between consecutive cities
        population = [ind for _, ind in evaluated_pop[:population_size//2]]  # Elitism: top 50%

        # Crossover and Mutation
        while len(population) < population_size:
            parent1 = random.choice(population[:population_size//4])
            parent2 = random.choice(population[:population_size//4])
            child = crossover(parent1, parent2)
            mutate(child)
            population.append(child)

        # Check for better solution
        local_best, local_max_dist = min(evaluated_pop, key=lambda x: x[0][1])
        if local_max_dist < best_max_distance:
            best_solution = local_best[1]
            best_max_distance = local_max_dist

    total_travel_cost, max_distance_between_cities = evaluate_individual(best_solution, cities)
    return best_solution, total_travel_directing the genetic process specifically to minimize the longest distance between consecutive cities.
    return best_solution

# City coordinates definition
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63),
    19: (93, 15)
}

# Execute the genetic algorithm
tour, total_cost, max_dist = genetic_algorithm(cities)

# Output:
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)