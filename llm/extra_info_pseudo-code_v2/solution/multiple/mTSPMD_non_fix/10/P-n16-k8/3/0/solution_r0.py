import numpy as np
import random
import math
from itertools import permutations

# Coordinates of cities and depots
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

num_robots = 8
depots = [0]  # All robots start at depot city 0

# Calculate distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initial random solution generator
def generate_initial_solution():
    cities = list(range(1, len(coords)))  # Exclude depot 0
    random.shuffle(cities)
    size = len(cities) // num_robots
    tours = [cities[i*size:(i+1)*size] for i in range(num_robots-1)]
    tours.append(cities[(num_robots-1)*size:])  # Remaining cities
    tours = [[0] + tour for tour in tours]  # Starting from depot 0
    return tours

# Calculate the cost of the tours
def calculate_costs(tours):
    total_cost = 0
    tour_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        tour_costs.append(tour_cost)
        total_cost += tour_cost
    return tour_costs, total_cost

# Genetic algorithm core functions
def crossover(parent1, parent2):
    """Apply a two-point crossover and maintain subtours integrity."""
    size = min(len(parent1), len(parent2))
    cx1, cx2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    middle = parent2[cx1:cx2]
    fill = [item for item in parent1 if item not in middle]
    child[:cx1] = fill[:cx1]
    child[cx1:cx2] = middle
    child[cx2:] = fill[cx1:]
    return child

def mutate(tour):
    """Simple mutation that swaps two cities in the tour."""
    idx1, idx2 = random.sample(range(1, len(tour)), 2)  # Exclude depot in swaps
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

def genetic_algorithm(population_size=50, generations=100):
    # Generating initial population
    population = [generate_initial_solution() for _ in range(population_size)]
    best_cost = float('inf')
    best_solution = None
    
    for _ in range(generations):
        new_population = []
        costs = []
        for tours in population:
            tour_costs, total_cost = calculate_costs(tours)
            costs.append((total_cost, tours))
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = tours
        costs.sort()  # Sort by total cost
        population = [tour for cost, tour in costs[:population_size//2]]  # Keep best half
        
        # Crossover and mutation
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_solution, best_cost

# Run the genetic algorithm
best_solution, best_cost = genetic_algorithm()
tour_costs, _ = calculate_costs(best_solution)

# Print the results
for i, tour in enumerate(best_num_warranties):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"\nOverall Total Travel Cost: {best_cost}")