import numpy as np
import random
from scipy.spatial import distance_matrix

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

num_cities = len(cities)
coords = np.array(list(cities.values()))

# Calculate distance matrix
dist_matrix = distance_matrix(coords, coords)

# Robot and GA settings
num_robots = 8
pop_size = 100
G_max = 1000
cr = 0.7
mr = 0.2

def initialize_population():
    population = []
    for _ in range(pop_size):
        perm = np.random.permutation(num_cities)
        splits = sorted(random.sample(range(1, num_cities), num_robots - 1))
        chromosome = []
        prev = 0
        for split in splits:
            chromosome.extend(perm[prev:split])
            chromosome.append(-1)  # Insert depot separator
            prev = split
        chromosome.extend(perm[prev:num_cities])
        population.append(chromosome)
    return population

def calculate_cost(tour):
    cost = 0
    if len(tour) > 1:
        for i in range(len(tour)-1):
            cost += dist_matrix[tour[i], tour[i+1]]
    return cost

def evaluate_chromosome(chromosome):
    tours = []
    tour = [0]  # Robot's start position, assuming all start at depot 0
    costs = []
    total_cost = 0
    for gene in chromosome:
        if gene == -1:
            tour.append(0)
            cost = calculate_cost(tour)
            costs.append(cost)
            total_cost += cost
            tours.append(tour)
            tour = [0]  # restart at depot
        else:
            tour.append(gene)
    return tours, costs, total_cost

# Example of initializing and evaluating a population
population = initialize_population()
tours, costs, total_cost = evaluate_chromosome(population[0])

# Output example
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_cost}")