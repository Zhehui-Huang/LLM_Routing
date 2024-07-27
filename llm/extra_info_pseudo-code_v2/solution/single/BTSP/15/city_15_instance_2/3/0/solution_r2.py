import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the optimal tour
def find_optimal_tour():
    vertices = list(cities.keys())
    min_max_distance = float('inf')
    optimal_tour = None
    total_cost = 0

    # Explore all permutations of cities excluding the depot city 0
    for perm in permutations(vertices[1:]):  # Fix the start/end at depot city 0
        current_tour = [0] + list(perm) + [0]
        current_max_distance = 0
        current_total_cost = 0

        # Calculate total travel cost and maximum distance between consecutive cities for this permutation
        for i in range(len(current_tour) - 1):
            dist = euclidean_distance(cities[current_tour[i]], cities[current_tour[i + 1]])
            current_total_cost += dist
            if dist > current_max_distance:
                current_max_distance = dist

        # Checking if the found tour has a smaller max distance between consecutive cities
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            optimal_tour = current_tour
            total_cost = current_total_cost

    return optimal_tour, total_cost, min_max_distance

# Execute the function to find the tour
tour, total_travel_cost, max_distance = find_optimal_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)