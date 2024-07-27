import math
from itertools import permutations

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_path_distance(tour, cities):
    """ Calculate the total path distance of the given tour. """
    distance = 0
    n = len(tour)
    for i in range(n-1):
        distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return distance

def find_shortest_tour(cities):
    """ Determine the optimal tour using a brute-force approach by checking all permutations. """
    n = len(cities)
    all_permutations = permutations(range(1, n))  # permutations of city indices, excluding the depot
    shortest_tour = None
    min_distance = float('inf')

    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]  # start and end at the depot
        current_distance = total_path_distance(current_tour, cities)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour

    return shortest_tour, min_distance

# Coordinates of each city
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Find the shortest tour and calculate the tour cost
tour, cost = find_shortest_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))