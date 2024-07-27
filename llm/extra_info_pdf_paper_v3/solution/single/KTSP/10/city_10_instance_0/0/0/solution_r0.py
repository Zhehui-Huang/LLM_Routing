import itertools
import math

# Coordinates of cities including depot
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

# Find best tour
def find_best_k_tsp_tour():
    best_distance = float('inf')
    best_tour = []
    
    # Generate all combinations of 3 cities from 9 possible city choices
    city_indices = list(range(1, 10))
    all_combinations = itertools.combinations(city_indices, 3)
    
    # Test all combinations
    for subset in all_combinations:
        # Create full subset including the depot
        current_subset = [0] + list(subset) + [0]
        
        # Test all permutations within the current subset
        for permuted_subset in itertools.permutations(current_subset[1:-1]):
            # Creating a potential tour from the permutations
            tour = [0] + list(permuted_subset) + [0]
            current_distance = calculate_total_distance(tour)
            
            # Check if the current tour is better (shorter) than what we've found before
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = tour
    
    return best_tour, best_distance

# Compute the optimal tour and its distance
best_tour, best_distance = find_best_k_tsp_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))