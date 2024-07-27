import numpy as np
import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calc_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_shortest_tour():
    """ Generate permutations and find the shortest tour """
    city_indices = list(cities.keys())[1:]  # Exclude the depot city from permutation
    min_distance = float('inf')
    best_tour = None
    
    for tour in permutations(city_indices):
        # Start and end at the depot city 0
        total_distance = calc_distance(0, tour[0]) + calc_distance(tour[-1], 0)
        
        # Calculate the total distance for the current tour:
        for i in range(len(tour) - 1):
            total_distance += calc_distance(tour[i], tour[i + 1])
        
        # Check if the current tour is better (i.e., has less distance) than what we have found before
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
    
    # wrap the best tour with the depot as starting and ending point
    best_tour = [0] + list(best_tour) + [0]
    return best_tour, min_distance

# Find the shortest tour and calculate its cost
tour, total_cost = find_shortest_tour()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")