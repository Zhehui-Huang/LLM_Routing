import numpy as np
import random
from math import sqrt

# Cities and their Coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Parameters for the Genetic Algorithm
num_cities = len(coordinates)
num_depots = 4
num_robots = 4
pop_size = 100
G_max = 1000  # max generations
cr = 0.8  # crossover rate
mr = 0.2  # mutation rate

# Euclidean distance calculation
def calc_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initial population generation
def generate_initial_population():
    population = []
    for _ in range(pop_size):
        # Generate a random permutation of cities
        perm = list(np.random.permutation(range(1, num_cities)))
        # Split into num_robots parts and add depots
        split_points = sorted(random.sample(range(1, num_cities - 1), num_robots - 1))
        tours = []
        start = 0
        for sp in split_points:
            tours.append([0] + perm[start:sp] + [0])  # each tour starts/ends at depot 0
            start = sp
        tours.append([0] + perm[start:] + [0])
        population.append(tours)
    return population

# Evaluate fitness (total distance of all tours)
def evaluate_fitness(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calc_distance(tour[i], tour[i + 1])
        total_cost += tour_cost
    return total_cost

# Genetic operators: Mutation and Crossover
def crossover(parent1, parent2):
    # Simple one point crossover for simplicity
    point = random.randint(1, num_cities - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(tour):
    # Simple swap mutation
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

# GA main loop
population = generate_initial_population()
fitness_scores = [evaluate_fitness(individual) for individual in population]

for generation in range(G_max):
    new_population = []
    while len(new_population) < pop_size:
        # Selection (Tournament)
        parents = random.sample(population, 2)
        parent1 = min(parents, key=evaluate_fitness)
        parent2 = min(parents, key=evaluate_fitness)
        
        # Crossover
        if random.random() < cr:
            child1, child2 = crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        
        # Mutation
        if random.random() < mr:
            mutate(child1)
            mutate(child2)
        
        new_population.extend([child1, child2])

    population = new_population[:pop_size]
    fitness_scores = [evaluate_fitness(individual) for individual in population]

# Find best solution
best_solution = min(population, key=evaluate_fitness)
best_fitness = evaluate_fitness(best_solution)

# Output results
overall_cost = 0
for robot_id, tour in enumerate(best_solution):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += calc_distance(tour[i], tour[i + 1])
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost
print(f"Overall Total Travel Cost: {overall_model_cost}")