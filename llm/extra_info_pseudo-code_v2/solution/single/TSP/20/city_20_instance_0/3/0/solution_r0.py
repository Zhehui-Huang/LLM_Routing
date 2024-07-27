import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Euclidean distance calculation
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate all distances between each city
dist_matrix = [[distance(cities[i], cities[j]) for j in range(20)] for i in range(20)]

# Apply heuristic: Nearest Neighbor
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_terms_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to start city to complete the tour
    tour.append(start_city)
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Get the tour and calculate its total cost
tour = nearest_neighbor_tour(0)
tour_cost = calculate_tour_cost(tour)

# Output the results in the specified format
print("Tour:", tour)
print("Total travel cost:", tour_cost)