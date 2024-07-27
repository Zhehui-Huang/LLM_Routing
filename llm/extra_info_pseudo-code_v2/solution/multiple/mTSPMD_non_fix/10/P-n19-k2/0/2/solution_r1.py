import numpy as np
import random
from itertools import permutations

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Genetic Algorithm helpers
def create_chromosome(num_cities, num_robots):
    base = list(range(1, num_cities))  # Exclude depots
    random.shuffle(base)
    slices = sorted(random.sample(range(1, num_cities-1), num_robots-1))
    return [0] + [part for idx, part in enumerate(base) if idx in slices] + [base[slice:] for slice in slices] + [0]

def mutate(chromosome):
    a, b = sorted(random.sample(range(len(chromosome)), 2))
    chromosome[a], chromosome[b] = chromosome[b], chromosome[a]
    return chromosome

def crossover(parent1, parent2):
    child = parent1[:3] + parent2[3:]
    return mutate(child) # We can use shuffling here to resolve any potential duplicate city issues

def genetic_algorithm(num_cities, num_robots, generations=1000):
    population_size = 50
    population = [create_chromosome(num_cities, num_robots) for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=lambda x: calculate_distance(x))
        new_population = [mutate(crossover(population[i], population[i+1])) for i in range(0, population_size, 2)]
        population = new_population
    return sorted(population, key=lambda x: calculate_distance(x))[0]

# Using genetic algorithm
num_cities = len(cities)
num_robots = 2
best_route = genetic_algorithm(num_cities, num_robots)

# Output results
routes = [best_route[x:x+2] for x in range(0, len(best_route), 2)]
total_cost = 0
output = []

for i, route in enumerate(routes):
    tour = [0] + route + [0]  # Assuming starting and ending at depot 0
    cost = calculate_distance(tour)
    total_cost += cost
    output.append(f"Robot {i} Tour: {tour}")
    output.append(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

output.append(f"Overall Total Travel Cost: {round(total_cost, 2)}")

for line in output:
    print(line)