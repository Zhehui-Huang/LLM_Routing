import numpy as np
from math import sqrt
import random

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a random initial solution
def generate_initial_solution(cities, k):
    chosen_cities = random.sample(cities[1:], k-1)  # Sample k-1 cities since depot is already included
    tour = [cities[0]] + chosen_cities + [cities[0]]  # Start and end at the depot
    return tour

# Calculate the total distance of the tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

# Simple shake function by swapping two cities
def shake(tour):
    idx1, idx2 = np.random.randint(1, len(tour) - 1, 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

# Variable Neighborhood Descent
def vnd(tour):
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if i != j:
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    return new_tour
    return tour

# General Variable Neighborhood Search (GVNS)
def gvns(cities, k, nrst, termination_criterion):
    best_solution = generate_initial_solution(cities, k)
    best_cost = calculate_total_distance(best_solution)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        for _ in range(termination_criterion):
            shaken_solution = shake(current_solution[:])
            new_solution = vnd(shaken_solution)
            new_cost = calculate_total_distance(new_solution)
            
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
    
    return best_solution, best_cost

# Define cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Parameters
k = 7  # Number of cities to visit (including depot)
nrst = 10  # Number of restarts
termination_criterion = 100  # Maximum number of iterations for each restart

# Run GVNS
best_tour, best_distance = gvns(cities, k, nrst, termination_criterion)

# Output the results
city_indices = [cities.index(city) for city in best_tour]
print("Tour:", city_indices)
print("Total travel cost:", best_distance)