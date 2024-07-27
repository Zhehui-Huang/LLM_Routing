import numpy as np
import random
from itertools import permutations

# City Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance calculation
def calc_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Genetic Algorithm Components

def generate_initial_population(size, cities):
    population = []
    for _ in range(size):
        route = random.sample(cities, len(cities))
        population.append(route)
    return population

def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += calc_distance(solution[i], solution[i + 1])
    total_distance += calc_distance(solution[-1], solution[0])  # Return to starting city
    return 1 / total_distance

def select_parents(population, fitnesses, k=5):
    selected = random.choices(population, weights=fitnesses, k=k)
    return sorted(selected, key=lambda x: calculate_fitness(x), reverse=True)[:2]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(cities, iterations=100, population_size=50, mutation_rate=0.1):
    population = generate_initial_population(population_size, cities)
    fitnesses = [calculate_fitness(individual) for individual in population]
    
    for _ in range(iterations):
        new_population = []
        for _ in range(len(population)):
            parent1, parent2 = select_parents(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        fitnesses = [calculate_fitness(individual) for individual in population]
        
    best_route = max(population, key=lambda x: calculate_fitness(x))
    return best_route

# Splitting cities between two robots
cities = list(range(2, 19)) # All cities excluding depots
random.shuffle(cities)
middle_index = len(cities) // 2
robot_0_cities = [0] + cities[:middle_index] + [0]
robot_1_cities = [1] + cities[middle_index:] + [1]

# Solve using Genetic Algorithm for each robot
robot_0_tour = genetic_algorithm(robot_0_cities, iterations=500, population_size=100)
robot_1_tour = genetic_algorithm(robot_1_cities, iterations=500, population_size=100)

# Calculating costs
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

robot_0_cost = tour_cost(robot_0_tour)
robot_1_cost = tour_cost(robot_1_tour)
overall_cost = robot_0_cost + robot_1_cost

print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", overall_cost)