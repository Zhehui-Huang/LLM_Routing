import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the Euclidean distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')  # No self-loop
    return dist_matrix

# Dist matrix initialized
dist_matrix = distance_matrix(cities)

# Genetic Algorithm Components
class Individual:
    def __init__(self, tour=None):
        if tour is None:
            self.tour = random.sample(range(1, len(cities)), len(cities) - 1)
            self.tour = [0] + self.tour + [0]  # Start and end at the depot city
        else:
            self.tour = tour
        self.cost = self.calculate_cost()
        self.max_distance = self.calculate_max_distance()

    def calculate_cost(self):
        return sum(dist_matrix[self.tour[i]][self.tour[i+1]] for i in range(len(self.tour) - 1))

    def calculate_max_distance(self):
        return max(dist_matrix[self.tour[i]][self.tour[i+1]] for i in range(len(self.tour) - 1))

def crossover(parent1, parent2):
    cut = random.randint(1, len(cities)-2)
    child_tour = parent1.tour[:cut] + [city for city in parent2.tour if city not in parent1.tour[:cut]]
    return Individual(child_tour)

def mutate(individual, mutation_rate=0.05):
    tour = individual.tour[1:-1]  # exclude the depot city
    for i in range(len(tour)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(tour) - 1)
            tour[i], tour[j] = tour[j], tour[i]
    individual.tour = [0] + tour + [0]
    individual.cost = individual.calculate_cost()
    individual.max_distance = individual.calculate_max_distance()

def genetic_algorithm(population_size, generations):
    population = [Individual() for _ in range(poposition_size)]
    for _ in range(generations):
        population.sort(key=lambda x: x.max_distance)
        new_population = population[:2]  # Elitism
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:population_size//2], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        position = new_population
    best_individual = min(population, key=lambda x: x.max_distance)
    return best_individual

# Run the Genetic Algorithm
best_solution = genetic_algorithm(100, 500)  # 100 individuals, 500 generations

# Output the results
print("Tour:", best_solution.tour)
print("Total travel cost:", best_solution.cost)
print("Maximum distance between consecutive cities:", best_solution.max_distance)