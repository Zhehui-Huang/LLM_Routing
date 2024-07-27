import random
import numpy as np
from math import sqrt

# Cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two city indices. """
    return sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def initial_population(population_size, num_robots):
    """ Generates the initial population for the genetic algorithm """
    population = []
    city_indices = list(range(2, len(cities)))  # exclude depots initially
    for _ in range(population_size):
        random.shuffle(city_indices)
        # No explicit depot assignments in the chromosome; handled in the evaluation
        population.append(city_indices[:])
    return population

def calculate_costs(chromosome):
    """ Calculate the total and individual costs for a given chromosome assuming 2 robots """
    mid_point = len(chromosome) // 2  # Split point for two robots

    # Robot starting from depot city 0
    tour1 = [0] + chromosome[:mid_point]
    cost1 = sum(euclidean_distance(tour1[i], tour1[i+1]) for i in range(len(tour1)-1))

    # Robot starting from depot city 1
    tour2 = [1] + chromosome[mid_point:]
    cost2 = sum(euclidean_distance(tour2[i], tour2[i+1]) for i in range(len(tour2)-1))

    return cost1, tour1, cost2, tour2

def select_parents(costs):
    """ Select parents based on a tournament selection mechanism """
    return costs.argsort()[:2]

def crossover(parent1, parent2):
    """ Performs a simple one-point crossover """
    cut = random.randint(1, len(parent1) - 2)
    left = parent1[:cut]
    right = [i for i in parent2 if i not in left]
    return left + right

def mutate(chromosome, mutation_rate=0.05):
    """ Performs swap mutation """
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm(population_size=100, generations=500, num_robots=2, mutation_rate=0.05):
    population = initial_population(population_size, num_robots)
    
    for _ in range(generations):
        costs = np.array([calculate_costs(chromosome)[0] + calculate_costs(chromosome)[2] for chromosome in population])
        best_two_indices = select_parents(costs)
        new_population = [population[i] for i in best_two_indices]  # Keep best two
        
        while len(new_population) < population_size:
            parent1, parent2 = population[best_two_indices[0]], population[best_two_indices[1]]
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        
    # Find best solution in the final population
    best_index = np.argmin([calculate_costs(chromosome)[0] + calculate_costs(chromosome)[2] for chromosome in population])
    best_chromosome = population[best_index]
    cost1, tour1, cost2, tour2 = calculate_costs(best_chromosome)

    return tour1, cost1, tour2, cost2

# Run the genetic algorithm
tour1, cost1, tour2, cost2 = genetic_algorithm()

print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", cost1)
print("\nRobot 1 Tour:", tour2)
print("Robot 1 Total Travel Cost:", cost2)
print("\nOverall Total Travel Cost:", cost1 + cost2)