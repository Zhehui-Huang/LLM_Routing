import numpy as np
import random
from scipy.spatial import distance

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Distance matrix computation
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return matrix

distance_matrix = compute_distance_matrix(cities)

# Initial configuration
robots = 4
depots = {0: 0, 1: 1, 2: 2, 3: 3}

# Function to compute the total travel cost of a tour
def tour_cost(tour, distance_matrix):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Genetic Algorithm Components
def create_initial_population(size, cities, depots, num_robots):
    population = []
    other_cities = list(set(cities) - set(depots.values()))
    for _ in range(size):
        random.shuffle(other_cities)
        chromosome = depots_to_chromosome(depots, other_cities, num_robots)
        population.append(chromosome)
    return population

def depots_to_chromosome(depots, other_cities, num_robots):
    parts = np.array_split(other_cities, num_robots)
    chromosome = []
    for i, part in enumerate(parts):
        tour = [depots[i]] + list(part) + [depots[i]]
        chromosome.append(tour)
    return chromosome

def genetic_algorithm(cities, depots, num_robots, distance_matrix, iterations=1000, pop_size=100):
    population = create_initial_population(pop_size, cities, depots, num_robots)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(iterations):
        # Evaluate the population
        evaluated = []
        for individual in population:
            total_cost = sum(tour_cost(tour, distance_matrix) for tour in individual)
            evaluated.append((individual, total_cost))
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = individual
        
        # Selection (roulette wheel selection)
        fitnesses = [1 / cost for _, cost in evaluated]
        total_fitness = sum(fitnesses)
        probabilities = [f / total_fitness for f in fitnesses]
        selected_indices = np.random.choice(range(pop_size), size=pop_size, p=probabilities)
        selected_population = [population[i] for i in selected_indices]

        # Crossover and mutation (simplified, each pair produces one offspring)
        next_population = []
        for i in range(0, pop_size, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i+1] if i+1 < pop_size else selected_population[0]
            # Ordered crossover and simple mutation can be applied here
            child1 = parent1  # Placeholder for actual crossover and mutation logic
            next_population.append(child1)
        
        population = next_size
        
    return best_solution, best_cost

# Finding the best solution
best_solution, best_cost = genetic_algorithm(cities, depots, robots, distance_matrix)

# Print results
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = tour_cost(tour, distance_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overallromise_robot_executionl_cost}")