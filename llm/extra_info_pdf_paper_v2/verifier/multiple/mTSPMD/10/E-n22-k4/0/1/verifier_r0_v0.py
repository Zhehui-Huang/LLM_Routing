import numpy as np
from math import sqrt

# Given Solution
best_tour = [0, 14, 16, 19, 21, 17, 20, 18, 15, 12, 10, 9, 7, 5, 2, 1, 3, 4, 6, 8, 11, 13, 0]
best_tour_cost = 279.11680573201915

# Cities Coordinates (With manual conversion for clarity)
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Requirement 1: Each robot must start and end at its assigned depot city.
def test_start_end_depot(tour):
    return tour[0] == tour[-1] == 0

# Requirement 2: Each city must be visited exactly once.
def test_cities_visited_once(tour):
    return len(set(tour)) == len(tour) and len(tour) == len(cities) + 1

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Requirement 3: Verify the calculated total cost
def test_total_travel_cost(tour):
    computed_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return np.isclose(computed_cost, best_tour_cost, atol=0.001)

# Execute tests
def run_tests():
    if not test_start_end_depot(best_tour):
        return "FAIL: Start/end depot test failed."
    if not test_cities_visited_once(best_tour):
        return "FAIL: Cities visited test failed."
    if not test_total_travel_cost(best_tour):
        return "FAIL: Total cost test failed."
    return "CORRECT"

# Output the test results
print(run_tests())