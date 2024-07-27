import numpy as np
from math import sqrt
import random

# Define the coordinates of the cities
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def euclidean_distance(c1, c2):
    return sqrt((coordinates[c1][0] - coordinates[c2][0])**2 + (coordinates[c1][1] - coordinates[c2][1])**2)

# Create the distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i, j] = euclidean_distance(i, j)

# Initialize tours using Nearest Neighbor heuristic
def nearest_neighbor(start_city):
    remaining_cities = set(range(1, len(coordinates)))  # Exclude depot initially.
    tour = [start_city]
    current_city = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distance_matrix[current_city, x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    return tour

# Nearest Neighbor Initial Tours
tour1 = nearest_neighbor(0)  # Robot 0 starts at depot 0
tour2 = nearest_neighbor(1)  # Robot 1 starts at depot 1

# Function to calculate the tour cost
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Randomly swap two cities in the tour to generate new tour
def generate_new_tour(old_tour):
    new_tour = old_tour[:]
    a, b = random.sample(range(1, len(new_tour)-1), 2)  # Randomly pick two indices for city swap
    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return new_tour

# Simple Tabu Search for each robot
def tabu_search(initial_tour, iterations=100, tabu_size=10):
    current_tour = initial_tour
    best_tour = initial_tour[:]
    best_cost = calculate_tour_cost(best_tour)
    tabu_list = []

    for _ in range(iterations):
        candidate_tour = generate_new_tour(current_tour)
        candidate_cost = calculate_tour_cost(candidate_tour)

        if candidate_tour not in tabu_list and candidate_cost < best_cost:
            best_tour = candidate_tour[:]
            best_cost = candidate_cost
            tabu_list.append(candidate_tour)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
        else:
            current_tour = candidate_tour
    
    return best_tour

# Perform Tabu Search on each tour
optimized_tour1 = tabu_search(tour1)
optimized_tour2 = tabu_search(tour2)

# Calculate and print costs as required
cost1 = calculate_tour_cost(optimized_tour1)
cost2 = calculate_tour_cost(optimized_tour2)

print(f"Robot 0 Tour: {optimized_tour1}")
print(f"Robot 0 Total Travel Cost: {cost1:.2f}\n")
print(f"Robot 1 Tour: {optimized_tour2}")
print(f"Robot 1 Total Travel Cost: {cost2:.2f}\n")
print(f"Overall Total Travel Cost: {cost1 + cost2:.2f}")