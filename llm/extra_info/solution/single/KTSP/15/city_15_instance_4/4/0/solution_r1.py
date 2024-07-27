import math
from itertools import permutations

# Coordinates for each city
city_coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Calculating Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to compute permutations of selected cities
def find_best_tour():
    minimum_cost = float('inf')
    best_path = []
    # We select city indices 0 through 14, but as we know, city 0 is always included and is the depot
    all_indices = list(range(15))
    # Generate combinations of 11 cities plus the depot city (total 12), starting from 1 excluding depot 0
    for indices in permutations(all_indices[1:], 11):
        # Always start and end at the depot
        current_permutation = [0] + list(indices) + [0]
        # Calculate cost for this permutation
        current_cost = 0
        for j in range(len(current_permutation) - 1):
            current_cost += distance(city_coords[current_permutation[j]], city_coords[current_permutation[j + 1]])
        # If found a new minimum, update the best path and cost
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_path = current_permutation
            
    return best_path, minimum_cost

# Find the best TSP tour
tour, total_cost = find_best_tour()

# Output the results
print("Tour:", tour)
print("Total travel ring cost:", total_cost)