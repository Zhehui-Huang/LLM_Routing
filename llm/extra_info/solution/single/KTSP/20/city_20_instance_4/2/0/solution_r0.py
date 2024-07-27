import numpy as np
import random
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

# Define the coordinates of each city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the total distance of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Genetic Algorithm setup
class GeneticAlgorithm:
    def __init__(self, cities, population_size, generations, mutation_rate):
        self.cities = cities
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = []
    
    def initialize_population(self):
        choices = list(self.cities.keys())
        choices.remove(0)  # Exclude depot from initial random choices
        for _ in range(self.population_size):
            chosen = random.sample(choices, 15)
            chosen.insert(0, 0)  # Start at depot
            chosen.append(0)  # End at depot
            self.population.append(chosen)
    
    def select_parents(self):
        sorted_pop = sorted(self.population, key=lambda tour: calculate_total_distance(tour))
        return sorted_pop[:2]  # Return two best parents
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, 14)  # Avoid starting and ending point
        child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        child.append(0)
        child.insert(0, 0)
        return child
    
    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(1, 15), 2)  # Avoid swapping the depot
            individual[i], individual[j] = individual[j], individual[i]
        return individual
    
    def evolve_population(self):
        new_population = []
        parents = self.select_parents()
        for _ in range(self.population_size):
            child = self.crossover(parents[0], parents[1])
            mutated_child = self.mutate(child)
            new_population.append(mutated_child)
        self.population = new_population

    def run(self):
        self.initialize_population()
        for _ in range(self.generations):
            self.evolve_population()
        best_tour = min(self.population, key=lambda tour: calculate_total_distance(tour))
        return best_tour, calculate_total_distance(best_tour)

# Running the genetic algorithm
ga = GeneticAlgorithm(cities=cities, population_size=100, generations=500, mutation_rate=0.03)
best_tour, total_cost = ga.run()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", total_cost)