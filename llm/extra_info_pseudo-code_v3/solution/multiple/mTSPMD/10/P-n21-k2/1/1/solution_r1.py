import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given cities and corresponding coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate the distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Customized Genetic Algorithm:
def initial_population(depot1, depot2, num_individuals=50):
    cities = list(range(2, len(coordinates))) # all cities except depots
    population = []
    for _ in range(num_individuals):
        random.shuffle(cities)
        split = len(cities) // 2
        population.append([depot1] + cities[:split] + [depot1])
        population.append([depot2] + cities[split:] + [depot2])
    return population

def compute_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def crossover(tour1, tour2, depot):
    # Using ordered crossover
    size = min(len(tour1), len(tour2)) - 2
    cx_point1, cx_point2 = sorted(random.sample(range(1, size), 2))
    middle = tour1[cx_point1:cx_point2]
    end_part = [city for city in tour2 if city not in middle]
    return [depot] + end_part[:cx_point1-1] + middle + end_part[cx_point1-1:] + [depot]

def mutate(tour, mutation_rate=0.1):
    tour_length = len(tour) - 1
    for i in range(1, tour_length):
        if random.random() < mutation_rate:
            j = random.randint(1, tour_length-1)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic Algorithm Execution
def genetic_algorithm(num_generations=1000, population_size=100):
    population = initial_population(0, 1, population_size)
    
    for generation in range(num_generations):
        # Evaluate
        population_costs = [(tour, compute_tour_cost(tour)) for tour in population]
        # Selection
        population_costs.sort(key=lambda x: x[1])
        population = [tour for tour, cost in population_costs[:population_size]]
        
        # Next Generation
        next_generation = population[:10]  # elitism: top 10 directly to next gen
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2, parent1[0])
            child = mutate(child)
            next_geneneration.append(child)
        population = next_generation
    
    best_tour, best_cost = min(population_costs, key=lambda x: x[1])
    return best_tour, best_cost

best_tour, best_cost = genetic_algorithm()
print("Best Tour:", best_tour)
print("Best Tour Cost:", best_cost)