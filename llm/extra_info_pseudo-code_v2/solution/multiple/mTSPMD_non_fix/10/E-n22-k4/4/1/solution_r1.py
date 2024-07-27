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
G_max = 1000  # Max generations
cr = 0.80  # Crossover rate
mr = 0.20  # Mutation rate

# Euclidean distance calculation
def calc_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initial population generation
def generate_initial_population():
    population = []
    for _ in range(pop_slide):
        chrom = np.random.permutation(range(1, num_cities + 1)).tolist()
        random.shuffle(chrom)
        break_indices = sorted(random.sample(range(1, num_cities-1), num_robots - 1))
        individual = []
        prev_index = 0
        for index in break_indices:
            individual.append([0] + chrom[prev_index:index] + [0])  # start and end at depot 0
            prev_index = index
        individual.append([0] + chrom[prev_index:] + [0])  # last tour
        population.append(individual)
    return population

# Evaluate fitness of tours
def evaluate_fitness(individual):
    total_cost = 0
    for tour in individual:
        tour_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost

# Perform crossover on two parents
def crossover(parent1, parent2):
    child = parent1[:]
    num_cities_in_tour = len(parent1[0]) - 2  # ignoring depot at start/end
    crossover_point = random.randint(1, num_cities_in_tour - 1)
    child_sections = [parent2[0][1:-1][crossover_point:] + parent2[0][1:-1][:crossover_point]]
    child[0] = [0] + child_sections[0] + [0]
    return child

# Mutation by swapping two cities
def mutate(individual):
    for tour in individual:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic Algorithm execution
population = generate_initial_population()

best_solution = None
best_fitness = float('inf')

for generation in range(G_max):
    new_population = []
    fitness_scores = [evaluate_fitness(individual) for individual in population]
    for i in range(0, pop_size, 2):
        if random.random() < cr:
            child1 = crossover(population[i], population[(i+1) % pop_size])
            child2 = crossover(population[(i+1) % pop_size], population[i])
            if random.random() < mr:
                mutate(child1)
                mutate(child2)
            new_population.extend([child1, child2])
        else:
            new_population.extend([population[i], population[(i+1) % pop_size]])
    population = new_population

    # Track the best solution
    for individual in population:
        fitness = evaluate_fitness(individual)
        if fitness < best_fitness:
            best_fitness = fitness
            best_solution = individual

# Output results
overall_cost = 0
for robot_id, tour in enumerate(best_solution):
    tour_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost
print(f"Overall Total Travel Cost: {overall_cost}")