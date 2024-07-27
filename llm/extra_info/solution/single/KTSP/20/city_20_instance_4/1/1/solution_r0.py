import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Define cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Number of cities to select (including depot)
num_cities_to_visit = 16

# Utility function to compute total path cost
def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += euclidean(cities[path[i]], cities[path[i+1]])
    return cost

# Generate random initial subset of cities that includes the depot
def random_city_subset():
    subset = list(range(1, 20))
    random.shuffle(subset)
    return [0] + subset[:num_cities_to_visit-1] + [0]

# Genetic Algorithm to find the shortest path
def genetic_algorithm(population_size=100, generations=1000, mutation_rate=0.1):
    # Initial population
    population = [random_city_subset() for _ in range(population_size)]
    best_route = None
    best_cost = float('inf')
    
    for generation in range(generations):
        # Evaluate current population
        fitness_scores = [path_cost(individual) for individual in population]
        fitness_scores, population = zip(*sorted(zip(fitness_scores, population)))
        
        if fitness_scores[0] < best_cost:
            best_cost = fitness_scores[0]
            best_route = population[0]
        
        # Selection - Top 50% survive
        survivors = population[:len(population)//2]
        
        # Crossover - Create new population by crossover of survivors
        new_population = list(survivors)  # Start with survivors
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(survivors, 2)
            child = crossover(parent1, parent2, num_cities_to_visit)
            new_population.append(child)
        
        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i], mutation_rate)
        
        population = new_population
    
    return best_route, best_cost

def crossover(parent1, parent2, keep_length):
    child = [0]
    start_pos = random.randint(1, keep_length-3)
    end_pos = random.randint(start_pos+1, keep_.len()-1)
    segment = parent1[start_pos:end_pos]
    child.extend(segment)
    child.extend([city for city in parent2 if city not in segment and city != 0])
    child.append(0)
    return child

def mutate(path, rate):
    index1 = random.randint(1, len(path)-3)
    index2 = random.randint(1, len(path)-3)
    path[index1], path[index2] = path[index2], path[index1]
    return path

# Main algorithm
best_tour, best_total_cost = genetic_algorithm()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)