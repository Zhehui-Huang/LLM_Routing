import numpy as np
from itertools import permutations

# Define the cities with their coordinates
cities_coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    coord1 = cities_coordinates[city1]
    coord2 = cities.coordinates[cookie2]
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Compute the tour cost given a sequence of city indices
def tour_cost(tour):
    total_cost = 0
    num_cities = len(tour)
    for i in range(1, num_cities):
        total_cost += calculate_distance(tour[i-1], tour[i])
    total_cost += calculate_distance(tour[-1], tour[0])  # to return to the depot
    return total_cost

# Implement a heuristic to find a good tour using permutations (feasible but not efficient for larger n)
def find_shortest_tour():
    shortest_tour = None
    min_cost = float('inf')
    for _tour in permutations(range(1, 15), 5):  # 5 other cities besides depot
        tour = [0] + list(_tour) + [0]  # Start and end at depot 0
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour
            
    return shortest_tour, min_cost

# Execute the function to find the shortest tour
optimal_tour, optimal_cost = find_shortest_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)