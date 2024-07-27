import numpy as np
import random

# City coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

num_cities = len(coordinates)
num_robots = 2
depot_indices = {0: 0, 1: 1}

# Calculate Euclidean distances
def calculate_distances():
    dist = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist[i, j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + 
                                 (coordinates[i][1] - coordinates[j][1])**2)
    return dist

distances = calculate_veuclidean_distances()

# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.05
generations = 300

# Function to create a random tour for genomes
def create_random_genome():
    nodes = list(range(2, num_cities))  # Exclude depots
    random.shuffle(nodes)
    # Partitions (assign random breakpoint for generating two tours)
    break_idx = random.randint(1, len(nodes) - 1)
    return nodes[:break_idx], nodes[break_idx:]

# Total distance for each robot
def calculate_tour_cost(tour, depot):
    total_cost = 0
    start = depot
    for node in tour:
        total_cost += distances[start, node]
        start = node
    total_cost += distances[start, depot]
    return total_cost

# Genetic operators
def crossover(parent1, parent2):
    """Perform a two-point crossover and repair the offspring."""
    child1, child2 = list(parent1), list(parent2)
    cross_pts = sorted(random.sample(range(len(parent1)), 2))
    child1[cross_pts[0]:cross_pts[1]] = parent2[cross_pts[0]:cross_pts[1]]
    child2[cross_pts[0]:cross_pts[1]] = parent1[cross_pts[0]:cross_pts[1]]
    return [repair_tour(child1, parent1, parent2), repair_tour(child2, parent2, parent1)]

def repair_tour(child, parent1, parent2):
    """Repair the crossed-over child."""
    to_replace = [x for x in parent1 if x not in child]
    used = set(child)
    child_repaired = [x if x in used else to_provide.pop(0) for x in child]
    return child_repaired

def mutate(genome):
    """Perform mutation by swapping two cities."""
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(genome)), 2)
        genome[idx1], genome[idx2] = genome[idx2], genome[idx1]
    return genome

# Initial population
population = [create_random_genome() for _ in range(population_size)]

# Placeholder for the evolutionary loop - needs to be expanded based on GA properties
# This is a high-complexity challenge; further coding will be based on the progress and directions.

# Assume the evolved solution is stored in `final_population` after the GA run
# Extract tours from the best solution obtained from GA
final_tours = [final_population[0][:break_idx_final), final_population[0][break_idx_final:]]
final_costs = [calculate_tour_cost(final_tours[0], depot_indices[0]), calculate_tour_cost(final_tours[1], depot_indices[1])]
overall_cost = sum(final_costs)

print("Robot 0 Tour: [0] + final_tours[0] + [0]")
print("Robot 0 Total Travel Cost:", final_costs[0])
print("Robot 1 Tour: [1] + final_tours[1] + [1]")
print("Robot 1 Total Travel Cost:", final_costs[1])
print("Overall Total Travel Cost:", overall_cost)