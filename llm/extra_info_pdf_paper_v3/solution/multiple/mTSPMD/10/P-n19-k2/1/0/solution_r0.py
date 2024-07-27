import numpy as np
import math
import random

# Cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Number of robots
num_robots = 2

# Depot assignments
depots = [0, 1]

# Fitness evaluation of one genome
def fitness(genome):
    tours = decode_genome(genome)
    total_cost = sum(calculate_tour_cost(tour) for tour in tours)
    return total_cost

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Decode genome into separate tours for each robot
def decode_genome(genome):
    # Split points are where the genome switches from one robot's route to another
    split_points = sorted(random.sample(range(2, 17), num_robots-1))
    parts = np.split(genome, split_points)
    tours = [[depots[i]] + list(part) + [depots[i]] for i, part in enumerate(parts)]
    return tours

# Crossover - Ordered Crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    child = [item for item in parent2 if item not in child[start:end]] + child
    child = child[size:] + child[:size]
    return child

# Mutation - 2-opt
def mutate(genome):
    start, end = sorted(random.sample(range(len(genome)), 2))
    genome[start:end] = reversed(genome[start:end])

# Genetic Algorithm core
def genetic_algorithm(population_size=100, generations=500):
    # Initialize population
    population = [random.sample(range(2, 19), 17) for _ in range(population_size)]
    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = [fitness(genome) for genome in population]
        next_generation = []
        # Elite selection
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
        next_generation.extend(sorted_population[:2])  # Elitism
        # Crossover and mutation
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(sorted_population[:50], 2)  # Tournament selection
            child = crossover(parent1, parent_type)
            if random.random() < 0.1:  # Mutation chance
                mutate(child)
            next_generation.append(child)
        population = next_generation
    # Best solution
    best_solution = min(population, key=fitness)
    return decode_genome(best_solution)

# Run the algorithm
solution_tours = genetic_algorithm()
costs = [calculate_tour_cost(tour) for tour in solution_tours]
overall_cost = sum(costs)

# Output solution
for i, tour in enumerate(solution_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")