import itertools
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Groups of cities (1-indexed to 0-indexed)
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all possible combinations of visiting one city from each group
possible_tours = itertools.product(*groups)

min_distance = float('inf')
optimal_tour = None

# Check all possible tours
for tour in possible_tours:
    # Combine with the starting/ending depot city
    full_tour = [0] + list(tour) + [0]
    # Calculate the distance of this complete tour
    tour_distance = sum(euclidean_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
    
    # Update the minimum distance found and the corresponding tour
    if tour_distance < min_distance:
        min_distance = tour_distance
        optimal_tour = full_tour

# Output the optimal tour found and its total distance
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_distance}")