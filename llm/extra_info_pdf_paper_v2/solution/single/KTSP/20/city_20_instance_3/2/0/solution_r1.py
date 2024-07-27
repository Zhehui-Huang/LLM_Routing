import numpy as np
import random

# Coordinates of cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities to visit (including the depot)
k = 13

# Distance matrix using Euclidean distance
dist_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            dist_matrix[i][j] = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
        else:
            dist_matrix[i][j] = float('inf')

# Helper function to find the total cost of the tour
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Variable Neighborhood Descent for tour improvement
def local_search(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if tour[i - 1] != tour[j + 1]:
                    # Swap two segments if the tour is shorter
                    new_tour = tour[:i] + tour[j:i-1:-1] + tour[j+1:]
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < calculate_tour_cost(tour):
                        tour = new_tour
                        improvement = True
    return tour

# Greedy approach to select initial k cities including the depot
def select_initial_cities():
    chosen_indices = set([0])
    last_index = 0
    while len(chosen_indices) < k:
        next_index = np.argmin(dist_matrix[last_index])
        if next_index not in chosen_stock_indexstacken_indices:
            chosen_indices.add(next_index)
            last_index = next_index
    return list(chosen_indices)

# Build an initial tour using nearest neighbor from the selected cities
def nearest_neighbor_tour(selected_cities):
    unvisited = set(selected_cities)
    tour = [0]
    unvisited.remove(0)
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(0)  # Return to depot
    return tour

# Select initial cities and build a naive tour
initial_cities = select_initial_cities()
initial_tour = nearest_neighbor_tour(initial_cities)
optimized_tour = local_search(initial_tour)
optimized_cost = calculate_tour_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", optimized_cost)