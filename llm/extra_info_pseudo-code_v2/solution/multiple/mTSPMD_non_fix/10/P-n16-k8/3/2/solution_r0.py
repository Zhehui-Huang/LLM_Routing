import numpy as np
import random
import math
from itertools import permutations

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Parameters
num_cities = len(cities)
num_robots = 8
depot_index = 0  # Starting depot index for all robots
pop_size = 50
G_max = 500
crossover_rate = 0.7
mutation_rate = 0.1

# Function to calculate Euclidean distance
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Cost evaluation function
def total_route_cost(route):
    total_cost = 0
    for i in range(1, len(route)):
        total_cost += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return total_cost

# Generate initial population
def generate_initial_population():
    population = []
    base_permutation = list(range(1, num_cities))
    random.shuffle(base_permutation)

    for _ in range(pop_size):
        perm = base_permutation[:]
        partitions = sorted(random.sample(range(1, len(perm)), num_robots - 1))
        chromosome = [0] + perm[:partitions[0]]

        for i in range(1, len(partitions)):
            chromosome += [0] + perm[partitions[i-1]:partitions[i]]

        chromosome += [0]
        population.append(chromosome)
    return population

# Genetic operations
def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(chromosome) - 1), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(parent1) - 1), 2))
        middle1 = parent1[idx1:idx2]
        part2 = [item for item in parent2 if item not in middle1]
        return part2[:idx1] + middle1 + part2[idx1:]
    return parent1

# Genetic algorithm
def genetic_algorithm():
    population = generate_initial_population()
    best_solution = min(population, key=total_route_cost)
    best_cost = total_route_cost(best_solution)

    for _ in range(G_max):
        new_population = []
        for _ in range(pop_size):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
            child_cost = total_route_cost(child)
            if child_cost < best_cost:
                best_cost = child_cost
                best_solution = child
        population = new_population

    return best_solution, best_cost

# Execute the GA and print results
best_solution, best_cost = genetic_algorithm()
print("Optimal tours and their costs:")
current_robot = 0
start_index = 0

for i in range(1, len(best_solution)):
    if best_solution[i] == 0:
        tour = best_solution[start_index:i + 1]
        cost = total_route_cost(tour)
        print(f"Robot {current_robot} Tour: {tour}")
        print(f"Robot {current_robot} Total Travel Cost: {cost:.2f}")
        start_index = i
        current_robot += 1
        if current_robot == num_robots:
            break

print(f"Overall Total Travel Cost: {best_cost:.2f}")