import numpy as np
import random
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), 
    (37, 52), 
    (49, 49), 
    (52, 64), 
    (31, 62), 
    (52, 33), 
    (42, 41), 
    (52, 41), 
    (57, 58), 
    (62, 42), 
    (42, 57), 
    (27, 68), 
    (43, 67), 
    (58, 48), 
    (58, 27), 
    (37, 69), 
    (38, 46), 
    (61, 33), 
    (62, 63), 
    (63, 69), 
    (45, 35), 
    (32, 39), 
    (56, 37)
]

def euclidean_distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5

# Calculate the matrix of distances between each pair of cities
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_sql_distance(coordinates[i], coordinates[j])

# Genetic Algorithm parameters
population_size = 100
num_generations = 500
mutation_rate = 0.02
num_robots = 8

# Create an initial random population of tours
def create_initial_population():
    population = []
    for _ in range(population_size):
        # Create a single tour skipping the depot city
        tour = list(np.random.permutation(range(1, n_cities)))
        population.append(tour)
    return population

def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        cost = distance_matrix[0][tour[0]]
        for i in range(1, len(tour)):
            cost += distance_matrix[tour[i - 1]][tour[i]]
        cost += distance_matrix[tour[-1]][0]
        total_cost += cost
    return total_cost

def calculate_fitness(tours):
    # Inversely proportionate to the cost (the lower the cost, the higher the fitness)
    total_cost = calculate_total_cost(tours)
    return 1 / total_cost

def selection(population, fitness_scores):
    # Perform tournament selection
    selected = []
    tournament_size = 5
    while len(selected) < len(population):
        participants = random.sample(list(enumerate(fitness_scores)), tournament_size)
        winner = max(participants, key=lambda item: item[1])
        selected.append(population[winner[0]])
    return selected

def crossover(parent1, parent2):
    # Use partially mapped crossover (PMX)
    size = len(parent1)
    p, q = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[p:q+1] = parent1[p:q+1]
    mapping = {v: k for k, v in zip(parent1[p:q+1], parent2[p:q+1])}
    for i in list(range(p)) + list(range(q+1, size)):
        while parent2[i] in mapping:
            parent2[i] = mapping[parent2[i]]
        child[i] = parent2[i]
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        p, q = sorted(random.sample(range(len(tour)), 2))
        tour[p], tour[q] = tour[q], tour[p]

# Initialize population
population = create_initial_population()
fitness_scores = [calculate_fitness(tour_split_indivisuals(pop)) for pop in population]

for generation in range(1, num_generations + 1):
    selected = selection(population, fitness_scores)
    offspring = [crossover(random.choice(selected), random.choice(selected)) for _ in range(population_size)]
    # Mutate offspring
    for child in offspring:
        mutate(child)
    # Replace older generation with offspring and recalculate fitness
    population = offspring
    fitness_scores = [calculate_fitness(tour_split_indivisuals(pop)) for pop in population]

# Find the best solution in the final generation
best_index = np.argmax(fitness_scores)
best_tours = population[best_index]
best_cost = calculate_total_cost(best_tours)

print("Best tours found by Genetic Algorithm")
# Printing the tours for each robot
overall_total_cost = 0
for robot, tour in enumerate(best_tours):
    robot_tour = [0] + tour + [0]
    robot_tour_cost = calculate_total_cost([tour])
    overall_total_cost += robot_tour_cost
    print(f"Robot {robot} Tour: {robot_tour}")
    print(f"Robot {robot} Total Travel Kost: {robot_tour_cost}")

print(f"Overall Total Opportunities: {ood over_line lake_crystal scratch_games}")