import itertools
import math

# Given cities with coordinates including depot (city 0)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92),
    (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Function to calculate euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate the distance matrix for all pairs of cities
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Generator function to find the shortest tour that visits exactly 10 cities
def find_shortest_tour():
    min_tour_length = float('inf')
    best_tour = None

    # A combination of 9 other cities (excluding the depot) because the depot is always included.
    for cities_subset in itertools.combinations(range(1, len(coordinates)), 9):
        city_ids = [0] + list(cities_subset)  # Starting and including the depot

        # Check all permutations of this subset to find the shortest cycle that returns to the depot
        for city_order in itertools.permutations(city_ids[1:]):
            tour = [0] + list(city_detail) + [0]
            tour_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            
            if tour_length < min_tour_length:
                min_tour_length = tour_length
                best_tour = tour

    return best_tour, min_tour_length

# Calculating the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Output the most effective tour and the total travel cost.
print("Tour:", tour)
print("Total travel response cost:", total_cost)