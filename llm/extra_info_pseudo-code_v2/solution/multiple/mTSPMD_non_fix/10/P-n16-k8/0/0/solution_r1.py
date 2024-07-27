import numpy as np
import random
import math

# Coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots and depots
num_robots = 8
depots = [0 for _ in range(num_robots)]  # all starting at depot 0

# Function to compute the Euclidean distance between two cities
def dist(city1_idx, city2_idx):
    x1, y1 = cities[city1_idx]
    x2, y2 = cities[city2_idx]
    return math.hypot(x2 - x1, y2 - y1)

# Initialize population with partitioned tours for each robot (chromosomes)
def initialize_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        perm = list(range(1, num_cities))
        random.shuffle(perm)
        partitions = sorted(random.sample(range(1, len(perm)), num_robots - 1))
        tours = [perm[i:j] for i, j in zip([0] + partitions, partitions + [None])]
        chromosome = [0]  # All start at depot 0
        for tour in tours:
            chromosome.extend(tour)
            chromosome.append(0)  # return to depot
        population.append(chromosome)
    return population

# Evaluate the total travel cost of a chromosome
def calculate_fitness(chromosome):
    total_cost = 0
    for i in range(1, len(chromosome)):
        total_cost += dist(chromosome[i - 1], chromosome[i])
    return total_cost

# Genetic Algorithm Implementation (simplified for context)
def genetic_algorithm():
    pop_size = 50
    max_generations = 200
    num_cities = 16

    population = initialize_population(pop_size, num_cities, num_robots)
    for generation in range(max_generations):
        fitness_scores = [calculate_fitness(chrom) for chrom in population]
        # (Selection, Crossover, and Mutation logic to be defined here)
        if generation % 10 == 0:
            print(f"Generation {generation}: Best score = {min(fitness_scores)}")
    
    best_solution_idx = np.argmin(fitness_scores)
    best_solution = population[best_solution_idx]
    best_cost = fitness_scores[best_solution_idx]
    
    return best_solution, best_cost

# Execute the Genetic Algorithm
best_solution, best_cost = genetic_algorithm()

# Parse the best solution into readable format
def parse_solution(chromosome):
    tours = []
    tour = []
    for city in chromosome:
        if city == 0:
            if tour:
                tours.append(tour)
                tour = []
        else:
            tour.append(city)

    return tours

tours = parse_solution(best_solution)
overall_total_cost = 0

for i, tour in enumerate(tours):
    cost = calculate_fitness([0] + tour + [0])
    overall_total_cost += cost
    print(f"Robot {i} Tour: {[0] + tour + [0]}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")