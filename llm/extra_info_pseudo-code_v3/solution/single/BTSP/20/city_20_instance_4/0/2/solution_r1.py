import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Cities coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89),
}

# Total number of cities
num_cities = len(cities)

# Function to check all permutations for Hamiltonian circuit with minimum max edge length
def find_minimax_tour():
    min_max_distance = float('inf')
    best_tour = None

    # Generate all possible tours starting and ending at the depot
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_edge_distance = 0
        valid_tour = True

        # Calculate the maximum distance between consecutive cities in this tour
        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1])
            if dist > max_edge_distance:
                max_edge_distance = dist

        # Update the best tour if the current one has a smaller maximum edge distance
        if max_edge_distance < min_max_distance:
            min_max_distance = max_edge_distance
            best_tour = tour

    # Calculate the total distance of the best tour
    total_distance = 0
    if best_tour:
        for i in range(len(best_tour) - 1):
            total_distance += euclidean_distance(cities[best_tour[i]][0], cities[best_tour[i]][1], cities[best_tour[i+1]][0], cities[best_tour[i+1]][1])

    return best_tour, total_distance, min_max_distance

# Find the best tour
tour, total_travel_cost, max_consecutive_distance = find_minimax_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")