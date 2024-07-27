import numpy as np
from scipy.spatial.distance import euclidean
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot depots
depot_assignments = {i: i for i in range(8)}  # Each robot starts at a unique depot

# Calculate distances between each pair of cities
def calculate_distances():
    dists = np.zeros((len(cities), len(cities)))
    for i in cities:
        for j in cities:
            dists[i, j] = euclidean(cities[i], cities[j]) if i != j else float('inf')
    return dists

distances = calculate_distances()

# Genetic Algorithm Components
def initialize_population(size=100):
    population = []
    for _ in range(size):
        individual = [list(cities.keys()) for _ in depot_assignments]
        for tour in individual:
            random.shuffle(tour)
            depot = depot_assignments[individual.index(tour)]
            tour.insert(0, depot)
            tour.append(depot)
        population.append(individual)
    return population
    
def calculate_fitness(individual):
    total_cost = 0
    for tour in individual:
        cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_cost += cost
    return total_cost

def select_parent(population, tournament_size=5):
    tournament = random.sample(population, tournament_count)
    fittest = min(tournament, key=calculate_fitness)
    return fittest

def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        start = random.randint(0, len(parent1[i]) - 2)
        stop = random.randint(start + 1, len(parent1[i]) - 1)
        temp_gene = parent1[i][start:stop]
        new_gene = [city for city in parent2[i] if city not in temp_gene]
        child_gene = new_gene[:start] + temp_gene + new_gene[start:]
        child.append(child_gene)
    return child

def mutate(individual, mutation_rate=0.1):
    for tour in individual:
        if random.random() < mutation_rate:
            i, j = random.randint(1, len(tour) - 2), random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]
    return individual

def genetic_algorithm(population_size=100, generations=100, mutation_rate=0.1):
    population = initialize_population(population_size)
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parent(population), select_parent(population)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            child1, child2 = mutate(child1, mutation_rate), mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        current_best = min(population, key=calculate_fitness)
        current_cost = calculate_fitness(current_best)
        if current_cost < best_cost:
            best_solution, best_cost = current_best, current_cost
    
    return best_solution, best_cost

# Solve the problem
best_solution, best_cost = genetic_algorithm()

# Output results
for idx, route in enumerate(best_solution):
    route_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {best_cost}")