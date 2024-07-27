import itertools
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of cities (including the depot city as index 0)
city_coords = [
    (14, 77), # Depot city
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Number of cities that needs to be visited (including the depot)
k = 7

def find_min_k_tsp_tour(city_coords, k):
    min_tour = None
    min_cost = float('inf')
    
    # All combinations of k-1 other cities (excluding depot)
    for cities in itertools.combinations(range(1, len(city_coords)), k-1):
        # Include the depot city at the beginning and end
        current_permutation = (0,) + cities + (0,)

        # Generate all permutations of the selected cities to determine the shortest possible path
        for perm in itertools.permutations(current_permutation[1:-1]): 
            tour = (0,) + perm + (0,)
            cost = sum(calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour) - 1))
            
            if cost < min_cost:
                min_cost = cost
                min_tour = tour

    return min_tour, min_cost

tour, total_cost = find_min_k_tsp_tour(city_coords, k)
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")