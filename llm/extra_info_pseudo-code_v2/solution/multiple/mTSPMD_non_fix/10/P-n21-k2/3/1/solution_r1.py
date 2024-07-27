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
    chromosome = []
    for i, tour in enumerate(tours):
        chromosome.extend(tour)
    return chromosome

# Calculate total fitness for tours
def fitness(chromosome):
    tour_lengths = calculate_tour_lengths(chromosome)
    return -sum(tour_lengths)

# Create tours from a chromosome
def create_tours(chromosome):
    # Partition tours between robots
    size_per_robot = len(chromosome) // num_robots
    tours = [chromosome[i*size_per_robot:(i+1)*size_per_robot] for i in range(num_robots)]
    for i in range(len(tours)):
        tours[i].insert(0, depots[0])  # start at depot
    return tours

# Calculate distance for each robot's tour
def calculate_tour_lengths(chromosome):
    tours = create_tours(chromosome)
    tour_lengths = []
    for tour in tours:
        tour_length = 0
        for i in range(len(tour) - 1):
            tour_length += get_distance(tour[i], tour[i+1])
        tour_length += get_distance(tour[-1], tour[0])  # Return to start depot
        tour_lengths.append(tour_length)
    return tour_lengths

# Main Genetic Algorithm
population = [create_chromosome() for _ in range(population_size)]
best_fitness = float('-inf')
best_chromosome = None

for generation in range(num_generations):
    new_population = []
    for chromosome in population:
        if random.random() < mutation_rate:
            # Mutation: swap two cities
            idx1, idx2 = random.sample(range(len(chromosome)), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        new_population.append(chromosome)
    
    # Crossover
    population = new_population
    for i in range(0, len(population), 2):
        if random.random() < crossover_rate and i+1 < len(population):
            # One-point crossover
            point = random.randint(1, len(population[i]) - 1)
            new_ch1 = population[i][:point] + population[i+1][point:]
            new_ch2 = population[i+1][:point] + population[i][point:]
            population[i], population[i+1] = new_ch1, new_ch2
    
    # Selection based on fitness
    fitnesses = [fitness(chrom) for chrom in population]
    sorted_indices = np.argsort(fitnesses)
    population = [population[idx] for idx in sorted_indices[:population_size]]
    if fitnesses[sorted_indices[0]] > best_fitness:
        best_fitness = fitnesses[sorted_response.append(chromosome)
        best_chromosome = population[sorted_indices[0]]

# Calculating and printing results
best_tours = create_tours(best_chromosome)
costs = calculate_tour_lengths(best_chromosome)

for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {sum(costs)}")