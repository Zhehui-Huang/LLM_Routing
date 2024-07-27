import numpy as np
import random
from math import sqrt

def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities_coordinates = [
    (30, 40), (37, 52), # Depot 0, Depot 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
num_robots = 2
num_cities = len(cities_coordinates) - num_robots  # Subtracting depots

# Genetic Algorithm settings
population_size = 100
num_generations = 500
mutation_rate = 0.15
tournament_size = 5

# Initialize population
def create_individual():
    """ Create a feasible tour for all robots starting from their respective depots. """
    cities = list(range(2, len(cities_coordinates)))  # Cities without depots
    random.shuffle(cities)
    point_of_split = random.randint(1, len(cities) - 1)
    return [0] + cities[:point_of_split] + [0] + [1] + cities[point_of_split:] + [1]

population = [create_individual() for _ in range(population_size)]

def fitness(individual):
    """ Calculate the total distance of the tour. Lower distance has better fitness. """
    total_dist = 0
    for i in range(len(individual) - 1):
        total_dist += distance(cities_coordinates[individual[i]], cities_coordinates[individual[i + 1]])
    return total_dist

def crossover(parent1, parent2):
    """ Create a child by partial crossover of the parent tours. """
    half = len(parent1) // 2
    child = parent1[:half] + [x for x in parent2 if x not in parent1[:half]]
    return child if len(child) == len(parent1) else parent1

def mutate(individual):
    """ Mutate an individual by swapping two cities in the tour. """
    idx1, idx2 = random.sample(range(1, len(individual) - 1), 2)  # avoid swapping depots
    if individual[idx1] != 0 and individual[idx2] != 1:
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def tournament_selection(pop):
    """ Select the best individual among `tournament_size` randomly picked. """
    tournament = random.sample(pop, tournament_size)
    best = min(tournament, key=fitness)
    return best

# Execute Genetic Algorithm
for generation in range(num_generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        if random.random() < mutation_rate:
            mutate(parent1)
            mutate(parent2)

        child = crossover(parent1, parent2)
        new_population.append(child)

    population = new_population[:]

# Find the best solution 
best_tour = min(population, key=fitness)
best_cost = fitness(best_tour)

# Output the tours and costs
separator = best_tour.index(1)
tour_robot_0 = best_tour[:separator+1]
tour_robot_1 = best_tour[separator:]

cost_robot_0 = sum(distance(cities_coordinates[tour_robot_0[i]], cities_coordinates[tour_robot_0[i + 1]]) 
                   for i in range(len(tour_robot_0) - 1))
cost_robot_1 = sum(distance(cities_coordinates[tour_robot_1[i]], cities_coordinates[tour_robot_1[i + 1]]) 
                   for i in range(len(tour_robot_1) - 1))

print("Robot 0 Tour:", tour_robot_0)
print("Robot 0 Total Travel Cost:", cost_robot_0)
print("Robot 1 Tour:", tour_robot_1)
print("Robot 1 Total Travel Cost:", cost_robot_1)
print("Overall Total Travel Cost:", cost_robot_0 + cost_robot_1)