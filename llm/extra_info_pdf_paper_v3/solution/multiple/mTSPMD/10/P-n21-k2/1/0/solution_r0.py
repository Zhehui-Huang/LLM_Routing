import numpy as
import random
from scipy.spatial import distance
from itertools import permutations

# City coordinates provided
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

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Examples of chromosomal representation for robots
# Example - Chromosome: [2, 1, 3, 2, 0, 0, 1, 0], where numbers represent city IDs

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

def genetic_algorithm():
    # Initialize population
    num_cities = len(cities)
    population_size = 100
    num_generations = 1000
    mutation_rate = 0.1
    population = [random.sample(range(2, num_cities), num_cities - 2) for _ in range(population_size)]
    
    # Evaluate fitness
    for generation in range(num_generations):
        fitness = []
        for individual in population:
            tour0 = [0] + individual[:10] + [0]
            tour1 = [1] + individual[10:] + [1]
            cost0 = calculate_total_distance(tour0)
            cost1 = calculate_total_distance(tour1)
            total_cost = cost0 + cost1
            fitness.append((individual, total_cost))
        
        # Selection
        population = sorted(fitness, key=lambda x: x[1])
        best_individuals = [x[0] for x in population[:population_size // 2]]
        
        # Crossover and Mutation
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(best_individuals, 2)
            # Implementing Ordered Crossover (OX)
            child = crossover(parent1, parent2)
            # Mutation
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        
        population = new_population
        
    # Best solution
    best_solution = sorted(fitness, key=lambda x: x[1])[0]
    tour0 = [0] + best_solution[0][:10] + [0]
    tour1 = [1] + best_solution[0][10:] + [1]
    cost0 = calculate_total_distance(tour0)
    cost1 = calculate_total_distance(tour1)

    return tour0, cost0, tour1, cost1

# Placeholder functions for crossover and mutation
def crossover(parent1, parent2):
    # Actual crossover logic to be implemented
    return parent1

def mutate(individual):
    # Actual mutation logic to be implemented
    return individual

# Running the genetic algorithm
tour0, cost0, tour1, cost1 = genetic_algorithm()
overall_cost = cost0 + cost1

print("Robot 0 Tour:", tour0)
print("Robot 0 Total Travel Cost:", cost0)
print("Robot 1 Tour:", tour1)
print("Robot 1 Total Travel Cost:", cost1)
print("Overall Total Travel Cost:", overall_cost)