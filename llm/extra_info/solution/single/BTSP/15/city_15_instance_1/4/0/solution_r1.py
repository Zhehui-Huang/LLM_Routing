import math
import itertools

# Define the cities with their coordinates
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

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Brute force to find the best tour minimizing the maximum leg distance
def optimal_tour_bruteforce():
    min_max_distance = float('inf')
    best_tour = None
    
    # Generate all permutations
    for perm in itertools.permutations(list(cities.keys())[1:]):
        tour = [0] + list(perm) + [0]
        # Determine the maximum distance between consecutive cities
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Update if a better tour is found
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    
    # Calculate total distance of the optimal tour
    total_distance = sum(euclidean(ciA) for ciA in range(len(best_tour) - 1))
    return best_tour, total_distance, min_max_distance

# Execute the function to get the outputs
optimal_tour, total_travel_cost, max_leg_distance = optimal_tour_bruteforce()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")