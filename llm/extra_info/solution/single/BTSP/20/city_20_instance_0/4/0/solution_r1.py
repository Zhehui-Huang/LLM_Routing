import numpy as np
from scipy.spatial import distance

# Define city coordinates
city_coords = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def calculate_distance(city1, city2):
    # Calculates Euclidean distance between two city coordinates
    return distance.euclidean(city_coords[city1], city_coords[city2])

def initial_tour():
    # Initial tour starting at the depot city, visiting all cities once, and returning to the depot
    return list(city_coords.keys())

def calculate_total_cost(tour):
    # Calculate total travel cost of the tour
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def two_opt(tour):
    # Performs the 2-opt optimization to minimize the maximum distance in the tour
    best_tour = tour
    improved = True
    n = len(tour)
    
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1: continue  # Consecutive edges, no changes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if max(calculate_distance(new_tour[k], new_tour[k+1]) for k in range(len(new_tour)-1)) < \
                   max(calculate_distance(best_tour[k], best_tour[k+1]) for k in range(len(best_tour)-1)):
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# Find an initial tour
tour = initial_tour()
tour.append(tour[0])  # Return to the depot

# Optimization using 2-opt
optimized_tour = two_opt(tour)

# Calculate the final tour cost details
total_distance = calculate_total_code(optimized_tour)
max_leg_distance = max(calculate_distance(optimized_tour[i], optimized_tour[i+1]) for i in range(len(optimized_tour)-1))

print("Tour:", optimized_tour)
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_leg_distance:.2f}")