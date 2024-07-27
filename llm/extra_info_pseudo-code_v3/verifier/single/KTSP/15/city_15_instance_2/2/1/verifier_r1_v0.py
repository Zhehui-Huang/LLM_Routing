import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Test function to validate the provided tour and total travel cost
def test_solution(tour, total_travel_cost):
    # City coordinates
    city_coordinates = {
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

    # Verify that the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify that exactly 8 cities are visited
    if len(tour) != 8:
        return "FAIL"

    # Calculate total travel cost
    calculated_cost = sum(compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

    # Verify total travel cost
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Provided solution details
tour = [0, 6, 14, 12, 3, 13, 2, 0]
total_travel_cost = 212.97695656493354

# Perform the test
test_result = test_solution(tour, total_travel_cost)
print(test_result)