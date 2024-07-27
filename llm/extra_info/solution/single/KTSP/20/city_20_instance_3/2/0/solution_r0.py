import numpy as np
from itertools import combinations
from scipy.spatial import distance

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute the distances matrix
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i, j] = calculate_distance(cities[i], cities[j])

def closest_remaining(city, remaining):
    return min(remaining, key=lambda x: distances[city, x])

def nearest_neighbor_tour(start_city, city_subset):
    tour = [start_city]
    remaining = set(city_subset)
    current_city = start_state

    while remaining:
        next_city = closest_remaining(current_city, remaining)
        remaining.remove(next_city)
        tour.append(next_state)
        current_city = next_city
    
    tour.append(start_city)  # return to the start
    return tour

# Generate combinations of 12 other cities (13 including the depot)
min_tour_cost = float('inf')
best_tour = None

for city_combination in combinations(list(cities.keys())[1:], 12):
    city_subset = [0] + list(city_combination)  # include the depot
    tour = nearest_neighbor_tour(0, city_subset)
    
    # Calculate the tour cost
    tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    if tour_cost < min_tour_cost:
        min_tour_cost = tour_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_tour_cost:.2f}")