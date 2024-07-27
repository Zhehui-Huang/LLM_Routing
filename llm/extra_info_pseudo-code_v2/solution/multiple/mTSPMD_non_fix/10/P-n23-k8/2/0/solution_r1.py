import numpy as np
from math import sqrt
import random

# Coordinates - including depot cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

def distance(city1, city2):
    c1, c2 = coordinates[city1], coordinates[city2]
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def generate_initial_population(pop_size, num_cities, num_robots, depot_index):
    population = []
    for _ in range(pop_size):
        cities = list(range(num_cities))
        random.shuffle(cities)
        # Insert depots
        positions = sorted(random.sample(range(1, num_cities), num_robots - 1))
        for pos in reversed(positions):
            cities.insert(pos, depot_index)
        cities.insert(0, depot_index)
        cities.append(depot_index)
        population.append(cities)
    return population

def evaluate_tours(individual):
    tour_costs = []
    current_tour, current_cost = [], 0
    start_city = individual[0]

    for i in range(1, len(individual)):
        current_tour.append(individual[i-1])
        current_cost += distance(individual[i-1], individual[i])
        if individual[i] == individual[0]:
            current_tour.append(individual[i])
            tour_costs.append((current_cost, current_tour))
            current_tour, current_cost = [], 0

    total_cost = sum(cost for cost, tour in tour_costs)
    return total_cost, tour_costs

def select_parents(population, fitness):
    sorted_pop = sorted(zip(population, fitness), key=lambda x: x[1])
    return sorted_pop[0][0], sorted_pop[1][0]

def crossover(parent1, parent2, depot_index):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(size), 2))
    # Middle segment from parent1
    middle_segment = [p for p in parent1[start:end] if p != depot_index]
    child[start:end] = middle_segment

    # Fill from parent2 without repeating cities
    fill_index = 0
    for i in range(size):
        city = parent2[i]
        if city not in middle_segment:
            while fill_index < size and child[fill_index] != -1:
                fill_index += 1
            if fill_index < size:
                child[fill_index] = city
                fill_index += 1

    child = [depot_index if x == -1 else x for x in child]
    if child[0] != depot_index:
        child[0] = depot_index
    if child[-1] != depot_index:
        child[-1] = depot_index
    return child

def mutate(individual, mutation_rate):
    for i in range(1, len(individual)-1):
        if random.random() < mutation
        # Swap mutation
        j = random.randint(1, len(indial)-2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm(num_generations, pop_size, num_cities, num_robots, depot_index):
    population = generate_initial_population(pop_size, num_cities, num_robots, depot_index)
    best_solution = None
    best_cost = float('inf')

    for generation in range(num_generations):
        new_pop = []
        fitness_scores = [evaluate_tours(individual)[0] for individual in population]
        for _ in range(len(population)//2):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1 = crossover(parent1, parent2, depot_index)
            child2 = crossover(parent2, parent1, depot_index)
            child1 = mutate(child1, 0.1)
            child2 = mutate(child2, 0.1)
            new_pop.extend([child1, child2])
        
        population = new_pop
        current_best, current_best_cost = min(zip(population, fitness_scores), key=lambda x: x[1])
        if current_best_cost < best_cost:
            best_cost = current_best_cost
            best_solution = current_best
        print(f"Generation {generation}: Best cost so far = {best_cost}")

    total_cost, tours = evaluate_tours(best_solution)
    return total_cost, tours

# Parameters for the GA
num_cities = len(coordinates)
num_robots = 8
depot_index = 0  # All robots start at city 0

# Run the genetic algorithm
overall_cost, detailed_tours = genetic_algorithm(100, 20, num_cities, num_robots, depot_index)

# Output
print("\nOutput:")
print(f"Overall Total Travel Cost: {overall_cost}")
for idx, (cost, tour) in enumerate(detailed_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")