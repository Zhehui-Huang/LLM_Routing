import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of the cities as per the environment information
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def compute_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

# Primary function to find the shortest tour visiting exactly 4 cities
def find_shortest_tour():
    depot_city_index = 0
    other_cities = list(range(1, len(coordinates)))
    best_tour = None
    best_cost = float('inf')
    
    # Iterate over all combinations of 3 other cities (excluding depot)
    for cities_combination in itertools.combinations(other_cities, 3):
        current_combination = [depot_city_index] + list(cities_combination)
        
        # Check all permutations of the selected cities
        for permutation in itertools.permutations(current_combination):
            tour = list(permutation) + [depot_city_index]
            cost = compute_total_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
    
    return best_tour, best_cost

# Get the best tour and its cost
best_tour, best_cost = find_shortest_tour()

# Output the required results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))