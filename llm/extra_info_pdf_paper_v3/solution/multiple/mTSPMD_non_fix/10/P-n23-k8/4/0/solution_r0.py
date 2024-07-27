import numpy as np
import random
from scipy.spatial import distance_matrix

# Define cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Parameters for Genetic Algorithm
population_size = 50
num_generations = 500
mutation_rate = 0.1
num_robots = 8

# Calculate the distance matrix between all cities
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Fitness function to minimize the path cost
def calculate_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
    return total_cost

# Generate initial random population
def generate_population():
    population = []
    for _ in range(population_size):
        # Create a permutation of the cities
        permutation = list(np.random.permutation(range(1, len(cities))))
        # Divide cities among robots
        tours = []
        avg_cities_per_robot = len(permutation) // num_robots
        for i in range(num_robots - 1):
            tours.append([0] + permutation[i * avg_cities_per_robot:(i + 1) * avg_cities_per_robot] + [0])
        tours.append([0] + permutation[(num_robots - 1) * avg_cities_per_robot:] + [0])
        population.append(tours)
    return population

# Genetic operators
def crossover(parent1, parent2):
    # Single point crossover for each robot
    child = []
    for i in range(num_robots):
        cut = random.randint(1, len(parent1[i]) - 2)
        first_half = parent1[i][1:cut]
        second_half = [x for x in parent2[i] if x not in first_half]
        child.append([0] + first_half + second_half + [0])
    return child

def mutate(tour):
    # Swap mutation for each tour in the robot's route
    for i in range(num_robots):
        if random.random() < mutation_rate:
            idx1, idx2 = random.randint(1, len(tour[i]) - 2), random.randint(1, len(tour[i]) - 2)
            tour[i][idx1], tour[i][idx2] = tour[i][idx2], tour[i][idx1]
    return tour

# Genetic Algorithm
population = generate_population()
for generation in range(num_generations):
    # Tournament selection based on path cost
    sorted_population = sorted(population, key=calculate_cost)
    new_population = sorted_population[:2]  # Elitism: carry the best solutions to the next generation
    while len(new_population) < population_size:
        parent1, parent2 = random.choices(sorted_population[:population_size//2], k=2)
        child = mutate(crossover(parent1, parent2))
        new_population.append(child)
    population = new_population

# Extract the best solution
best_solution = sorted(population, key=calculate_cost)[0]
best_cost = calculate_cost(best_solution)

# Display output
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")