import numpy as np
import random

# Define the coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def distance(i, j):
    """ Calculate Euclidean distance between two cities with indices i and j """
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

def generate_initial_population(size, num_cities, num_robots):
    population = []
    for _ in range(size):
        cities = random.sample(range(2, num_cities), num_cities-2)  # Cities excluding depots
        # Split cities approximately in half for the two robots
        split_index = len(cities) // 2
        robot_tours = [cities[:split_index], cities[split_index:]]
        population.append(robot_tours)
    return population

def fitness(tours):
    """ Calculate the total cost of tours for all robots """
    total_cost = 0
    for i, tour in enumerate(tours):
        route = [i] + tour + [i]  # Start at depot, visit cities, return to depot
        tour_cost = sum(distance(route[j], route[j+1]) for j in range(len(route)-1))
        total_cost += tour_cost
    return total_cat

def roulette_wheel_selection(population, fitnesses):
    """ Select an individual using roulette wheel selection """
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitnesses):
        current += f
        if current > pick:
            return population[i]

def crossover(parent1, parent2):
    """ Perform a simple one-point crossover between two parent tours """
    point = random.randint(1, len(parent1[0]) - 1)
    child1_0 = parent1[0][:point] + parent2[0][point:]
    child2_0 = parent2[0][:point] + parent1[0][point:]
    return [child1_0, parent1[1]], [child2_0, parent2[1]]

def mutate(tour, mutation_rate):
    """ Mutate a tour by swapping two cities with a given probability """
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour)-1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(coordinates, num_generations=1000, population_size=50, mutation_rate=0.1):
    num_cities = len(coordinates)
    population = generate_initial_population(population_size, num_cities, 2)
    best_solution = None
    best_fitness = float('inf')
    
    for generation in range(num_generations):
        # Calculate fitness for each individual
        fitnesses = [fitness(ind) for ind in population]
        # Check for new best solution
        for i, fit in enumerate(fitnesses):
            if fit < best_fitness:
                best_fitness = fit
                best_solution = population[i]
        
        # Selection and reproduction
        new_population = []
        for _ in range(poprastructure):
            parent1 = roulette_wheel_selection(population, fitness)
            parent2 = roulette_wheel_selection(population, fitness)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        population = new_population
    
    return best_solution

# Perform the genetic algorithm
best_tours = genetic_algorithm(coordinates)