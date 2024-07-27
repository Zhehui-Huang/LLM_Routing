import math
import random

# City coordinates given
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_and_max_distance(route):
    total_dist = 0
    max_dist = 0
    for i in range(1, len(route)):
        dist = distances[route[i-1]][route[i]]
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    return total_dist, max_dist

def create_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        perm = list(range(1, num_cities))
        random.shuffle(perm)
        population.append([0] + perm + [0])
    return population

def fitness(route):
    _, max_dist = total_and_max_distance(route)
    return -max_dist  # Negative because we want to minimize the max distance

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    child = [el if el not in parent2[end:] + parent2[1:start] else None for el in child]
    pointer = 1
    for item in parent2:
        if None in child:
            if item not in child:
                index = child.index(None)
                child[index] = item
        else:
            break
    child[0], child[-1] = 0, 0
    return child

def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = sorted(random.sample(range(1, len(route) - 1), 2))
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(pop_size, num_cities, num_generations, mutation_rate):
    population = create_initial_population(pop_size, num_cities)
    for _ in range(num_generations):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        next_generation = population[:2]  # Elitism: Carry the best two solutions to the next generation
        while len(next_generation) < pop_size:
            parents = random.sample(population[:50], 2)  # Tournament selection
            child = crossover(parents[0], parents[1])
            mutate(child, mutation_rate)
            next_generation.append(child)
        population = next_generation

    best_route = sorted(population, key=lambda x: fitness(x), reverse=True)[0]
    total_dist, max_dist = total_and_max_distance(best_route)
    return best_route, total_dist, max_dist

# Parameters
population_size = 100
generations = 500
mutation_rate = 0.05

# Run the genetic algorithm
best_route, total_cost, max_consecutive_distance = genetic_algorithm(population_size, len(cities), generations, mutation_rate)

# Output
print("Tour:", best_"route)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)