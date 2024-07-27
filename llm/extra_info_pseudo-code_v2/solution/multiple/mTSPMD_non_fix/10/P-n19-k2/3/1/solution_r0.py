import numpy as np
import random
from math import sqrt

# List of cities by their coordinates.
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Euclidean distance calculation.
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Total number of cities and robots.
num_cities = len(cities)
num_robots = 2

# Function to calculate the total path cost for a given tour.
def path_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Function to create a random valid chromosome.
def create_valid_chromosome():
    unique_cities = list(range(2, num_cities))  # Exclude separated depots
    random.shuffle(unique_cities)
    # To divide almost evenly between robots:
    split_point = len(unique_cities) // num_robots
    chromosome = []
    robot_chunks = [unique_cities[:split_point]] + [unique_cities[split_point:]]
    
    # Add depots back into the chromosome
    for robot_id in range(num_robots):
        robot_tour = [0] + robot_chunks[robot_id]
        chromosome.extend(robot_tour)
    return chromosome

# Function to decode a chromosome into separate robot tours.
def decode_chromosome(chromosome):
    tours = []
    current_tour = []
    for gene in chromosome:
        if gene == 0 and current_tour:
            tours.append(current_tour)
            current_tour = [0]  # restart tour for the next robot
        else:
            current_tour.append(gene)
    if current_tour: tours.append(current_tour)  # add the last tour
    return tours

# Let us assume that we have a simple approach to simulate genetic iterations
def genetic_algorithm():
    population_size = 20
    population = [create_valid_chromosome() for _ in range(population_size)]
    generations = 100
    for _ in range(generations):
        # Here, you can implement crossover and mutation functions for genetic iterations.
        # For simplification, let's randomly shuffle populations in this pseudo example.
        population = [random.sample(indiv, len(indiv)) for indiv in population]

    # Select the best solution from the current population
    best_solution = min(population, key=lambda chromo: path_cost(chromo))
    return best_solution

# Running the genetic algorithm and preparing the output.
best_chromosome = genetic_algorithm()
best_tours = decode_chromosome(best_chromosome)
total_costs = [path_cost(tour) for tour in best_tours]
overall_cost = sum(total_costs)

# Display the results
for i, (tour, cost) in enumerate(zip(best_tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")