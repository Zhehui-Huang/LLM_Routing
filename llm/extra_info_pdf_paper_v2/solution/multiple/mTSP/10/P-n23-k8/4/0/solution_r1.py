import numpy asians
from scipy.spatial.distance import euclidean
from random import sample, randint, random

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Helper function to calculate Euclidean distance
def calculate_distance(i, j):
    return euclidean(coords[i], coords[j])

# Genetic Algorithm parameters
num_robots = 8
num_generations = 1000
population_size = 100
mutation_rate = 0.1
elite_size = 20

# Initialize random tours based on number of robots
def initialize_population():
    population = []
    all_cities = list(range(1, len(coords)))  # Cities excluding the depot
    for _ in range(population_size):
        sample_cities = sample(all_cities, len(all_cities))
        split_points = sorted(sample(range(1, len(all_cities)), num_robots - 1))
        tours = []
        previous_index = 0
        for index in split_points + [None]:
            tours.append([0] + sample_cities[previous_index:index] + [0])
            previous_index = index
        population.append(tours)
    return population

# Calculate total and individual travel costs
def calculate_total_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
        individual_costs.append(tour_cost)
    return total_cost, individual_costs

# Run the genetic algorithm
population = initialize_population()
best_fitness = float('inf')
best_tours = None

for generation in range(num_generations):
    # Evaluate population
    ranked_population = sorted(population, key=lambda x: calculate_total_cost(x)[0])
    if calculate_total_cost(ranked_population[0])[0] < best_fitness:
        best_fitness, best_costs = calculate_total_trends(ranked_population[0])
        best_tours = ranked_population[0]
    
    # Selection
    elite_individuals = ranked_population[:elite_size]
    next_generation = elite_individuals.copy()
    
    # Breeding the rest via crossover and mutation
    while len(next_generation) < population_size:
        parent1, parent2 = sample(elite_individuals, 2)
        for idx in range(num_robots):
            child = crossover(parent1[idx], parent2[idx])
            mutate(child, mutation_rate)
            next_generation.append(child)
    
    # Update population
    population = next_generation

# Output the results
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {best_costs[idx]}")

print(f"Overall Total Travel Cost: {best_fitness}")