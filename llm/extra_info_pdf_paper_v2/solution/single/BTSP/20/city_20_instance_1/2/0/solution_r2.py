import math
from itertools import permutations

# Define coordinates for each city
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to compute the Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    return math.hypot(cities[idx1][0] - cities[idx2][0], cities[idx1][1] - cities[idx2][1])

# Function to generate all possible tours from a given city
def generate_tours(start_city):
    cities_indices = list(range(len(cities)))
    cities_indices.remove(start_city)
    return [[start_city] + list(perm) + [start_city] for perm in permutations(cities_indices)]

# Find the minimum bottleneck value of all tours
def find_min_bottleneck_tour():
    all_possible_tours = generate_tours(0)
    min_bottleneck_value = float('inf')
    min_bottleneck_tour = None
    
    for tour in all_possible_tours:
        max_distance_in_tour = max(
            euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)
        )
        if max_distance_in_tour < min_bottleneck_value:
            min_bottleneck_value = max_distance_in_tour
            min_bottleneck_tour = tour
    
    total_distance = sum(
        euclidean_distance(min_bottleneck_tour[i], min_bottleneck_tour[i+1]) for i in range(len(min_bottleneck_tour) - 1)
    )
    
    return min_bottleneck_tour, total_distance, min_bottleneck_value

# Get the optimal tour with the minimum bottleneck
optimal_tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")