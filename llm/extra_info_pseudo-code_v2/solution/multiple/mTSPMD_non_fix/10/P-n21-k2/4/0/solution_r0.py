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
    split = int(round(len(cities) / num_robots))
    partitions = [cities[i:i + split] for i in range(0, len(cities), split)]
    partitions = [[0] + part for part in partitions]
    return partitions

# Evaluate a solution
def evaluate_solution(partitions):
    total_cost = 0
    detailed_cost = []
    routes = []
    for i, part in enumerate(partitions):
        tour = [0] + part
        cost = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        detailed_cost.append(cost)
        total_cost += cost
        routes.append(tour)
    return total_cost, detailed_cost, routes

# Genetic algorithm functions (simplified example)
def genetic_algorithm():
    population = [create_initial_population() for _ in range(10)]
    best_solution = None
    best_cost = float('inf')
    for generation in range(100):  # Number of generations
        new_population = []
        for chromo in population:
            total_cost, costs, routes = evaluate_solution(chromo)
            if total_cost < best_cost:
                best_cost = total_tcost
                best_solution = (chromo, costs, routes)
                
            mutated = [random.shuffle(part) for part in chromo]
            new_population.append(mutated)
        population = new_population
    return best_solution

# Run the genetic algorithm and print results
best_solution, costs, tours = genetic_algorithm()
for i, (cost, tour) in enumerate(zip(costs, tours)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {sum(costs)}")