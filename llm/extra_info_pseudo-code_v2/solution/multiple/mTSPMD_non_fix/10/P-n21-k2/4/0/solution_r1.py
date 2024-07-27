import numpy as np
import random
from math import sqrt

# City coordinates {(city_number): (x_coord, y_coord)}
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of depots and robots
num_depots = 2
num_robots = 2

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize population
def create_initial_population():
    cities = list(range(num_depots, len(city_coords)))
    random.shuffle(cities)
    split = len(cities) // num_robots
    partitions = [cities[i * split:(i + 1) * split] for i in range(num_robots)]
    partitions = [[0] + part for part in partitions]  # Using depot 0 for all for simplicity
    return partitions

# Evaluate a solution
def evaluate_solution(partitions):
    total_cost = 0
    detailed_cost = []
    routes = []
    for part in partitions:
        tour = part + [part[0]]  # end at the starting depot
        cost = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        detailed_cost.append(cost)
        total_cost += cost
        routes.append(tour)
    return total_cost, detailed_cost, routes

# Genetic algorithm functions (simplified)
def genetic_algorithm(max_generations=100, population_size=10):
    population = [create_initial_population() for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(max_generations):
        # Assume simple selection and mutation without crossover for simplification
        next_generation = []
        for chromo in population:
            total_cost, costs, routes = evaluate_solution(chromo)
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = (chromo, total_cost, costs, routes)
            
            # Mutation: randomly swap two cities in one robot's tour
            mutant = [part[:] for part in chromo]
            rand_robot = random.choice(mutant)
            if len(rand_robot) > 2:
                i, j = random.sample(range(1, len(rand_robot)), 2)  # avoid depot at 0
                rand_robot[i], rand_robot[j] = rand_robot[j], rand_robot[i]
            next_generation.append(mutant)
        
        population = next_generation

    return best_solution

# Execute the algorithm
best_chromosome, best_score, costs, tours = genetic_algorithm()

# Print results
for i, (cost, tour) in enumerate(zip(costs, tours)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {best_score}")