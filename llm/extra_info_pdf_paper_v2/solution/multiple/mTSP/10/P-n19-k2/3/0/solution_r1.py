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
distance_matrix = [[euclidean_vectors(coords[i], coords[j]) for j in range(num_cities)]
                   for i in range(num_cities)]

# GA parameters
num_individuals = 50
num_generations = 1000
mutation_rate = 0.05
num_robots = 2

# Initialize population
def initialize_population():
    population = []
    for _ in range(num_individuals):
        tour = list(range(1, num_cities))  # Tour doesn't include the depot
        random.shuffle(tour)
        population.append(tour)
    return population

# Fitness function to minimize
def evaluate(tour):
    segment_length = len(tour) // num_robots
    total_cost = 0
    tours = []
    
    for i in range(num_robots):
        start_index = i * segment_length
        end_index = start_index + segment_length if i < num_robots - 1 else len(tour)
        robot_tour = [0] + tour[start_index:end_index] + [0]
        tours.append(robot_tour)
        robot_cost = sum(distance_matrix[robot_tour[j]][robot_tour[j + 1]] for j in range(len(robot_tour) - 1))
        total_cost += robot_cost
    
    return total_cost, tours

# Evolutionary operations
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

def crossover(a, b):
    start, end = sorted(random.sample(range(len(a)), 2))
    child = [None]*len(a)
    child[start:end] = a[start:end]
    pointer = 0
    for x in b:
        if x not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = x
    return child

def select(population, fitness_scores):
    fitness_probs = [1/f for f in fitness_scores]
    total_fitness = sum(fitness_probs)
    normalized_fitness = [f/total_fitness for f in fitness_probs]
    return population[np.random.choice(range(len(population)), p=normalized_fitness)]

# Genetic Algorithm Process
population = initialize_population()
best_solution = None
best_fitness = float('inf')

for generation in range(num_generations):
    fitness_scores = [evaluate(individual)[0] for individual in population]
    fittest_index = np.argmin(fitness_scores)
 
    if fitness_scores[fittest_index] < best_fitness:
        best_fitness = fitness_scores[fittest_index]
        best_solution = population[fittest_index]
        
    new_population = []
    
    while len(new_population) < num_individuals:
        parent1 = select(population, fitness_scores)
        parent2 = select(population, fitness_scores)
        if random.random() > 0.1:
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
        else:
            offspring1, offspring2 = parent1, parent2

        mutate(offspring1)
        mutate(offspring2)
        new_population.append(offspring1)
        new_population.append(offspring2)
    
    population = new_population

# Displaying the results
if best_solution:
    best_cost, best_tours = evaluate(best_solution)
    print("Optimized Tours:")
    for idx, tour in enumerate(best_tours):
        print(f"Robot {idx} Tour: {tour}")
        tour_cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {best_cost}")