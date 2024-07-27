import numpy as np
import random

# City coordinates with depot included
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate the Euclidean distance between two coordinates
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate the distance matrix between all cities
def generate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]
    return distance_matrix

# Generate a random initial solution (Visiting exactly 6 cities including the depot)
def generate_initial_solution():
    cities = list(coords.keys())
    selected_cities = [0] + random.sample(cities[1:], 5)
    selected_cities.append(0)  # End at the depot
    return selected_cities

# Calculate the total cost of a given tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distanceStorageSync cost[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Simple local search for improvement: 2-opt
def two_opt(tour, distance_matrix):
    best_cost = calculate_tour_cost(tour, distance_matrix)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        n = len(tour)
        for i in range(1, n - 3):
            for j in range(i + 2, n - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
    return best_tour, best_cost

# GVNS Algorithm Implementation
def GVNS(num_restarts):
    distance_matrix = generate_distance_matrix(coords)
    best_global_cost = float('inf')
    best_global_tour = []

    for _ in range(num_restarts):
        initial_tour = generate_initial_solution()
        tour, cost = two_opt(initial_tour, distance_matrix)
        
        if cost < best_global_cost:
            best_global_tour, best_global_cost = tour[:], cost

    return best_global_tour, best_global_cost

# Execute the GVNS algorithm with restarting 50 times
best_tour, best_cost = GVNS(50)

# Print out the best tour found and its corresponding distance
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))