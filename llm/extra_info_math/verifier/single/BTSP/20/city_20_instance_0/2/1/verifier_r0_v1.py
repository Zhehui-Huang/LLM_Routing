import numpy as np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def test_solution():
    # Coordinates of the cities
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    # Provided solution
    tour = [0, 1, 17, 13, 8, 5, 6, 2, 19, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 4, 0]
    expected_total_cost = 388.510060202877
    expected_max_distance = 32.38826948140329

    # Check Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit each city exactly once
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    # Calculate the total cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_euclidean_distance(*cities[city1], *cities[city2])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check Requirement 6: Output the total travel cost of the tour
    if not np.isclose(total_cost, expected_total_cost, atol=0.01):
        return "FAIL"

    # Check Requirement 7: Output the maximum distance between any two consecutive cities in the tour
    if not np.isclose(max_distance, expected_max_distance, atol=0.01):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Running the test function
print(test_solution())