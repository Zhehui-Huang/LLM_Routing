import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, randint, random

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def calculate_distance(i, j):
    return euclidean(coords[i], coords[j])

# Genetic Algorithm Parameters
num_robots = 8
num_generations = 500
population_size = 50
mutation_rate = 0.1
elite_rate = 0.2

# Initialize random tours
def initialize_population():
    population = []
    for _ in range(population_size):
        tours = sample(range(1, len(coords)), len(coords) - 1)
        splits = sorted(sample(range(1, len(coords) - 1), num_robots - 1))
        robot_tours = [tours[i:j] for i, j in zip([0] + splits, splits + [None])]
        population.append(robot_tours)
    return population

# Calculate travel cost for tours
def tour_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        tour_distance = calculate_distance(0, tour[0]) + calculate_distance(tour[-1], 0)
        for i in range(len(tour) - 1):
            tour_distance += calculate_distance(tour[i], tour[i + 1])
        costs.append(tour_distance)
        total_cost += tour_distance
    return costs, total

# Genetic operators: crossover and mutation
def crossover(p1, p2):
    # Single point crossover
    point = randint(1, len(coords) - 2)
    child = p1[:point] + [city for city in p2 if city not in p1[:point]]
    return child

def mutate(tour):
    for i in range(len(tour)):
        if random() < mutation_rate:
            j = randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]

# Genetic Algorithm core loop
population = initialize_population()
for generation in range(num_generations):
    new_population = []
    sorted_population = sorted(population, key=lambda x: tour_cost(x)[1])
    num_elites = int(population_size * elite_rate)
    elites = sorted_population[:num_elites]

    while len(new_population) < population_size:
        if len(new_population) < num_elites:
            new_population.extend(elites)
        else:
            parent1, parent2 = sample(sorted_population[:num_elites * 2], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
    population = new_population

# Extract and print the results
best_solution = sorted(population, key=lambda x: tour_cost(x)[1])[0]
costs, total_cost = tour_cost(best_solution)

# Outputting results
for idx, (tour, cost) in enumerate(zip(best_solution, costs)):
    print(f"Robot {idx} Tour: {[0] + tour + [0]}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")