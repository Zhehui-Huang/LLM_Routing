import numpy as np
import random
from math import sqrt

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Parameters
num_robots = 4
depots = [0] * num_robots
population_size = 100
number_of_generations = 500
crossover_rate = 0.8
mutation_rate = 0.15

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize population
def initialize_population():
    population = []
    all_cities = list(cities.keys())[1:]  # Exclude the depot
    for _ in range(population_size):
        random.shuffle(all_cities)
        # Splitting cities roughly evenly among robots
        chunks = np.array_split(all_cities, num_robots)
        chromosome = []
        for chunk in chunks:
            chromosome.append(list(chunk))
        population.append(chromosome)
    return population

# Fitness function
def fitness(chromosome):
    total_cost = 0
    all_tours = []
    for i, tour in enumerate(chromosome):
        tour_cost = calculate_distance(0, tour[0])  # Start from depot
        for j in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[j], tour[j + 1])
        tour_cost += calculate_distance(tour[-1], 0)  # Return to depot
        total_cost += tour_cost
        all_tours.append([0] + tour + [0])  # Include start and end at depot
    return total_cost, all_tours

# Selection
def selection(population):
    sorted_population = sorted(population, key=lambda x: fitness(x)[0])
    return sorted_population[:2]

# Crossover
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1, parent2
    child1, child2 = [], []
    for i in range(num_robots):
        cut = random.randint(1, len(parent1[i]) - 1)
        child1.append(parent1[i][:cut] + parent2[i][cut:])
        child2.append(parent2[i][:cut] + parent1[i][cut:])
    return child1, child2

# Mutation
def mutate(chromosome):
    if random.random() < mutation_rate:
        robot = random.randint(0, num_robots - 1)
        a, b = random.sample(range(len(chromosome[robot])), 2)
        chromosome[robot][a], chromosome[robot][b] = chromosome[robot][b], chromosome[robot][a]
    return chromosome

# Genetic algorithm
def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_cost = float("inf")

    for _ in range(number_of_generations):
        new_population = []
        while len(new_population) < population_size:
            parents = selection(population)
            for child in crossover(parents[0], parents[1]):
                child = mutate(child)
                new_population.append(child)
        population = new_population
        for individual in population:
            cost, _ = fitness(individual)
            if cost < best_cost:
                best_cost = cost
                best_solution = individual

    _, best_tours = fitness(best_solution)
    return best_tours, best_cost

# Run the GA
best_tours, best_cost = genetic_algorithm()

# Output the results
for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")