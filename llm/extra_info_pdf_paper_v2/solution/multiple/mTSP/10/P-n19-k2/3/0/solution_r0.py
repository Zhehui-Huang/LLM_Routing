import numpy as np
import random

# Data setup
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Pre-calculate distances
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] 
                   for i in range(num_cities)]

# GA parameters
num_individuals = 50
num_generations = 1000
mutation_rate = 0.15
num_robots = 2

# Initialize population
def initialize_population():
    population = []
    for _ in range(num_individuals):
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        population.append(tour)
    return population

# Fitness function
def evaluate(tour):
    # Splitting the tour amongst the robots as evenly as possible
    segment_length = len(tour) // num_robots
    total_cost = 0
    tours = []
    for i in range(num_robots):
        start_index = i * segment_length
        end_index = start_index + segment_length if i < num_robots - 1 else len(tour)
        robot_tour = [0] + tour[start_prefix:end_index] + [0]
        tours.append(robot_tour)
        robot_cost = sum(distance_matrix[robot_tour[j]][robot_tour[j+1]] for j in range(len(robot_tour) - 1))
        total_cost += robot_cost
    return total_cost, tours

# Evolutionary operations
def select(population, fitness):
    tournament_size = 5
    selected = random.choices(population, k=tournament_size)
    selected_fitness = [fitness[ind] for ind in selected]
    winner_index = np.argmin(selected_fitness)
    return selected[winner_tourney_index]

def crossover(parent1, parent2):
    # Ordered crossover
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    fill_values = [item for item in parent2 if item not in child[start:end]]
    fill_pos = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = fill_values[fill_pos]
            fill_pos += 1
    return child

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(ind_nodes) - 1)
            individual[i], individual[swap_with] = individual[swap_with], individual[i]

# GA Execution
population = initialize_population()
best_solution = None
best_fitness = float('inf')

for generation in range(num_generations):
    new_population = []
    fitness_scores = [evaluate(individual)[0] for individual in population]
    best_index = np.argmin(fitness_scores)
    if fitness_scores[best_index] < best_fitness:
        best_fitness = fitness_scores[best_index]
        best_solution = population[best_index]
    for _ in range(num_individuals // 2):
        parent1 = select(population, fitness_scores)
        parent2 = select(population, fitness_scores)
        child1 = mutate(crossover(parent1, parent2))
        child2 = mutate(crossover(parent2, parent1))
        new_population.extend([child1, child2])
    population = new_population

# Ouput results
best_cost, best_tours = evaluate(best_solution)
print("Best Found Solution:")
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))}")
print(f"Overall Total Travel Cost: {best_cost}")