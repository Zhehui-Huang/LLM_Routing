import numpy as np
import random
from scipy.spatial.distance import euclidean

def calc_distance(city1, city2):
    return euclidean(city1, city2)

def initialize_population(size, cities):
    population = []
    for _ in range(size):
        random.shuffle(cities)
        population.append(list(cities))
    return population

def calculate_total_distance(tour, coords):
    total = 0
    for i in range(len(tour) - 1):
        total += calc_distance(coords[tour[i]], coords[tour[i+1]])
    total += calc_distance(coords[tour[-1]], coords[tour[0]])
    return total

def fitness(chromosome, coords, depot_id):
    # Create tour starting and ending at the depot
    tour = [depot_id] + list(chromosome) + [depot_id]
    return calculate_total_distance(tour, coords)

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

def genetic_algorithm_per_robot(coords, cities, depot_id, population_size=50, generations=100):
    population = initialize_population(population_size, cities)
    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, coords, depot_id))
        next_generation = population[:2]  # elitism: keep best 2
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)  # tournament
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)
        population = next_generation
    best = sorted(population, key=lambda x: fitness(x, coords, depot_id))[0]
    best_cost = fitness(best, coords, depot_id)
    best_tour = [depot_id] + best + [depot_id]
    return best_tour, best_cost

# Defining coordinates and depot indices
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

depots = [0, 1, 2, 3, 4, 5, 6, 7]
total_travel_cost = 0

# Run the genetic algorithm for each depot
for depot_id in depots:
    cities = [i for i in range(len(coords)) if i not in depots]
    tour, tour_cost = genetic_algorithm_per_robot(coords, cities, depot_id)
    total_travel_cost += tour_cost
    print(f"Robot {depot_id - depots[0]} Tour: {tour}")
    print(f"Robot {depop_id - depots[0]} Total Travel Cost: {tour_cost}\n")

print(f"Overall Total Travel Cost: {total_travel_cost}")