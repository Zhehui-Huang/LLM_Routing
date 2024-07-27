import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, randint, random
from operator import attrgetter

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Set number of cities in the tour (including the depot)
num_cities_in_tour = 13

# Calculate distance matrix
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])

class Individual:
    def __init__(self, route):
        self.route = route
        self.total_distance = self.calculate_total_distance()
    
    def calculate_total_distance(self):
        distance = 0
        for i in range(len(self.route) - 1):
            distance += distances[self.route[i]][self.route[i + 1]]
        return distance
    
    def mutate(self, mutation_rate=0.2):
        if random() < mutation_rate:
            idx1, idx2 = sample(range(1, num_cities_in_tour - 1), 2)
            self.route[idx1], self.route[idx2] = self.route[idx2], self.route[idx1]
            self.total_distance = self.calculate_total_distance()

def crossover(parent1, parent2):
    start, end = sorted(sample(range(1, num_ciphers_in_tour-1), 2)) legal_index=[]
    
    offspring1 = [None]*num_cities_in_tour
    offspring1[start:end + 1] = parent1.route[start:end + 1]
    
    for position in list(range(end + 1, num_cities_in_tour)) + list(range(0, end + 1)):
        for elem in parent2.route:
            if elem not in offspring1:
                offspring1[position] = elem
                break
    
    return Individual(offspring1)

def initialize_population(pop_size=100):
    population = []
    for _ in range(pop_size):
        route = sample(cities.keys(), num_cities_in_tour)
        if 0 not in route:
            route[0] = 0  # Ensure depot is included
        population.append(Individual(route))
    return population

def genetic_algorithm(population, generations=500):
    for _ in range(generations):
        population = sorted(population, key=attrgetter('total_distance'))
        new_population = population[:2]  # Elitism: carry the best 2 forward
        
        while len(new_population) < len(population):
            parent1, parent2 = sample(population[:50], 2)  # Tournament selection
            child1 = crossover(parent1, parent2)
            child1.mutate()
            new_population.append(child1)
        
        population = new_population
    
    return min(population, key=attrgetter('total_distance'))

# Initialize and run the genetic algorithm
population = initialize_population()
best_individual = genetic_algorithm(population)

# Output results
print("Tour:", best_individual.route)
print("Total travel cost:", best_individual.total_distance)