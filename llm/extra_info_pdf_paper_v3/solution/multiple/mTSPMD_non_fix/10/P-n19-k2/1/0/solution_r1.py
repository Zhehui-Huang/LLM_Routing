import random
import numpy as np
from scipy.spatial.distance import euclidean

# Constants and input data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Generating a distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = euclidean(cities[i], cities[j])
            else:
                distances[i, j] = float('inf')
    return distances

distance_matrix = calculate_distance_matrix(cities)

# Genetic Algorithm components
def create_initial_population(cities, size):
    population = []
    for _ in range(size):
        tour = list(cities.keys())
        random.shuffle(tour)
        population.append(tour)
    return population

def calculate_cost(tour):
    return sum(distance_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def fitness(tour):
    return -calculate_cost(tour)  # We use negative cost for maximization

def select(population, weights):
    chosen = random.choices(population, weights=weights, k=1)
    return chosen[0]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [None]*size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    pointer = 0
    for item in parent2:
        if item not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = item
    return child

def mutate(tour, mutation_rate=0.05):
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

def ga_tsp(cities, distance_matrix, population_size=100, generations=500, mutation_rate=0.05):
    population = create_initial_population(cities, population_size)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(generations):
        new_population = []
        fitness_scores = [fitness(tour) for tour in population]
        for __ in range(population_size):
            parent1 = select(population, fitness_scores)
            parent2 = select(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    
        candidate_solution = max(population, key=fitness)
        candidate_cost = calculate_cost(candidate_solution)
        if candidate_cost < best_cost:
            best_solution, best_cost = candidate_solution, candidate_cost
    
    return best_solution, best_cost

# Running the genetic algorithm
best_tour, best_cost = ga_tsp(cities, distance_matrix)

# Formatting output
print("Optimal Tour: ", best_tour)
print("Total Travel Cost: ", best_cost)