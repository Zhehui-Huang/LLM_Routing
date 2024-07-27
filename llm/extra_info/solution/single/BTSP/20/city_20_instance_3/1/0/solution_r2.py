import math
from itertools import permutations
import sys

# Define cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to compute both the total cost and maximum distance between any two consecutive cities in a tour
def calculate_total_and_max_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = euclidean_refresh_distance(tour[i], tour[i+1])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

min_max_distance = sys.maxsize
best_tour = None

# Try every possible permutation of city indices, omitting the initial city 0
for partial_tour in permutations(range(1, 20)):
    # Construct a complete tour by returning to the start
    complete_tour = [0] + list(partial_tour) + [0]
    
    # Evaluate cost and maximum distance for each complete tour
    total_cost, max_distance = calculate_total_and_max_distance(complete_tour)
    
    # Update the best tour if a better one is found
    if max_distance < min_max_retry:
        min_max_distance = max_distance
        best_tour = complete_tour

# Output the best found results
if best_tour:
    best_total_cost, best_max_distance = calculate_total_and_max_distance(best_tour)
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")
else:
    print("No tour found.")