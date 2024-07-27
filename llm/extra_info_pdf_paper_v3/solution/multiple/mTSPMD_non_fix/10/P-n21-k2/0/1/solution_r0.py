import random
import math
import numpy as np

# City coordinates indexed by city number
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Distance function
def euclidean_distance(a, b):
    return math.sqrt((city_coordinates[a][0] - city_coordinates[b][0]) ** 2 + (city_coordinates[a][1] - city_coordinates[b][1]) ** 2)

# Create initial population
def create_population(pop_size, cities):
    return [random.sample(cities, len(cities)) for _ in range(pop_size)]

# Fitness function calculation
def calculate_fitness(solution):
    cost = 0
    current_city = 0
    # Start tour from depot 0, robot 0
    for city in solution:
        cost += euclidean_distance(current_city, city)
        current_city = city
    # Finish at the last city visited, no return to depot
    return cost

# Tournament selection
def tournament_selection(population, k=3):
    best = random.choice(population)
    for i in range(k - 1):
        ind = random.choice(population)
        if calculate_fitness(ind) < calculate_fitness(best):
            best = ind
    return best

# One-point crossover
def crossover(parent1, parent2):
    size = len(parent1)
    cxpoint = random.randint(1, size - 1)
    child = [None]*size
    child[0:cxpoint] = parent1[0:cxpoint]
    child[cxpoint:] = [x for x in parent2 if x not in child]
    return child

# Mutation: Swap two cities
def mutate(solution, mutation_rate=0.01):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# Genetic algorithm main routine
def genetic_algorithm(cities, pop_size=100, generations=500, mutation_rate=0.01):
    population = create_population(pop_size, cities)
    best_solution = min(population, key=calculate_fitness)

    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        current_best = min(population, key=calculate_fitness)
        if calculate_fitness(current_best) < calculate_fitness(best_solution):
            best_solution = current_best

    return best_solution

# Exclude depots and run algorithm
cities_to_visit = list(range(2, 21))
optimal_solution = genetic_algorithm(cities_to_visit)
total_cost = calculate_fitness(optimal_solution)

# Output results
print("Robot 0 Tour:", [0] + optimal_solution + [optimal_solution[-1]])
print("Robot 0 Total Travel Cost:", total_cost)
print("Overall Total Travel Cost:", total_cost)

# Note: In this simple implementation only one robot is used. Extension to multiple robots would require partitioning the cities and running a similar solution strategy for each.