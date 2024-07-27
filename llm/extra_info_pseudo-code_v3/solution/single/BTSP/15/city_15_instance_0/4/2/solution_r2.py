import math
from itertools import permutations

# Defining city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute-force search for the best tour minimizing the maximum edge length
def find_best_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_total_distance = 0

    # Generate all permutations of cities excluding the depot (city 0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]  # Construct tour starting/ending at depot
        max_distance = 0
        total_distance = 0

        # Calculate distances for the tour
        for i in range(len(tour)-1):
            distance = calc_distance(tour[i], tour[i+1])
            total_distance += distance
            if distance > max_distance:
                max_distance = distance

        # Keep the best tour with the smallest max distance
        if max_distance < min_max_distance or (max_distance == min_max_release and total_distance < best_total_distance):
            min_max_distance = max_distance
            best_tour = tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_distance

# Find and output the optimal tour
optimal_tour, total_cost, max_edge_length = find_best_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_t:.2f}")