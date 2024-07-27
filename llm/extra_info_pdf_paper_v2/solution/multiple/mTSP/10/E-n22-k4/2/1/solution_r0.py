import numpy as np
import random
import itertools

# Cities coordinates, including the depot city as index 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]
num_cities = len(coordinates) - 1  # Exclude depot city

# Robot info
num_robots = 4

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to evaluate total travel costs of tours defined by robot paths
def evaluate(paths):
    total_cost = 0
    for path in paths:
        tour_cost = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))
        total_cost += tour_cost
    return total_cost

# Function to generate random feasible tours for robots
def generate_random_tours():
    cities = list(range(1, num_cities + 1))
    random.shuffle(cities)
    partitions = sorted(random.sample(range(1, num_cities), num_robots - 1))
    sub_tours = [cities[i:j] for i, j in zip([0]+partitions, partitions+[None])]
    paths = [[0] + sub_tour + [0] for sub_tour in sub_tours]
    return paths

# Apply the Genetic Algorithm
best_solution = None
best_cost = float('inf')
for generation in range(1000):  # Number of generations
    # Generate or evolve a population of solutions
    if generation == 0:
        population = [generate_random_tours() for _ in range(50)]  # Initial population
    else:
        # Apply selection, crossover, and mutation to evolve the population
        population = evolve(population)
    
    # Evaluate the current population
    for solution in population:
        cost = evaluate(solution)
        if cost < best_cost:
            best_cost = cost
            best_solution = solution

# Output the results
total_cost = 0
for robot_id, tour in enumerate(best_solution):
    robot_tour_cost = evaluate([tour])
    total_cost += robot_tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")