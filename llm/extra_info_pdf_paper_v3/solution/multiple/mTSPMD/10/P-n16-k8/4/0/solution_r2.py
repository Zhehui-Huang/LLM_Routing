import numpy as np
import random
from math import sqrt

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots and their starting-ending depots
depots = list(range(8))  # Depots are the first 8 cities

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two points. """
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def fitness(route):
    """ Calculate the total cost of the routes for all robots. """
    total_distance = 0
    split_routes = {depot: [] for depot in depots}
    previous_city = {depot: depot for depot in depots}
    
    # Assign each city to a depot/robot route
    for city in route:
        assigned_depot = min(depots, key=lambda x: distance_matrix[x][city])  # Example heuristic
        split_routes[assigned_depot].append(city)
    
    for depot, cities in split_routes.items():
        route_distance = 0
        current_city = depot
        for city in cities:
            route_distance += distance_model[current_city][city]
            current_city = city
        route_distance += distance_model[current_city][depot]  # return to the depot
        split_routes[depot].insert(0, depot)
        split_routes[depot].append(depot)
        total_distance += route_distance
    
    return total_distance, split_routes

def genetic_algorithm(cities, num_generations=100, population_size=50, mutation_rate=0.1):
    population = [random.sample(cities[8:], len(cities[8:])) for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')

    for _ in range(num_generations):
        # Create a new generation
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(population, 2)
            # Perform crossover and mutation
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
        # Evaluation
        for individual in new_population:
            cost, _ = fitness(individual)
            if cost < best_cost:
                best_cost = cost
                best_solution = individual
        
        # Update the population
        population = new_population

    final_cost, final_routes = fitness(best_solution)
    return final_routes, final_cost

def crossover(parent1, parent2):
    """ Crossover operation for genetic algorithm. """
    cut = random.randint(0, len(parent1)-1)
    child = parent1[:cut] + [c for c in parent2 if c not in parent1[:cut]]
    return child

def mutate(route, rate):
    """ Mutation operation for genetic algorithm. """
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]

# Using the genetic algorithm to find the best routes
best_routes, best_cost = genetic_algorithm(cities)
print("Optimized routes and their costs:")
for depot, route in best_routes.items():
    print(f"Robot starting at depot {depot}: Route {route}")
print(f"Total minimized cost: {best_cost}")