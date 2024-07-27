import numpy as np
import random
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities and their locations
city_locations = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return euclidean(city_locations[city1], city_locations[city2])

def total_distance(tour):
    """ Calculate the total distance of a tour. """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find a reasonable tour using permutations (Note: not efficient for large number of cities)
def find_shortest_tour():
    cities = list(city_locations.keys())
    shortest_tour = None
    min_distance = float('inf')

    for perm in permutations(cities[1:]):  # excluding the depot from permutations
        current_tour = [0] + list(perm) + [0]
        current_distance = total_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour

    return shortest_tour, min_distance

# Calculate the shortest tour (warning: can be very slow as number of cities increases)
tour, cost = find_shortest_tour()

print("Tour:", tour)
print("Total travel cost:", cost)