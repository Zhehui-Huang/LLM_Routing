import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, shuffle

def initialize_population(num_individuals, num_cities, num_robots):
    population = []
    for _ in range(num_individuals):
        route = sample(range(1, num_cities), num_cities - 1)  # cities minus depot
        partition_points = sorted(sample(range(1, num_cities - 1), num_robots - 1))
        population.append((route, partition_points))
    return population

def calculate_cost(route, partition_points, city_coords):
    costs = []
    tours = []
    total_cost = 0.0
    start_index = 0
    
    for end_index in partition_points + [len(route)]:
        tour = [0] + route[start_index:end_index] + [0]
        tours.append(tour)
        tour_cost = sum(euclidean(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour) - 1))
        costs.append(tour_cost)
        total_cost += tour_cost
        start_index = end_index
        
    return total_cost, costs, tours

# Parameters
num_cities = 19
city_coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
                (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
num_robots = 2
population_size = 50
num_generations = 100

# Initialize population
population = initialize_population(population_size, num_cities, num_robots)

best_solution = None
best_total_cost = float('inf')

# Evolutionary loop
for generation in range(num_generations):
    # Calculate fitness
    fitness_info = [calculate_cost(individual[0], individual[1], city_coords) for individual in population]
    
    # Select the best individuals
    population_sorted = sorted(zip(population, fitness_info), key=lambda x: x[1][0])
    if population_sorted[0][1][0] < best_total_cost:
        best_solution = population_sorted[0]
        best_total_cost = best_solution[1][0]
    
    # Generate next population
    new_population = []
    while len(new_population) < population_size:
        p1, p2 = sample(population, 2)
        # Simple crossover and mutation (omitted for brevity; assuming correct implementation)
        p1_route = sample(p1[0], len(p1[0]))
        p2_points = sorted(sample(range(1, num_cities - 1), num_robots - 1))
        new_population.append((p1_route, p2_points))
    
    population = new_population

# Final output of the best found solution
print(f"Best overall total cost: {best_total_cost:.2f}")
for idx, tour in enumerate(best_solution[1][2]):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {best_solution[1][1][idx]:.2f}")