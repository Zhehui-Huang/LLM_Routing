import math
from itertools import permutations

# Define the cities and coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all permutations of the cities (excluding the depot for permutations)
non_depot_cities = list(cities.keys())[1:]
permutations_of_cities = list(permutations(non_depot_cities))

# Find the Hamiltonian cycle that minimizes the maximum leg distance
best_tour = None
best_max_distance = float('inf')

for perm in permutations_of_cities:
    # Including the depot as the start and end point
    tour = [0] + list(perm) + [0]
    
    # Calculate the maximum distance in this tour
    max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Update best tour if current permutation is better
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour

# Calculate the total distance of the best tour
total_distance = sum(euclidean_address(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", best_max_distance)