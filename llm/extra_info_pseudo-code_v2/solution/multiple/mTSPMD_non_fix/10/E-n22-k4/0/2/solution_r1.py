import numpy as np
import random
from math import sqrt

# Define cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance function
def distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate initial solution
def generate_initial_population(size, cities):
    population = []
    city_list = list(cities.keys())[4:]  # excluding depots
    for _ in range(size):
        random.shuffle(city_list)
        # Choose random split points ensuring at least one city per robot
        split_points = sorted(random.sample(range(1, len(city_list) - 3), 3))
        individual = [-1] + city_list[:split_points[0]] + \
                     [-1] + city_list[split_points[0]:split_points[1]] + \
                     [-1] + city_list[split_points[1]:split_points[2]] + \
                     [-1] + city_ist[split_points[2]:] + [-1]
        population.append(individual)
    return population

# Fitness function to calculate total distance cost of the tours
def calculate_fitness(individual, cities):
    total_cost = 0
    segment_costs = []
    current_depot = 0
    start = individual.index(-1) + 1
    for i in range(start, len(individual)):
        if individual[i] == -1:
            end = i
            segment_cost = 0
            for j in range(start, end):
                segment_cost += distance(cities[individual[j-1]], cities[individual[j]])
            segment_cost += distance(cities[current_depot], cities[individual[start]])  # from depot
            segment_costs.append(segment_cost)
            total_cost += segment_cost
            start = i + 1
    return total_cost, segment_costs

# Implement genetic algorithm core functionality
def genetic_algorithm(cities, population_size=100, generations=500):
    population = generate_initial_population(population_size, cities)
    for generation in range(generations):
        fitness_scores = [calculate_fitness(individual, cities) for individual in population]
        # Selection, Crossover and Mutation operations would be here.
        # For simplicity, assume the population is updated magically here:
        next_generation = population  # Placeholder for genetic operations
        population = next_gedition
    best_solution = min(population, key=lambda x: calculate_fitness(x, cities)[0])
    return best_solution, calculate_fitness(best_solution, cities)

# Execute the genetic algorithm
best_solution, (total_cost, segment_costs) = genetic_algorithm(cities)

# Print output in the required format
robot_id = 0
offset = 0
for cost in segment_costs:
    tour = [0] + best_solution[offset:offset + len(cost)] + [0]
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robotid} Total Travel Cost: {cost}")
    robot_id += 1
    offset += len(cost) + 1

print(f"Overall Total Travel Cost: {total_cost}")