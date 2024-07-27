import numpy as np
import random
from itertools import permutations

# Coordinates of each city (depot cities included)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Euclidean distance calculator
def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize population
def initialize_population(size, num_cities):
    return [random.sample(range(4, num_cities), num_cities - 4) for _ in range(size)]

# Evaluate fitness of each chromosome
def fitness(chromosome, depot_starts):
    total_cost = 0
    current_location = depot_starts[0]
    for city in chromosome:
        total_cost += calculate_distance(current_location, city)
        current_location = city
    total_cost += calculate_distance(current_location, depot_starts[1])  # Return to depot
    return total_cost

# Selection using tournament
def tournament_selection(population, scores, k=3):
    selection_idx = np.random.randint(len(population))
    for idx in np.random.randint(0, len(population), k-1):
        if scores[idx] < scores[selection_idx]:
            selection_idx = idx
    return population[selection_idx]

# Ordered Crossover
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    fill_items = [item for item in parent2 if item not in child]
    fill_pos = [pos for pos, item in enumerate(child) if item is None]
    for pos, item in zip(fill_pos, fill_items):
        child[pos] = item
    return child

# Mutation operator: Swap two elements
def mutate(chromosome, mutation_rate=0.02):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic algorithm to solve mTSP
def genetic_algorithm(depots, num_generations=1000, pop_size=50, mutation_rate=0.02):
    num_cities = len(cities)
    population = initialize_population(pop_size, num_cities)
    best_tour = None
    best_score = float('inf')
    
    for generation in range(num_generations):
        # Evaluate all individuals in the population
        scores = [fitness(chromosome, depots) for chromosome in population]
        # Check for a new best solution
        for i in range(pop_size):
            if scores[i] < best_score:
                best_score = scores[i]
                best_tour = population[i]
        
        # Selection and create new population
        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)
            child = ordered_crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    return best_tour, best_score

# Define depots for each robot; tuples of starting and ending depots
depot_pairs = [(0,0), (1,1), (2,2), (3,3)]
robot_tours_and_costs = []

# Solve for each robot
for i, depot_pair in enumerate(depot_pairs):
    best_tour, best_cost = genetic_algorithm(depot_pair)
    robot_tour = [depot_pair[0]] + best_tour + [depot_pair[1]]
    robot_tours_and_costs.append((robot_tour, best_cost))

# Output results
overall_cost = sum(cost for _, cost in robot_tours_and_costs)
for idx, (tour, cost) in enumerate(robot_torna_costs):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")