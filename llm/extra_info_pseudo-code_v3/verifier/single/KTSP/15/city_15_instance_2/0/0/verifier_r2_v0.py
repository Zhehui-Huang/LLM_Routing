import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, reported_cost):
    # Coordinates for each city
    coordinates = {
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

    # Check number of cities visited (including depot city)
    if len(set(tour)) != 9:  # Including depot city twice
        return "FAIL"

    # Check the tour begins and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculating the actual cost of the tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    # Comparing the computed cost with the reported cost
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given tour and total cost
tour = [0, 8, 3, 10, 6, 4, 12, 5, 0]
reported_cost = 159.87

# Perform the unit test
print(test_solution(tour, reported_cost))