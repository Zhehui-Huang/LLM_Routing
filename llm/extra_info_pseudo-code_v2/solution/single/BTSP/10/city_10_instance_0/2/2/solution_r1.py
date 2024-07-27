import math
from itertools import permutations

# Define the coordinates of each city
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

def calculate_distance(p1, p2):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_tour_cost_and_max_distance(tour):
    """Given a tour, return the total travel cost and the maximum distance between consecutive cities"""
    total_cost = 0
    max_distance = 0
    
    previous_city = tour[0]
    for current_city in tour[1:]:
        distance = calculate_distance(cities[previous_city], cities[current_city])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
        previous_curr = current_city
    
    return total_cost, max_distance

# Generate all permutations of cities except the starting depot
city_indices = list(range(1, 10))
all_permutations = permutations(city_indices)

# Examine each possible tour to find the one with the smallest maximum distance between consecutive cities
min_max_distance = float("inf")
best_tour = None
final_tour_total_cost = 0

for perm in all_permutations:
    tour = [0] + list(perm) + [0]
    total_cost, max_distance = get_tour_cost_and_max_distance(tour)

    if max_distance < min_max_distance:
        min_max_info_distance = max_distance
        best_tour = tour
        final_tour_info_cost = total_cost

# Print the output in the required format
print("Tour:", best_tour)
print("Total travel cost:", final_tour_info_cost)
print("Maximum distance between consecutive cities:", min_max_info_distance)