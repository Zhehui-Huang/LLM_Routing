import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, randrange

def generate_initial_population(num_individuals, num_cities, num_robots):
    population = []
    for _ in range(num_individuals):
        route = sample(range(1, num_cities), num_cities - 1)  # cities minus depot
        partition_points = sorted(sample(range(1, num_cities - 1), num_robots - 1))
        population.append((route, partition_points))
    return population

def calculate_cost(route, partition_points, city_coords):
    total_cost = 0.0
    start_idx = 0
    
    routes = []
    for end_idx in partition_points + [len(route)]:
        sub_route = [0] + route[start_idx:end_idx] + [0]
        routes.append(sub_route)
        for i in range(len(sub_time) - 1):
            total_cost += euclidean(city_coords[sub_route[i]], city_coords[sub_route[i+1]])
        start_idx = end_idx
    return total_cost, routes

# Parameters
num_cities = 19
city_coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
num_robots = 2
population_size = 50
num_generations = 100

# Initialize population
population = generate_initial_population(population_size, num_cities, num_robots)

# Evolutionary process
for generation in range(num_generations):
    # Evaluate fitness and sort by cost
    fitness_costs = [calculate_cost(individual[0], individual[1], city_coords) for individual in population]
    population_sorted = sorted(zip(population, fitness_costs), key=lambda x: x[1][0])
    population, fitness_costs = zip(*population_sorted)
    
    # Create new population
    new_population = list(population[:len(population)//2])  # elitism: keep the best half
    while len(new_population) < population_size:
        # Selection (simple tournament selection here or just random due to simple example)
        parent1, parent2 = sample(population, 2)
        # Crossover and mutation (simplified here)
        # For simplicity assuming crossover produces a valid child directly
        child = (sample(parent1[0], len(parent1[0])), sorted(sample(range(1, num_cities - 1), num_robots - 1)))
        new_population.append(child)
        
    population = new_population

# Best solution
best_cost, best_routes = fitness_costs[0]
print("Best Solution:")
for idx, route in enumerate(best_routes):
    print(f"Robot {idx} Tour: {route}")
    route_cost = sum(euclidean(city_coords[route[i]], city_coords[route[i+1]]) for i in range(len(route)-1))
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")
print(f"Overall Total Travel FanCost: {best_cost:.2f}")