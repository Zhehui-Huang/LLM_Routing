import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.utils import shuffle
import random

# Define the cities and their coordinates
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
    15: (37, 69)
}

# Calculate distances between cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = euclidean(cities[i], cities[j])
            else:
                distances[i, j] = float('inf')  # Prevent traveling from the city to itself
    return distances

# Distances matrix
distances = calculate_distances(cities)

# Parameters
num_robots = 8
num_generations = 500
population_size = 100
mutation_rate = 0.2

# Initialize random tours for population
def initial_population():
    pop = []
    cities_list = list(cities.keys())[1:]  # Exclude the depot
    for _ in range(population_size):
        shuffled_cities = shuffle(cities_list)
        pop.append(shuffled_cities)
    return pop

# Calculate total distance of a tour for a robot
def tour_distance(tour, depot=0):
    total_distance = 0
    start = depot
    for city in tour:
        total_distance += distances[start, city]
        start = city
    total_distance += distances[start, depot]  # return to depot
    return total_distance

# Fitness function
def fitness(chromosome):
    split_points = sorted(random.sample(range(1, len(cities)-1), num_robots-1))
    tours = np.split(chromosome, split_points)
    total_cost = sum(tour_distance(tour) for tour in tours)
    return total_cost, tours

# Selection
def select(population):
    fitness_results = [fitness(individual)[0] for individual in population]
    sorted_population = [x for _, x in sorted(zip(fitness_results, population))]
    return sorted_population[:50]  # Select the top 50

# Crossover
def crossover(parent1, parent2):
    child = [-1] * (len(cities) - 1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child[start:end] = parent1[start:end]
    child = [gene if gene in child else -1 for gene in parent2]
    return [gene for gene in child if gene != -1]

# Mutation
def mutate(individual):
    if random.random() < mutation_rate:
        swap_indices = random.sample(range(len(individual)), 2)
        individual[swap_indices[0]], individual[swap_indices[1]] = individual[swap_indices[1]], individual[swap_indices[0]]
    return individual

# Genetic Algorithm
population = initial_population()
for generation in range(num_generations):
    selected = select(population)
    offspring = [mutate(crossover(selected[random.randint(0, len(selected) - 1)],
                                  selected[random.randint(0, len(selected) - 1)])) for _ in range(population_size)]
    population = selected + offspring

# Execution
best_solution = select(population)[0]
best_cost, best_tours = fitness(best_solution)

# Output Result
overall_total_cost = sum(tour_distance(tour) for tour in best_tours)
for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: [0, {' '.join(map(str, tour))}, 0]")
    print(f"Robot {idx} Total Travel Cost: {tour_distance(tour)}")

print(f"Overall Total Travel Cost: {overall_total_cost}")