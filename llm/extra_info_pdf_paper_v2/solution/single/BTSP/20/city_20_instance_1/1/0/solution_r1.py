import math
from itertools import permutations

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Prepare city coordinates data
coords = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def find_btsp_solution(coords):
    best_tour = None
    min_max_distance = float('inf')
    total_distance = 0
    
    cities = list(coords.keys())
    
    # Simple exhaustive search to find the best permutation that minimizes the maximum leg distance
    for perm in permutations(cities[1:]):  # Exclude the depot city from permutations
        tour = [0] + list(perm) + [0]
        max_distance = 0
        tour_cost = 0
        
        for i in range(len(tour) - 1):
            dist = calculate_euclidean_distance(coords[tour[i]], coords[tour[i + 1]])
            tour_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            total_distance = tour_cost

    return best_tour, total_distance, min_max_distance

# Find the best solution according to criteria
tour, total_cost, max_distance = find_btsp_solution(coords)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))