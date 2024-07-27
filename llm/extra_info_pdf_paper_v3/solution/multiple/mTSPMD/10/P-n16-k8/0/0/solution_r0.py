import numpy as np
import random

# Function to calculate the Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Define the cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Define the number of robots and their start/end locations based on the depots
robots = list(range(8))  # Robot IDs
depots = {robot: robot for robot in robots}  # Depot mapping

# Helper function to create a random individiual
def create_individual(depot_cities, non_depot_cities):
    # Shuffle non-depot cities
    shuffled_cities = random.sample(non_depot_cities, len(non_depot_cities))
    # Insert the depots in the beginning and end of the shuffle
    for depot in depot_cities:
        shuffled_cities.insert(0, depot)
        shuffled_cities.append(depot)
    return shuffled_cities

# Compute the total cost of the tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Genetic Algorithm Parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Initialize Population
population = []
non_depot_cities = [city for city in cities if city not in depots.values()]
for _ in range(population_size):
    individual = create_individual(list(depots.values()), non_depot_cities)
    population.append(individual)

# Genetic Algorithm Execution
for generation in range(generations):
    # Evaluate
    fitness_scores = [calculate_total_cost(individual) for individual in population]
    
    # Selection
    sorted_population = sorted(zip(fitness_versions, population), key=lambda x: x[0])
    selected = [individual for _, individual in sorted_population[:population_size//2]]
    
    # Crossover and Mutation
    next_population = selected
    while len(next_population) < population_size:
        parent1, parent2 = random.sample(selected, 2)
        child = crossover(parent1, parent2)  # Implement crossover logic
        if random.random() < mutation_rate:
            child = mutate(child)  # Implement mutation logic
        next_population.append(child)
    
    population = next_population

# Best solution
best_solution = population[0]
best_cost = calculate_total_cost(best_solution)

# Output
print(f"Robot 0 Tour: {best_solution}")
print(f"Robot 0 Total Travel Cost: {best_cost}")
print(f"Overall Total Travel Cost: {best_cost}")