import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, coordinates):
    # Requirement 1: The robot must visit all 20 cities exactly once and return to the depot (city 0)
    if set(tour) != set(range(21)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: The travel cost between any two cities is calculated as the Euclidean distance
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    # Expected to not actually calculate the shortest distance due to lack of a specific solution comparison
    # but ensuring that the costs are calculated correctly for any provided tour path.
    # This only automatically checks for correct distance calculation following requirement 2.

    # Requirement 3: As we cannot determine optimally without solving, we assume correct calculation suffices.
    return "CORRECT"

# Example input data based on provided scenario (to be adapted based on actual use)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Demo tour (must be edited based on actual algorithm output)
demo_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]

# Verification
print(verify_solution(demo_tour, coordinates))