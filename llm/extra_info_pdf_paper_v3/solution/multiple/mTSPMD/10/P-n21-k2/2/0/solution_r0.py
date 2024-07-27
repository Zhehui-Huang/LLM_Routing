import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the coordinates of each city
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance calculation
def calculate_distance(city1, city2):
    return euclidean(coords[city1], coords[city2])

# Initial random solution generation
def generate_initial_solution(depot1, depot2, cities):
    random.shuffle(cities)
    half = len(cities) // 2
    return [depot1] + cities[:half] + [depot1], [depot2] + cities[half:] + [depot2]

# Fitness evaluation function
def evaluate_solution(route):
    cost = sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))
    return cost

# Mutation function: simple 2-opt mutation
def mutate(route):
    i, j = sorted(random.sample(range(1, len(route) - 1), 2))
    route[i:j] = reversed(route[i:j])

# Genetic Algorithm main function
def genetic_algorithm(num_iterations=1000):
    cities = list(coords.keys())
    cities.remove(0)
    cities.remove(1)
    best_solution = None
    best_cost = float('inf')

    # Random initial solutions
    robot1_route, robot2_route = generate_initial_solution(0, 1, cities)
    for _ in range(num_iterations):
        if random.random() < 0.1:  # Mutation chance
            mutate(robot1_route)
            mutate(robot2_route)
        
        # Evaluate new solution
        cost1 = evaluate_solution(robot1_route)
        cost2 = evaluate_solution(robot2_route)
        total_cost = cost1 + cost2

        # Selection mechanism
        if total_cost < best_cost:
            best_solution = (robot1_route.copy(), robot2_route.copy())
            best_cost = total_cost
    
    return best_solution, best_cost

# Run the Genetic Algorithm
best_solution, best_cost = genetic_algorithm()
robot0_tour, robot1_tour = best_solution
robot0_cost = evaluate_solution(robot0_tour)
robot1_cost = evaluate_solution(robot1_tour)

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", robot0_cost)
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)
print("Overall Total Travel Cost:", best_cost)