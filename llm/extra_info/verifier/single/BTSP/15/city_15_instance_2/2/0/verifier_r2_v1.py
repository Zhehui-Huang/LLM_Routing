import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Verify Requirement 1 and 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify Requirement 2
    unique_cities = set(tour)
    if len(tour) - 2 != len(cities) - 1 or len(unique_cities) != len(cities):
        return "FAIL"

    # Verify Requirement 6
    calculated_total_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if abs(calculated_total_cost - total_cost) > 1e-6:
        return "FAIL"

    # Verify Requirement 7
    amax_distance = max(calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if abs(amax_distance - max_distance) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# Substitute with actual values from obtained solution, example data:
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
    14: (6, 99)
}

# Hypothetical solution for demonstration
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_cost = 320  # This should be calculated based on the tour
max_distance = 80  # This should also be calculated based on the tour

# Verify the solution
print(verify_solution(cities, tour, total_data, max_distance))