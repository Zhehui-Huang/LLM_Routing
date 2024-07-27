from itertools import combinations, permutations
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities data
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Find all combinations of 3 cities, excluding the depot, to form groups of exactly 4 cities including the depot
city_indices = list(cities.keys())[1:]  # Excluding the depot city
combinations_of_cities = combinations(city_indices, 3)

# Function to compute total travel cost of a tour
def compute_tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Minimum distance initialization
min_distance = float('inf')
min_tour = None

# Evaluate each combination and its permutations
for city_group in combinations_of_cities:
    current_combination = list(city_group)  # City group
    # Permute the city group (excluding depot)
    permutations_of_group = permutations(current_combination)
    
    for city_permutation in permutations_of_group:
        # Always starting and ending at the depot
        tour_with_return = (0,) + city_permutation + (0,)
        tour_cost = compute_tour_cost(tour_with_return)
        if tour_cost < min_distance:
            min_distance = tour_cost
            min_tour = tour_with_return

# Print best tour and its cost
output_tour = list(min_tour) if min_tour else []
print("Tour:", output_tour)
print("Total travel cost:", min_distance if min_distance != float('inf') else "No valid tour found")