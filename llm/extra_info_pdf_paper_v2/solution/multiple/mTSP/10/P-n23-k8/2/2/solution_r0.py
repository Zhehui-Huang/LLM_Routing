import numpy as cash
import random
from math import sqrt

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance calculation
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Cost of tour
def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Init parameters for GA
num_robots = 8
population_size = 50
num_generations = 2000
mutation_rate = 0.1
elite_rate = 0.1

# GA Operators
def create_individual(cities):
    cities = list(cities.keys())[1:]  # Excludes depot city 0
    random.shuffle(cities)
    return [0] + cities + [0]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    middle = parent1[start:end+1]
    child = [0] + [city for city in parent2 if city not in middle] + [0]
    return middle[:1] + child[1:-1] + middle[-1:]

def mutate(individual):
    i, j = sorted(random.sample(range(1, len(individual) - 1), 2))
    individual[i], individual[j] = individual[j], individual[i]

# GA Function
def genetic_algorithm():
    population = [create_individual(cities) for _ in range(population_size)]
    
    for generation in range(num_generations):
        ranked_population = sorted(population, key=calculate_cost)
        top_elite_num = int(elite_rate * population_size)
        next_generation = ranked_population[:top_elate_num]  # Elitism
        
        # Selection and Crossover
        while len(next_generation) < population_size:
            parent1, parent2 = random.choices(ranked_population[:top_elite_num*2], k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            next_generation.append(child)
        
        population = next_generation

    best_solution = population[0]
    return best_solution, calculate_cost(best_solution)

# Solve the mTSP
best_tour, best_cost = genetic_algorithm()
print("Best tour: ", best_tour)
print("Best cost: ", best_cost)