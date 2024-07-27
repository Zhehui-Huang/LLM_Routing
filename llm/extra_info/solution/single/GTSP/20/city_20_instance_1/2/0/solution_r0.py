import itertools
import math

# City coordinates
city_coords = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []
    
    # Consider all permutations from each group
    for tour in itertools.product(*groups):
        # Include the start/end point to the tour
        tour = [0] + list(tour) + [0]
        
        # Calculate the distance of this tour permutation
        total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check for a new minimum distance tour
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
            
    return best_tour, min_distance

# Finding the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")