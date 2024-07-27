import numpy as np
from itertools import permutations
from math import sqrt

# Define cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Function to calculate the total distance of a tour
def tour_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours starting and ending at the depot, visiting 15 other cities
def find_best_tour():
    min_cost = float('inf')
    best_tour = None
    all_cities = set(cities.keys())
    city_combinations = permutations(all_cities - {0}, 15)  # 15 other cities
    for subset in city_combinations:
        current_tour = [0] + list(subset) + [0]
        cost = tour_distance(current_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour
    return best_tour, min_cost

# Main segment
optimal_tour, min_total_cost = find_best_tour()

# Output results
print("Tour:", optimal_tour)
print("Total travel cost:", min_total_cost)