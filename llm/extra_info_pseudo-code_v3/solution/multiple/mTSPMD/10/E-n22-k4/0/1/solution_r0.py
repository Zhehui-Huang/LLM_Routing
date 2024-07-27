import numpy as np
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Genetic Algorithm Components
# Chromosome representation: sequence of city visits and partition of cities for each salesman
def create_initial_population(population_size, num_cities, num_salesmen):
    population = []
    for _ in range(population_size):
        sequence = np.random.permutation(range(4, num_cities))  # cities excluding depots
        partitions = sorted(np.random.choice(range(1, num_cities-3), num_salesmen-1, replace=False))
        population.append((sequence, partitions))
    return population

# Fitness function (total distance)
def evaluate_solution(solution, depots):
    sequence, partitions = solution
    segments = np.split(sequence, partitions)
    total_cost = 0
    for idx, segment in enumerate(segments):
        tour = [depots[idx]] + list(segment) + [depots[idx]]
        cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += cost
    return total_cost

# Main Genetic Algorithm Execution
def genetic_algorithm(population_size, num_generations, num_cities, num_salesmen, depots):
    population = create_initial_population(popization_size, num_cities, num_salesmen)
    best_solution = None
    best_cost = float('inf')

    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            # Parent selection and crossover (simplified for demonstration)
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])  
        population = sorted(new_population, key=lambda s: evaluate_solution(s, depots))[:population_size]
        new_best_cost = evaluate_solution(population[0], depots)
        if new_best_cost < best_cost:
            best_cost = new_best_cost
            best_solution = population[0]

    return best_solution, best_cost

# Define higher-level functions for crossover and mutation
def crossover(parent1, parent2):
    # Placeholder for actual crossover logic
    return parent1, parent2

def mutate(individual):
    # Placeholder for actual mutation logic
    return individual

# Running the GA
best_solution, best_cost = genetic_algorithm(
    population_size=100,
    num_generations=1000,
    num_cities=len(cities),
    num_salesmen=4,
    depots=[0, 1, 2, 3]
)

print("Best Solution: ", best_solution)
print("Best Cost: ", best_cost)