import math

# Given solution
solution_tour = [0, 18, 12, 8, 14, 7, 4, 1, 10, 11, 9, 16, 17, 15, 5, 2, 13, 6, 19, 3]
reported_cost = 418.9261491671591

# City coordinates
city_coordinates = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 74)
}

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_tour(tour, reported_cost):
    # Check if starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, excluding depot city which should be visited twice
    if sorted(tour) != sorted([0] + list(range(1, 20))):
        return "FAIL"

    # Calculate the total travel cost based on the Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_cost += calculate_euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])

    # Validate cost within a reasonable floating point precision range
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Verify the tour and travel cost
verification_result = verify_tour(solution_tour + [0], reported_cost)  # Ensuring the tour ends at the depot city as per implementation
print(verification_result)