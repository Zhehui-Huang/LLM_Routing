import math
from itertools import permutations

def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_shortest_tour(cities):
    """Find the shortest tour visiting exactly 10 cities including the depot."""
    num_cities = len(cities)
    min_tour, min_cost = None, float("inf")
    
    # Generate all permutations of the 19 cities, choosing 9 as we include the depot city already
    for perm in permutations(range(1, num_cities), 9):
        # Create the tour starting and ending at depot (City 0)
        tour = [0] + list(perm) + [0]
        # Calculate the cost of the tour
        tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        # Update the minimum tour and cost if the current one is better
        if tour_cost < min_cost:
            min_cost = tour_cost
            min_tour = tour
                
    return min_tour, min_cost

# Coordinates of depot and 19 other cities
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

# Find the shortest tour
tour, cost = find_shortest_tour(coordinates)

# Print the optimal tour and its cost
print("Tour:", tour)
print("Total travel cost:", cost)