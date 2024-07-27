import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations
import random

# Define city coordinates
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    coord1 = city_coordinates[city1]
    coord2 = city_coordinates[city2]
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
n = len(city_coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean_distance(i, j)

# Genetic Algorithm Parameters
population_size = 50
number_of_cities_to_visit = 13
generations = 200
mutation_rate = 0.1

# Initialize population
def create_individual():
    cities = list(range(1, n))
    random.shuffle(cities)
    return [0] + cities[:number_of_cities_to_visit-1] + [0]

def create_population():
    return [create_individual() for _ in range(population_size)]

def calculate_total_distance(individual):
    total_dist = 0
    for i in range(len(individual) - 1):
        total_dist += distance_matrix[individual[i], individual[i+1]]
    return total_dist

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, number_of_cities_to_visit-1), 2))
    child = [None] * number_of_cities_to_visit
    child[start:end+1] = parent1[start:end+1]
    pointer = 1
    for city in parent2[1:number_of_cities_to_visit-1]:
        if None in child and city not in child:
            while child[pointer] != None:
                pointer += 1
            child[pointer] = city
    child[0] = 0
    child[-1] = 0
    return child

def mutate(individual):
    start, end = sorted(random.sample(range(1, number_of_cities_to_visit-1), 2))
    individual[start:end+1] = reversed(individual[start:end+1])

def genetic_algorithm():
    population = create_population()
    
    for gen in range(generations):
        population = sorted(population, key=calculate_total_distance)
        next_population = population[:2]  # Elitism
        
        while len(next_population) < population_size:
            parent1, parent2 = random.choices(population[:population_size//2], k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            next_population.append(child)
        
        population = next_population
    
    best_solution = sorted(population, key=calculate_total_distance)[0]
    return best_solution, calculate_total_distance(best_solution)

# Find the best tour and total travel cost
best_tour, best_cost = genetic_algorithm()

# Output the solution in the required format
print("Tour:", best_tour)
print("Total travel cost:", best_cost)