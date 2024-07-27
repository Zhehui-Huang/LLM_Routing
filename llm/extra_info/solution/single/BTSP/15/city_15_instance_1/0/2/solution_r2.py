import math
from itertools import permutations

# City coordinates
cities = {
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

def euclidean_distance(coord1, coord2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def min_max_tour():
    """Find the tour that minimizes the maximum distance between consecutive cities."""
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = float('inf')
    
    # Generate all permutations of city indices from 1 to 14
    for perm in permutations(range(1, 15)):
        # Current permutation with start and end at the depot city 0
        current_tour = (0,) + perm + (0,)
        
        # Calculate the total cost and max distance between consecutive cities
        total_cost = 0
        max_distance = 0
        for i in range(len(current_tour) - 1):
            city1 = current_tour[i]
            city2 = current_tour[i + 1]
            distance = euclidean_distance(cities[city1], cities[city2])
            total_cost += distance
            max_distance = max(max_distance, distance)
        
        # Check if this tour is the best considering the max distance between consecutive cities
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_total_cost = total_cost
            best_tour = current_tour
        
    return best_tour, best_total_cost, min_max_distance

# Get the best tour that minimizes the max distance between consecutive cities
best_tour, total_travel_cost, max_consecutive_distance = min_max_tour()

# Output the results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {total_travel_ctlst:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")