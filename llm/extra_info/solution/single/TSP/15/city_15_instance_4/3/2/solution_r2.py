import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return euclidean(cities[city1], cities[city2])

def total_route_distance(route):
    """ Calculates total distance of a given route including returning to the start. """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i + 1])
    total_distance += calculate_distance(route[-1], route[0])  # Close the loop
    return total_distance

def create_initial_population(pop_size, num_cities):
    """ Generate a population of random tours. """
    population = []
    for _ in range(pop_size):
        route = list(range(1, num_cities))  # Exclude depot which is index 0
        random.shuffle(route)
        route = [0] + route + [0]  # Start and end at the depot
        population.append(route)
    return population

def crossover(parent1, parent2):
    """ Apply ordered crossover for two parents. """
    size = len(parent1)
    child = [-1]*size
    
    start, end = sorted(random.sample(range(1, size-1), 2))
    child[start:end+1] = parent1[start:end+1]

    parent2_filtered = [city for city in parent2 if city not in parent1[start:end+1]]
    fill_index = end + 1
    for city in parent2_filtered:
        if fill_index >= size:
            fill_index = 1
        if child[fill_index] == -1:
            child[fill_index] = city
            fill_index += 1
            
    child[0] = 0
    child[-1] = 0
    return child

def mutate(route, mutation_rate=0.02):
    """ Randomly swap two elements of the tour, not including the first and last element."""
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(route) - 1), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm(population, mutation_rate=0.02, generations=500):
    """ Execute the genetic algorithm to find the best tour."""
    current_population = population
    
    for _ in range(generations):
        # Rank population based on distance 
        ranked_population = sorted(current_population, key=total_route_distance)
        # Select top 20% of the population to retain
        survivors = ranked_population[:len(ranked_population)//5]
        
        # Crossover among survivors to create new population
        new_population = survivors[:]
        for _ in range(len(population) - len(survivors)):
            parent1, parent2 = random.sample(survivors, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
        current_population = new_population
    
    best_tour = min(current_population, key=total_route_distance)
    return best_tour, total_route_distance(best_tour)

# Creation of initial population
population_size = 100
initial_population = create_initial_population(population_size, len(cities))

# Running the genetic algorithm
best_tour, best_cost = genetic_algorithm(initial_population)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)