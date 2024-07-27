import random
import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of the cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def get_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Parameters for GA
num_generations = 1000
population_size = 50
num_robots = 2
mutation_rate = 0.1
crossover_rate = 0.8
depots = [0, 1]

# Creates a random valid chromosome
def create_chromosome():
    all_cities = list(range(2, len(cities)))  # Avoid depots since depots are fixed
    random.shuffle(all_cities)
    splits = sorted(random.sample(range(1, len(all_cities)), num_robots - 1))
    tours = [all_cities[i:j] for i, j in zip([0] + splits, splits + [None])]
    chromosome = [-depots[i%len(depots)] for i in range(num_robots)]
    for i, tour in enumerate(tours):
        chromosome.extend(tour)
        chromosome.append(-depots[i%len(depots)])
    return chromosome

# Fitness function (lower distance is better, hence negative)
def fitness(chromosome):
    total_distance = 0
    current_tour = []
    current_depot = None
    for gene in chromosome:
        if gene < 0:  # depot
            if current_tour:
                total_distance += get_distance(current_tour[-1], current_depot)
                current_tour = []
            current_depot = abs(gene)
        else:
            if current_tour:
                total_distance += get_distance(current_tour[-1], gene)
            else:
                total_distance += get_distance(current_depot, gene)
            current_tour.append(gene)
    return -total_distance

# Output the formulated tour from chromosome
def formulate_tour(chromosome):
    tours = {}
    current_tour = []
    current_robot = -1
    for gene in chromosome:
        if gene < 0:  # depot
            if current_tour:
                current_tour.append(current_tour[0])  # Close the loop to the depot
                tours[current_robot] = current_tour.copy()
                current_tour = []
            current_robot = abs(gene)
            current_tour.append(current_robot)
        else:
            current_tour.append(gene)
    if current_tour:
        current_tour.append(current_tour[0])
        tours[current_robot] = current_tour
    return tours

# Initialize a random population
population = [create_chromosome() for _ in range(population_size)]
fitness_scores = [fitness(chrom) for chrom in population]

# Genetic Algorithm process
for generation in range(num_generations):
    # Tournament selection and reproduction (Elitism and Crossover)
    sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1])
    population, fitness_scores = zip(*sorted_population)  # Unzipped
    
    next_generation = list(population[:10])  # Elitism: Carry forward the best 10 solutions
    while len(next_generation) < population_size:
        if random.random() < crossover_rate:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            # Simple crossover implementation (for clarity, not following the exact model given)
            cut1, cut2 = sorted(random.sample(range(len(parent1)), 2))
            child = parent1[:cut1] + parent2[cut1:cut2] + parent1[cut2:]
            next_generation.append(child)
        else:
            next_generation.append(random.choice(population))
    
    population = next_generation
    fitness_scores = [fitness(chrom) for chrom in population]

# Optimal solution and output
best_solution_idx = np.argmin(fitness_scores)
optimal_tours = formulate_tour(population[best_solution_idx])
total_cost = -fitness_scores[best_solution_idx]

# Display results
for robot, tour in optimal_tours.items():
    print(f"Robot {robot} Tour:", tour)
    tour_cost = sum([get_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    print(f"Robot {robot} Total Travel Cost: {tour_detect completed")
print(f"Overall Total Travel Cost: {total_cost}")