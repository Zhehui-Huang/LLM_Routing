import numpy as np
import math
from itertools import permutations

# Define the cities with their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating all permutations of the city indices except for the depot city 0
city_indices = list(cities.keys())[1:]
perm = permutations(city_indices)

# Function to find the shortest possible tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    for tour in perm:
        # Calculate the total distance including the return to the depot city 0
        total_distance = calc_distance(0, tour[0]) + calc_distance(tour[-1], 0)
        for i in range(len(tour) - 1):
            total_distance += calc_distance(tour[i], tour[i + 1])
        
        # Update the shortest tour found
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
    
    # Return the tour starting and ending at the depot city 0
    if best_tour:
        best_tour = [0] + list(best_tour) + [0]
    return best_tour, min_distance

# Execute the function to find the shortest tour
tour, total_cost = find_shortest_tour()

# Output the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")