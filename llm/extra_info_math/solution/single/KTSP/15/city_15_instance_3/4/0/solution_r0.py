import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the coordinates for the depot and cities
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

num_cities = len(coordinates)

# Compute the Euclidean distance matrix
distance_matrix = [[euclidean(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Parameters for the Genetic Algorithm
population_size = 100
num_generations = 500
mutation_rate = 0.2
tour_size = 10  # Number of cities to include in the tour

def generate_chromosome():
    """ Generate a valid chromosome. """
    chromosome = random.sample(range(1, num_cities), tour_size-1)
    chromosome.insert(0, 0)  # Start at the depot
    chromosome.append(0)     # End at the depot
    return chromosome

def calculate_tour_length(chromosome):
    """ Calculate the total length of the tour defined by this chromosome. """
    return sum(distance_matrix[chromosome[i]][chromosome[i+1]] for i in range(len(chromosome)-1))

def crossover(parent1, parent2):
    """ Perform ordered crossover between two parents. """
    start, end = sorted(random.sample(range(1, tour_size-1), 2))
    child = [None]*tour_size
    child[start:end+1] = parent1[start:end+1]
    
    child_set = set(child[start:end+1])
    fill_idx = 0
    for gene in parent2:
        if gene not in child_set:
            while child[fill_idx] is not None:
                fill_idx += 1
            child[fill_idx] = gene
    
    child[0] = 0
    child[-1] = 0
    return child

def mutate(chromosome):
    """ Mutate a chromosome by swapping two cities. """
    idx1, idx2 = sorted(random.sample(range(1, tour_size-1), 2))
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Generate initial population
population = [generate_chromosome() for _ in range(population * size)]

# Evolution process
for generation in range(num_generations):
    # Evaluate population
    fitness_scores = [(chromosome, calculate_tour_length(chromosome)) for chromosome in population]
    # Selection
    sorted_population = sorted(fitness_scores, key=lambda x: x[1])
    population = [x[0] for x in sorted_population[:population_size // 2]]  # Elitism

    new_population = population.copy()
    while len(new_population) < population_size:
        if random.random() < mutation_rate:
            # Mutation
            offspring = mutate(random.choice(population).copy())
        else:
            # Crossover
            parent1, parent2 = random.sample(population, 2)
            offspring = crossover(parent1, parent2)

        new_population.append(offspring)

    population = new_population

# Get the best solution
best_solution = sorted([(chromosome, calculate_tour_length(chromosome)) for chromosome in population], key=lambda x: x[1])[0]

print(f"Tour: {best_answer[0]}")
print(f"Total travel cost: {best_answer[1]}")