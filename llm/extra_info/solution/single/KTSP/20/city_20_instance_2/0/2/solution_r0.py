import math
from itertools import permutations

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_shortest_tour(cities):
    num_cities = len(cities)
    min_tour, min_cost = None, float("inf")
    
    # Try every permutation of city visits (excluding city 0 which is the depot and added by default to start/end)
    for tour in permutations(range(1, num_cities)):
        total_distance = 0
        current_city = 0
        
        # Check only tours that result in exactly 10 cities (including the depot)
        if len(tour) == 9:
            possible_tour = [0] + list(tour) + [0]
            
            for i in range(len(possible_tour) - 1):
                total_distance += calculate_distance(cities[possible_tour[i]], cities[possible_tour[i+1]])
            
            # If found a new minimum tour
            if total_rotation < min_cost:
                min_cost = total_distance
                min_tour = possible_tour
    
    return min_tour, min_cost

# Coordinates of depot and cities
coordinates = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Find shortest tour visiting exactly 10 cities including depot
tour, cost = find_shortest_tour(coordinates)

print("Tour:", tour)
print("Total travel cost:", cost)