import numpy as np
import math
import random

# Define coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance function using Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Genetic Algorithm Functions
def init_population(pop_size, genome_length):
    return [random.sample(range(2, 19), genome_length - 2) for _ in range(pop_size)]

def decode_genome(genome):
    split = 4  # Chosen arbitrarily, here 0 to 3 for robot 1; 4 to 17 for robot 2
    return [genome[:split], genome[split:]]

def calculate_total_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def fitness(genome):
    tours = decode_genome(genome)
    tour_costs = [calculate_total_distance([0] + tour + [0]) for tour in tours]
    tour_costs += [calculate_total_distance([1] + tour + [1]) for tour in tours]
    return sum(tour_costs), tours, tour_costs

def selection(population, scores):
    population_scores = list(zip(population, scores))
    sorted_population_scores = sorted(population_scores, key=lambda x: x[1])
    return [genome for genome, score in sorted_population_scores[:len(population)//2]]

def crossover(parent1, parent2):
    size = len(parent1)
    child = parent1[:size//2] + parent2[size//2:]
    fix(child)
    return child

def mutate(genome):
    index1, index2 = random.sample(range(len(genome)), 2)
    genome[index1], genome[index2] = genome[index2], genome[index1]

def fix(genome):
    # Ensure no duplicate cities are in the genome
    unique_genes = list(set(range(2, 19)))
    for gene in unique_genes:
        while genome.count(gene) > 1:
            genome[genome.index(gene)] = random.choice([x for x in unique_genes if x not in genome])

# Genetic algorithm
def genetic_algorithm():
    population_size = 100
    generations = 100
    genome_length = 17

    pop = init_population(population_size, genome_length)

    for _ in range(generations):
        pop_fitness = [fitness(genome)[0] for genome in pop]
        selected_pop = selection(pop, pop_fitness)
        next_gen = []
        while len(next_gen) < population_size:
            p1, p2 = random.sample(selected_pop, 2)
            child = crossover(p1, p2)
            if random.random() < 0.1:  # Chance of mutation
                mutate(child)
            next_gen.append(child)
        pop = next_gen

    best_genome = min(pop, key=lambda g: fitness(g)[0])
    best_score, best_tours, tour_costs = fitness(best_genome)
    return best_tours, tour_costs, best_score

# Run the genetic algorithm
best_tours, tour_costs, best_score = genetic_algorithm()

# Output results
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {[depots[i]] + tour + [depot[i]]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")
print(f"Overall Total Travel Cost: {best_score}")