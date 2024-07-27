import numpy as np
import random
from itertools import permutations

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Genetic Algorithm constants and parameters
num_robots = 2
depot_cities = [0, 1]
mutation_rate = 0.2
population_size = 50
num_generations = 500

# Helpers and GA operators
def compute_total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_chromosome():
    cities = list(range(2, len(coordinates)))
    random.shuffle(cities)
    division = sorted(random.sample(range(1, len(cities)), num_robots - 1))
    return [cities[i:j] for i, j in zip([0]+division, division+[None])]

def crossover(parent1, parent2):
    # Order 1 Crossover as example
    child = [None]*len(parent1)
    start_pos, end_pos = sorted(random.sample(range(len(parent1)), 2))
    for i in range(start_pos, end_pos):
        child[i] = parent1[i]
    child = [item for item in child if item is not None]
    return child + [item for item in parent2 if item not in child]

def genetic_algorithm():
    population = [generate_chromosome() for _ in range(population_size)]
    for generation in range(num_generations):
        ranked_population = sorted(
            [(chromosome, sum(compute_total_distance(chromosome[robot] + [depot_cities[robot], depot_cities[robot]]) for robot in range(num_robots)))
             for chromosome in population],
            key=lambda x: x[1]
        )
        if generation % 100 == 0:
            print(f"Generation {generation}: Best score = {ranked_population[0][1]}")
        new_population = [ranked_population[i][0] for i in range(population_size//5)]  # elitism: keep top 20%
        while len(new_population) < population_size:
            parents = random.sample(ranked_population, 2)
            child1, child2 = crossover(parents[0][0], parents[1][0])
            new_population += [child1, child2]
        population = new_population
    return ranked_population[0]

final_tours = genetic_algorithm()
for i, tour in enumerate(final_tours[0]):
    print(f"Robot {i} Tour: {[depot_cities[i]] + tour + [depot_cities[i]]}")
    print(f"Robot {i} Total Travel Cost: {compute_total_distance([depot_cities[i]] + tour + [depot_cities[i]])}")

overall_cost = sum(compute_total_distance([depot_cities[i]] + final_tours[0][i] + [depot_cities[i]]) for i in range(num_robots))
print(f"Overall Total Travel Cost: {overall_cost}")