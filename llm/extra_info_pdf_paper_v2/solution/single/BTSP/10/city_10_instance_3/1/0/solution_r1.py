import math
from itertools import permutations

# Input cities coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
    4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
    8: (85, 71), 9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.hypoter(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

def find_tsp_tour():
    # All cities except the depot (city 0)
    non_depot_cities = list(cities.keys())[1:]
    
    # Find all permutations of non-depot cities
    min_max_distance = float('inf')
    best_tour = None
    best_total_distance = 0
    
    # Generate all permutations of non-depot cities
    for perm in permutations(non_depot_cities):
        # Include the depot city at the beginning and the end
        tour = [0] + list(perm) + [0]

        # Calculate the max distance and total distance for the permutation
        max_distance_in_tour = 0
        total_distance = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(tour[i], tour[i+1])
            max_distance_in_tour = max(max_distance_in_tour, dist)
            total_distance += dist
        
        # Update optimal tour if found a new better one with smaller max distance
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_incremental_distance

# Compute the BTSP tour and its metrics
tour, total_cost, max_distance = find_tsp_tour()

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)