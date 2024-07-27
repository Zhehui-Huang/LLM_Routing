import numpy as np
import random
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}
number_of_robots = 4
depot_cities = [0]

def euclidean_distance(a, b):
    return np.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Initialize Population
def initialize_population(pop_size):
    population = []
    city_list = list(cities.keys())
    for _ in range(pop_size):
        random.shuffle(city_list)
        population.append(city_list)
    return population

# Fitness Function
def evaluate_fitness(chromosome):
    cost = 0
    start = depot_cities[0]  # assuming all robots start from the same depot for simplicity
    path = [start] + chromosome + [start]
    cost = total_tour_cost(path)
    return cost

# Genetic Operations
def crossover(parent1, parent2):
    size = len(parent1)
    point1, point2 = sorted(random.sample(range(size), 2))
    temp = parent1[point1:point2]
    child = [city for city in parent2 if city not in temp]
    return child[:point1] + temp + child[point1:]

def mutate(chromosome):
    idx1, idx2 = random.sample(range(len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

# Genetic Algorithm
def genetic_algorithm(max_generations, pop_size):
    population = initialize_population(pop_size)
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(max_generations):
        new_population = []
        population = sorted(population, key=evaluate_fitness)
        if evaluate_fitness(population[0]) < best_cost:
            best_cost = evaluate_fitness(population[0])
            best_solution = population[0]
        
        # Crossover and Mutation
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population[:pop_size//2], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Mutation rate
                mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_solution, best_cost

# Running the Genetic Algorithm
best_tour, best_tour_cost = genetic_algorithm(100, 50)
start = depot_cities[0]
final_tour = [start] + best_tour + [start]
print(f"Robot 0 Tour: {final_tour}")
print(f"Robot 0 Total Travel Cost: {best_tour_cost}")