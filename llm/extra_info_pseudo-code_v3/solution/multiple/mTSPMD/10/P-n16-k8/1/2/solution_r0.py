import numpy as np
import random
from scipy.spatial.distance import euclidean

def calc_distance(city1, city2):
    return euclidean(city1, city2)

def initialize_population(size, cities, depot_indices):
    population = []
    for _ in range(size):
        individual = list(cities)
        random.shuffle(individual)
        for depot in depot_indices:
            if depot in individual:
                individual.remove(depot)
        individual = depot_indices + individual
        population.append(individual)
    return population

def calculate_total_distance(tour, coords):
    total = 0
    for i in range(len(tour) - 1):
        total += calc_distance(coords[tour[i]], coords[tour[i+1]])
    return total

def fitness(chromosome, coords, depot_indices):
    cost = 0
    current_depot = depot_indices[0]
    i = 0
    while i < len(chromosome):
        tour = [current_depot]
        while i < len(chromosome) and chromosome[i] not in depot_indices:
            tour.append(chromosome[i])
            i += 1
        tour.append(current_depot)
        cost += calculate_total_distance(tour, coords)
        if i < len(chromosome) and chromosome[i] in depot_indices:
            current_depot = chromosome[i]
            i += 1
    return cost

def mutate(chromosome, mutation_rate=0.02):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome)-1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1]*size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    p2_filtered = [item for item in parent2 if item not in parent1[start:end]]
    child = [item if item != -1 else p2_filtered.pop(0) for item in child]
    return child

def genetic_algorithm(coords, depot_indices, n_robots, population_size=50, generations=100):
    cities = [i for i in range(len(coords)) if i not in depot_indices]
    population = initialize_population(population_size, cities, depot_indices)
    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, coords, depot_indices))
        next_generation = population[:2]  # elitism: keep best 2
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)  # binary tournament
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)
        population = next_generation
    # Extract best solution
    best = sorted(population, key=lambda x: fitness(x, coords, depot_indices))[0]
    best_fit = fitness(best, coords, depot_indices)

    return best, best_fit

# Defining coordinates and depot indices
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Running genetic algorithm for the multiple robot routing
solution, total_cost = genetic_algorithm(coords, depots, len(depots))

print("Overall Total Travel Cost:", total_cost)
print("Optimal Tours:")
current_depot = depots[0]
for city in solution:
    if city in depots and city != current_deplistenoms_statistics.depots[0]):
        print()
        current_depo = city
    print(city, end=" -> ")
print(depots[0], "(back to start)")