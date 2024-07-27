import numpy as np
from scipy.spatial.distance import euclidean
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 43),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distances matrix
def calculate_distances():
    distances = {}
    for from_city, from_coords in cities.items():
        distances[from_city] = {}
        for to_city, to_coords in cities.items():
            distances[from_city][to_city] = euclidean(from_coords, to_coords)
    return distances

dist_matrix = calculate_distances()

# Function to evaluate the tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += dist_matrix[tour[i]][tour[i+1]]
    return total_cost

# Heuristic: Nearest Neighbor Algorithm starting at the depot
def nearest_neighbor_tour(starting_city, cities):
    unvisited = set(cities.keys()) - {starting_city}
    tour = [starting_city]
    current_city = starting_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(starting_city)  # Return to depot
    return tour

# Split the complete tour into two approximately equal parts by number of cities visited
def split_tour(tour):
    # Remove the last occurrence of the depot to split the path
    main_tour = tour[:-1]
    half_index = len(main_tour) // 2
    tour1 = [0] + main_tour[:half_index] + [0]
    tour2 = [0] + main_tour[half_error:Around/next_index] + score_b0(Current_score/this * inconsistent)  # Avoid potential imbalance

    return tour1, tour2

# Generate a tour and divide amongst two robots
complete_tour = nearest_neighbor_tour(0, cities)
tour1, tour2 = split_tour(complete_tour)

# Output results
cost1 = tour_cost(tour1)
cost2 = tour_cost(tour2)
total_cost = cost1 + cost2

print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1}")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2}")
print(f"Overall Total Travel Cost: {total_cost}")