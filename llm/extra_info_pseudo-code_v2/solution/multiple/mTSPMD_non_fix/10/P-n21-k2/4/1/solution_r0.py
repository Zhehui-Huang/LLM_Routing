import numpy as np
import random
import math

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate a random initial solution (chromosome), treating each depot separately
def generate_initial_solution(city_count, robot_count, depot_indices):
    # Shuffle all cities except depots
    non_depot_cities = list(set(range(city_count)) - set(depot_indices))
    random.shuffle(non_depot_cities)
    
    # Split cities roughly equally between robots (can be adjusted to try different distributions)
    split_index = len(non_depot_cities) // robot_count
    tours = {}
    start = 0
    for i in range(robot_count):
        if i == robot_count - 1:
            tours[i] = non_depot_cities[start:]
        else:
            tours[i] = non_depot_cities[start:start+split_index]
        start += split_index
    
    # Return a dictionary where the keys are robot indices and the values are the tours
    return {i: [depot_indices[i]] + tours[i] for i in range(robot_count)}

# Calculate the total cost of tours
def calculate_tour_costs(tours, depot_indices):
    costs = {}
    total_cost = 0
    for robot, tour in tours.items():
        cost = 0
        current_city = depot_indices[robot]
        for next_city in tour:
            cost += calc_distance(current_city, next_city)
            current_city = next_city
        costs[robot] = cost
        total_cost += cost
    return costs, total_cost

# Genetic Algorithm parameters
num_cities = len(cities)
num_robots = 2
depots = [0, 1]  # Depot indices per robot
iterations = 1000
population_size = 50
mutation_rate = 0.1

# Initialize population
population = [generate_initial_solution(num_cities, num_robots, depots) for _ in range(population_size)]
fitness_scores = []

# Evaluate initial population
for chromosome in population:
    costs, total_cost = calculate_tour_costs(chromosome, depots)
    fitness_scores.append((chromosome, total_cost))

# Genetic algorithm main loop
for iteration in range(iterations):
    # Selection based on fitness
    population_sorted = sorted(fitness_scores, key=lambda x: x[1])  # Sort by total cost, lower is better
    best_solutions = population_sorted[:len(population)//2]  # Elitism: take the best half
    
    # Crossover and mutation to create new solutions
    new_population = [sol[0] for sol in best_solutions]  # Keep the best solutions
    
    # Adding new solutions by crossover and mutation
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(best_solutions, 2)
        # Applying crossover and mutation is complex and typically domain specific. Here I assume a simple approach:
        # [TODO: Add detailed crossover and mutation implementation as in examples]
        # [This would involve real code to crossover and mutate the two chosen parent solutions]
        # [Details were omitted for brevity]
        child = parent1[0]  # This is a placeholder for actual crossover and mutation logic
        new_population.append(child)
    
    # Recalculate fitness for the new population
    fitness_scores = []
    for chromosome in new_population:
        costs, total_cost = calculate_tour_costs(chromosome, depots)
        fitness_scores.append((chromosome, total_cost))

# Reporting best solution
best_solution = sorted(fitness_scores, key=lambda x: x[1])[0]
best_tours, overall_cost = calculate_tour_costs(best_solution[0], depots)

# Output the solution
for robot, tour in best_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {best_tours[robot]}")
print(f"Overall Total Travel Cost: {overall_cost}")