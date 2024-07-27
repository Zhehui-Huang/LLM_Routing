import numpy as np
import random
import math
from scipy.spatial.distance import euclidean

# Coordinates of the cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def get_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize a population of solutions
def initialize_population(pop_size, num_cities):
    return [random.sample(range(2, num_cities), num_cities - 2) for _ in range(pop_size)]

# Calculate the total distance of the tours
def calculate_fitness(individual):
    # Calculate robot 0 tour from depot 0
    robot0_tour = [0] + individual[:len(individual)//2] + [0]
    robot1_tour = [1] + individual[len(individual)//2:] + [1]
    
    total_distance = 0
    # Calculate distance for robot 0
    for i in range(len(robot0_tour) - 1):
        total_distance += get_distance(robot0_tour[i], robot0_tour[i+1])

    # Calculate distance for robot 1
    for i in range(len(robot1_tour) - 1):
        total_distance += get_distance(robot1_tour[i], robot1_tour[i+1])
    
    return total_distance, robot0_tour, robot1_tour

# Genetic algorithm functions: crossover, mutation
def crossover(parent1, parent2, crossover_rate=0.8):
    if random.random() < crossover_rate:
        point1, point2 = sorted(random.sample(range(len(parent1)), 2))
        child = [None] * len(parent1)
        child[point1:point2] = parent1[point1:point2]
        fill = [item for item in parent2 if item not in child]
        fill_pointer = 0
        for i in range(len(child)):
            if child[i] is None:
                child[i] = fill[fill_pointer]
                fill_pointer += 1
        return child
    return parent1[:]  # return a copy of parent1 if no crossover

def mutate(individual, mutation_rate=0.2):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Run the Genetic Algorithm
def genetic_algorithm(pop_size, num_generations):
    population = initialize_population(pop_size, len(cities))
    best_solution = None
    best_distance = float('inf')

    for generation in range(num_generations):
        new_population = []
        for i in range(pop_size):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        
        # Evaluate the new population
        population = sorted(new_population, key=lambda x: calculate_fitness(x)[0])
        
        # Keep the best solution
        current_best_distance, robot0_tour, robot1_tour = calculate_fitness(population[0])
        if current_best_distance < best_distance:
            best_distance = current_best_distance
            best_solution = population[0]

    return calculate_fitness(best_solution)


# Settings
pop_size = 100
num_generations = 500

# Run GA
best_distance, robot0_tour, robot1_tour = genetic_algorithm(pop_size, num_generations)

# Compute individual costs
robot0_cost = sum(get_distance(robot0_tour[i], robot0_tour[i+1]) for i in range(len(robot0_tour)-1))
robot1_cost = sum(get_distance(robot1_tour[i], robot1_tour[i+1]) for i in range(len(robot1_tour)-1))

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", robot0_cost + robot1_cost)