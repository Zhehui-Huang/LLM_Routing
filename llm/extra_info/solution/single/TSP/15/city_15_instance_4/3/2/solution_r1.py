import numpy as np
import random
from scipy.spatial.distance import euclidean

# Locations of all cities including the depot city
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return euclidean(cities[city1], cities[city2])

def total_route_distance(route):
    """ Calculates total distance of a given route. """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i + 1])
    total_distance += calculate_distance(route[-1], route[0])  # Return to the starting city
    return total_distance

def generate_initial_population(pop_size, num_cities):
    """ Generate initial population for the GA. """
    population = []
    for _ in range(pop_size):
        route = list(range(1, num_cities))
        random.shuffle(route)
        route = [0] + route + [0]  # Starting and ending at the depot city
        population.append(route)
    return population

def crossover(parent1, parent2):
    """ Perform Ordered Crossover (OX) between two parents. """
    child = [-1] * len(parent1)
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child[start:end+1] = parent1[start:end+1]
    
    filled_positions = set(parent1[start:end+1])
    place_position = (end + 1) % (len(parent1) - 1)
    for city in parent2 + parent2:
        if city not in filled_positions and place_position != len(parent1) - 1:
            child[place_position] = city
            filled_positions.add(city)
            place_position = (place_position + 1) % (len(parent1) - 1)
    child[0], child[-1] = 0, 0  # Ensure the tour starts and ends at the depot
    return child

def mutate(route, mutation_rate):
    """ Implements swap mutation on the route. """
    if random.random() < mutation(tion_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(route) - 1), 2))
        route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm(population, mutation_rate=0.01, generations=500):
    """ Runs the genetic algorithm. """
    current_gen = population
    for _ in range(generations):
        next_gen = []
        sorted_population = sorted(current_gen, key=total_route_distance)
        elite_size = len(sorted_population) // 5  # Take top 20% from the sorted population as elite
        next_gen.extend(sorted_population[:elite_size])
        
        while len(next_gen) < len(current_gen):
            parent1, parent2 = random.sample(sorted_population[:len(sorted_population) // 2], 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_gen.append(child)
        
        current_gen = next_gen
    
    best_route = min(current_gen, key=total_route_distance)
    return best_route, total_route_distance(best_route)

# Setup and run the Genetic Algorithm
num_cities = len(cities)
pop_size = 100
initial_population = generate_initial_population(pop_size, num_cities)
best_tour, best_distance = genetic_algorithm(initial_population)

# Output the solution
print("Tour:", best_tour)
print("Total travel cost:", best_distance)