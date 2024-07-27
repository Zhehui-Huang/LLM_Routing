import numpy as np
import itertools

# Coordinates of the cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities to visit including the depot
k = 13

# Calculate distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all combinations of k-1 out of the 19 non-depot cities
combinations = itertools.combinations(range(1, 20), k-1)

# Minimum distance and corresponding optimal tour initialization
min_distance = float('inf')
optimal_tour = None

# Check each combination
for comb in combinations:
    # Final tour considers depot and selected cities
    tour = [0] + list(comb) + [0]
    
    # Calculate the cost for a straightforward tour through cities in this combination
    current_distance = 0
    for i in range(len(tour) - 1):
        current_distance += distance(cities[tour[i]], cities[tour[i+1]])
    
    # If found a shorter tour, update the minimum and optimal tour
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = tour

# Return the results
print("Tour:", optimal_tour)
print("Total travel cost:", min_distance)