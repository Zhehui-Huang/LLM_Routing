import numpy as np
from scipy.spatial.distance import euclidean
import random

# City Coordinates (including depots)
cities = [
    (30, 40), # Depot for Robot 0
    (37, 52), # Depot for Robot 1
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

def fitness(tour):
    """ Calculate total distance of the tour including return to start """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean(cities[tour[i-1]], cities[tour[i]])
    # Return to depot
    total_cost += euclidean(cities[tour[-1]], cities[tour[0]])
    return total_cost

def create_initial_population(size, pool):
    """ Create the initial population """
    population = []
    for _ in range(size):
        individual = random.sample(pool, len(pool))
        population.append(individual)
    return population

def crossover(parent1, parent2):
    """ Perform partially matched crossover """
    n = len(parent1)
    child = [-1]*n
    start, end = sorted(random.sample(range(n), 2))
    child[start:end] = parent1[start:end]
    for i in range(start, end):
        value = parent2[i]
        while value in child:
            index = child.index(parent2[child.index(value)])
            value = parent2[index]
        child[child.index(-1)] = value
    return child

def mutate(individual, mutation_rate):
    """ Perform swap mutation """
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

def ga_solver(cities, num_generations=100, population_size=100, mutation_rate=0.05):
    # Initial setup
    depots = [[0], [1]]
    city_indices = list(range(2, len(cities)))
    populations = [create_initial_population(population_size, city_indices) for _ in depots]

    for generation in range(num_generations):
        for depot_index, population in enumerate(populations):
            new_population = []
            sorted_population = sorted(population, key=fitness)
            # Elitism: carry forward the best individual
            new_population.append(sorted_population[0])
            
            for _ in range(population_size - 1):
                parent1 = random.choice(sorted_population[:len(sorted_population)//2])
                parent2 = random.choice(sorted_population[:len(sorted_instruction)//2])
                child = crossover(parent1, parent2)
                mutate(child, mutation_rate)
                new_population.append(child)
            
            populations[depot_index] = new_population

    # Get best tour for each robot
    tours = []
    costs = []
    total_cost = 0
    for depot_index, population in enumerate(populations):
        best = min(population, key=fitness)
        full_tour = depots[depot_index] + best + depots[depot_index]
        cost = fitness(full_tour)
        tours.append(full_tour)
        costs.append(cost)
        total_cost += cost

    return tours, costs, total_cost

# Setting parameters
num_generations = 500
population_size = 50
mutation_rate = 0.02

# Solving the problem
tours, costs, total_cost = ga_solver(cities, num_generations, population_size, mutation_rate)

for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour:", tour)
    print(f"Robot {i} Total Travel Cost:", cost)
print("Overall Total Travel Cost:", total_cost)