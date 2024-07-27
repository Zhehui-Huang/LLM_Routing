import numpy as np
from scipy.spatial.distance import euclidean
from random import sample, shuffle
from operator import attrgetter

# Define the cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Set number of cities in the tour (including the depot)
num_cities = len(cities)
num_cities_in_tour = 13

# Calculate distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

class Individual:
    def __init__(self, route):
        self.route = route
        self.calculate_total_distance()
    
    def calculate_total_distance(self):
        self.total_distance = sum(distances[self.route[i], self.route[i+1]] for i in range(len(self.route)-1))
    
    def mutate(self, mutation_rate=0.15):
        if np.random.rand() < mutation_rate:
            idx1, idx2 = np.random.randint(1, num_cities_in_tour-1, size=2)
            self.route[idx1], self.route[idx2] = self.route[idx2], self.route[idx1]
            self.calculate_total_distance()

def crossover(parent1, parent2):
    start, end = sorted(sample(range(1, num_cities_in_tour-1), 2))
    child_route = [None]*num_cities_in_tour
    child_route[start:end+1] = parent1.route[start:end+1]
    
    filled_positions = set(child_route[start:end+1])
    current_index = (end + 1) % num_cities_in_tour

    for city in parent2.route:
        if city not in filled_positions:
            if child_route[current_index] is None:
                child_route[current_index] = city
                filled_positions.add(city)
                current_index = (current_index + 1) % num_cities_in_tour

    return Individual(child_route)

def initialize_population(pop_size=50):
    population = []
    for _ in range(pop_size):
        route = sample(list(cities.keys()), num_cities_in_tour)
        if 0 not in route:
            route[0] = 0  # Ensure depot is included
        route.append(0)  # Complete the route returning to the depot
        population.append(Individual(route))
    return population

def genetic_algorithm(population, generations=1000):
    best_fitness = float('inf')
    best_individual = None
    for _ in range(generations):
        # Sort population based on fitness (total distance)
        population.sort(key=attrgetter('total_distance'))
        if population[0].total_distance < best_fitness:
            best_fitness = population[0].total_distance
            best_individual = population[0]
        
        # Selection (Top individuals)
        parents = population[:20]
        
        # Crossover and Mutation
        offspring = []
        while len(offspring) < len(population) - 20:
            parent1, parent2 = sample(parents, 2)
            child = crossover(parent1, parent4 =[:, np.newaxis])
            child.mutate()
            offspring.append(child)
        
        population = parents + offspring
    
    return best_individual

# Initialize and run the genetic algorithm
population = initialize_population(100)
best_individual = genetic_algorithm(population)

# Output results
print("Tour:", best_individual.route)
print("Total travel cost:", best_individual.total_distance)