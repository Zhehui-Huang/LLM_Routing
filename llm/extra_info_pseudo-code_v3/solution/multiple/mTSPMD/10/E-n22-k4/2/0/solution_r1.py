import numpy as np
import random
from operator import attrgetter

# City coordinates (depots + cities)
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

depots = {0: 0, 1: 1, 2: 2, 3: 3}

# Compute Euclidean distance matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = np.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
    return distances

distances = calculate_distances(cities)

class Individual:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = self.calculate_fitness()
    
    def calculate_fitness(self):
        total_cost = 0
        last_city = depots[0]
        for i, city in enumerate(self.genome):
            total_cost += distances[last_city][city]
            last_city = city
        total_cost += distances[last_city][depots[0]]  # Return to depot
        return total_cost
    
    def mutate(self):
        idx1, idx2 = random.sample(range(len(self.genome)), 2)
        self.genome[idx1], self.genome[idx2] = self.genome[idx2], self.genome[idx1]
        self.fitness = self.calculate_fitness()  # Recalculate fitness
    
    def __repr__(self):
        return f"{self.genome} - {self.fitness}"

def initialize_population(pop_size, num_cities):
    return [Individual(random.sample(range(4, num_cities), num_cities - 4)) for _ in range(pop_size)]

def crossover(parent1, parent2):
    # Single point crossover
    point = random.randint(1, len(parent1.genome) - 2)
    child_genome = parent1.genome[:point] + parent2.genome[point:]
    return Individual(child_genome)

def evolve_population(population):
    new_population = []
    sorted_pop = sorted(population, key=attrgetter('fitness'))
    # Elitism: keep the top individuals
    elite_count = int(len(population) * 0.1)
    new_population.extend(sorted_pop[:elite_count])
    
    # Crossover and mutation
    while len(new_population) < len(population):
        parent1, parent2 = random.choices(sorted_pop[:int(len(population) * 0.5)], k=2)
        child = crossover(parent1, parent2)
        if random.random() < 0.1:
            child.mutate()
        new_population.append(child)
        
    return new_population

# Genetic Algorithm
def genetic_algorithm(pop_size, generations):
    population = initialize_population(pop_size, len(cities))
    for _ in range(generations):
        population = evolve_population(population)
    
    best_individual = sorted(population, key=attrgetter('fitness'))[0]
    return best_individual, best_individual.fitness

# Parameters
population_size = 50
generation_count = 100

# Running the algorithm
best_solution, best_cost = genetic_algorithm(population_size, generation_count)
print("Best Tour (with depots):", [depots[0]] + best_solution.genome + [depots[0]])
print("Total Travel Cost:", best_cost)