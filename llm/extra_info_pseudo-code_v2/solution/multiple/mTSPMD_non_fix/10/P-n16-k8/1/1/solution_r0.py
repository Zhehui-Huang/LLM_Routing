import numpy as- np
import random
import math
from itertools import permutations

# Coordinates (x, y) for each city including depots at starting points of the list
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Utility functions
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Define Genetic Algorithm components
def create_initial_population(number_of_robots, num_population, num_cities=16):
    population = []
    for _ in range(num_population):
        tour = list(range(1, num_cicles))  # cities except depot 0
        random.shuffle(tour)  # shuffle non-depot cities
        tour = [0] + tour  # add depot at the start
        # Create tours for robots by randomly splitting
        split_points = sorted(random.sample(range(1, num_cities-1), number_of_robots-1))
        robot_tours = []
        prev = 0
        for point in split_points:
            robot_tours.append([0] + tour[prev:point] + [0])  # each tour starts and ends at depot 0
            prev = point
        robot_tours.append([0] + tour[prev:] + [0])  # last tour
        population.append(robot_tours)
    return population

def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: sum(total_distance(tour) for tour in x))
    return selected[0]

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1)-1)
    child1_tours = parent1[:cut] + parent2[cut:]
    child2_tours = parent2[:cut] + parent1[cut:]
    return [child1_tours, child2_tours]

def mutation(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)-1), 2)  # avoiding the initial depot 0
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Run Genetic Algorithm
def genetic_algorithm(number_of_robots, population_size, generations, num_cities=16):
    population = create_initial_population(number_of_robots, population_size, num_cities)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            offspring = crossover(parent1, parent2)
            offspring = [[mutation(tour) for tour in child] for child in offspring]
            new_population.extend(offspring)
        population = new_population
        current_best = min(population, key=lambda x: sum(total_distance(tour) for tour in x))
        current_cost = sum(total_distance(tour) for tour in current_best)
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best
    
    return best_solution, best_cost

# Set parameters
number_of_robots = 8
population_size = 50
generations = 1000
best_solution, best_cost = genetic_algorithm(number_of_robots, population_size, generations)

# Display results
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = total_distance(tour)
    overall_cost += cost
    tour_result = " -> ".join(map(str, tour))
    print(f"Robot {idx} Tour: [{tour_result}]")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"\nOverall Total Travel Cost: {overall_cost:.2f}")