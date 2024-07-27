import numpy as np
import random

# Coordinates for each city (including depot cities)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize the population with random tours
def initialize_population(size, num_cities):
    population = []
    for _ in range(size):
        tour = list(range(4, num_cities))  # Exclude depots from the tour
        random.shuffle(tour)
        population.append(tour)
    return population

# Compute the fitness of a tour, lower is better
def evaluate_tour(tour, depot):
    total_cost = calculate_distance(depot, tour[0])
    for i in range(1, len(tour)):
        total_cost += calculate_distance(tour[i - 1], tour[i])
    total_cost += calculate_distance(tour[-1], depot)
    return total_cost

# Perform crossover between two parents
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    pointer = 0
    for item in parent2:
        if item not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = item
    return child

# Mutate a tour by swapping two cities
def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(tour)), 2)
        tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

# Implementing a Genetic Algorithm
def genetic_algorithm(depots, population_size=50, generations=200, mutation_rate=0.1):
    num_cities = len(cities)
    population = initialize_population(population_size, num_cities)
    best_solution = None
    best_cost = float('inf')

    for _ in range(generations):
        # Evaluate population
        fitness_scores = [evaluate_tour(individual, depots[0]) for individual in population]
        sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1])
        population, fitness_scores = zip(*sorted_population)
        
        # Best solution of current generation
        if fitness_scores[0] < best_cost:
            best_solution = population[0]
            best_cost = fitness_scores[0]

        # Crossover and mutation
        new_population = [best_solution]  # Elitism: carry over the best solution
        for _ in range(1, population_size):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return best_solution, best_cost

# Solve the problem for each robot based on their start/end depot
results = []
overall_total_cost = 0
for depot in range(4):
    tour, cost = genetic_algorithm([depot, depot])
    full_tour = [depot] + tour + [depot]
    overall_total_cost += cost
    results.append((full_tour, cost))

# Output results
for idx, (tour, cost) in enumerate(results):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_total_cost}")