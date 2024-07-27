import numpy as np
import random
from math import sqrt
from copy import deepcopy

# Coordinates of the cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Initialize the number of robots
num_robots = 8

# Create individual as a list of cities to visit
def create_individual():
    cities_to_visit = list(cities.keys())[1:]  # All cities except the depot
    random.shuffle(cities_to_visit)
    return cities_to_visit

# Calculate the cost of the given tours
def calculate_cost(tours):
    cost = 0
    for tour in tours:
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        cost += tour_cost
    return cost

# Genetic algorithm setup
def genetic_algorithm():
    population_size = 100
    num_generations = 500
    mutation_rate = 0.1
    elite_size = 10

    # Initialize the population with random individuals
    population = [create_individual() for _ in range(population_size)]
    best_cost = float('inf')
    best_solution = None
    
    for _ in range(num_generations):
        # Rank individuals by their cost
        sorted_population = sorted(population, key=lambda ind: calculate_cost([ind]))
        # Select the elite individuals
        elites = sorted_population[:elite_size]
        
        # Create the next generation
        next_gen = deepcopy(elites)
        while len(next_gen) < population_size:
            if random.random() < mutation_rate:
                mutate(next_gen)
            else:
                ind1, ind2 = random.sample(elites, 2)
                child = crossover(ind1, ind2)
                next_gen.append(child)
        
        population = next_gen
        
        # Check for new best solution
        current_best, current_cost = sorted_population[0], calculate_cost([sorted_population[0]])
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best

    return best_solution, best_cost

# Crossover two individuals to produce a child
def crossover(parent1, parent2):
    # Single point crossover
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

# Mutate an individual by swapping two cities in the tour
def mutate(population):
    for individual in population:
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(individual)), 2)
            individual[i], individual[j] = individual[j], individual[i]

# Run the genetic algorithm for our mTSP
best_tour, best_cost = genetic_algorithm()
print("Best tour found:", [0] + best_tour + [0])
print("Cost of the best tour:", best_cost)