import numpy as np
import random
import math
from copy import deepcopy

# Coordinates (x, y) for each city including the depot at the starting point
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def total_distance(tour):
    """Calculate total distance for a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def create_initial_population(num_population, num_cities=16, num_robots=8):
    """Create an initial population for genetic algorithm."""
    population = []
    for _ in range(num_population):
        # Generate a random tour of cities (excluding the depot)
        cities = list(range(1, num_cities))
        random.shuffle(cities)
        
        # Splitting tour among robots randomly
        splits = sorted(random.sample(range(1, num_cities-1), num_robots-1))
        prev = 0
        tours = []
        for split in splits:
            tours.append([0] + cities[prev:split] + [0])
            prev = split
        tours.append([0] + cities[prev:] + [0])
        
        population.append(tours)
    return population

def crossover(tours1, tours2):
    """Perform one point crossover between two sets of tours."""
    point = random.randint(1, len(tours1)-1)
    new_tours1 = tours1[:point] + tours2[point:]
    new_tours2 = tours2[:point] + tours1[point:]
    return [new_tours1, new_tours2]

def mutate(tours, mutation_rate=0.05):
    """Randomly swap cities in the tours with a given mutation rate."""
    for tour in tours:
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour)-1), 2)
            tour[i], tour[j] = tour[j], tour[i]
    return tours

def genetic_algorithm(population_size, generations, num_cities=16, num_robots=8):
    """Run genetic algorithm and find the best routing solution."""
    population = create_initial_population(population_size, num_cities, num_robots)
    best_solution = None
    best_cost = float("inf")

    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            children = crossover(parent1, parent2)
            child1 = mutate(deepcopy(children[0]))
            child2 = mutate(deepcopy(children[1]))
            new_population.extend([child1, child2])
        
        # Assess fitness and keep the best solutions
        population.extend(new_population)
        population.sort(key=lambda tours: sum(total_distance(tour) for tour in tours))
        population = population[:population_size]

        best_current = population[0]
        best_current_cost = sum(total_distance(tour) for tour in best_current)
        if best_current_cost < best_cost:
            best_cost = best_current_cost
            best_solution = best_current

    return best_solution, best_cost

# Set parameters for the genetic algorithm
population_size = 100
generations = 500

# Execute the genetic algorithm
best_solution, best_cost = genetic_algorithm(population, generations)

# Display the results
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = total_distance(tour)
    overall_cost += cost
    tour_result = " -> ".join(str(city) for city in tour)
    print(f"Robot {idx} Tour: [{tour_result}]")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"\nOverall Total Travel Cost: {overall_cost:.2f}")