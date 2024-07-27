import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate initial population
def create_initial_population():
    population = []
    for _ in range(pop_size):
        chromo = list(cities.keys())[1:]  # Exclude depots
        random.shuffle(chromo)
        # Insert depots and separators for robots
        for i in range(1, num_robots):
            chromo.insert(random.randint(1, len(chromo)), -1)
        chromo.insert(0, 0)  # Start at depot 0
        population.append(chromo)
    return population

# Calculate fitness (total distance of the tours)
def fitness(chromosome):
    total_distance = 0
    current_city = 0  # starts at depot 0
    for gene in chromosome:
        if gene >= 0:
            total_distance += calculate_distance(current_city, gene)
            current_city = gene
        else:
            # Transition to new robot starting at depot 0
            total_distance += calculate_distance(current_city, 0)
            current_city = 0
    total_distance += calculate_distance(current_city, 0)  # Return to depot (not needed per task, but here for completeness)
    return total_distance

# Genetic Algorithm Configuration
num_robots = 2
pop_size = 50
G_max = 100
mutation_rate = 0.1

# Genetic algorithm main loop
def genetic_algorithm():
    population = create_initial_population()
    best_distance = float('inf')
    best_solution = None
    
    for _ in range(G_max):
        population = sorted(population, key=fitness)
        if fitness(population[0]) < best_distance:
            best_distance = fitness(population[0])
            best_solution = population[0]
        
        new_population = population[:10]  # Elitism: top 20% goes to next gen
        
        # Crossover (80% of next gen)
        while len(new_population) < pop_size * 0.9:
            p1, p2 = random.sample(population[:20], 2)  # Tournament selection
            child = crossover(p1, p2)
            new_population.append(child)
        
        # Mutation (10% of next gen)
        while len(new_population) < pop_size:
            mutant = mutate(random.choice(population))
            new_population.append(mutant)

        population = new_population

    return best_solution, best_distance

# Crossover function (simple one point crossover)
def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + [gene for gene in parent2 if gene not in parent1[:cut]]
    return child

# Mutation function
def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Run the genetic algorithm and print results
best_tour, best_cost = genetic_algorithm()

# Printing the tour in required format
print("Best Tour:", best_tour)
print("Best Total Travel Cost:", best_cost)