import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution():
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Given solution
    tour = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0, 0]
    reported_cost = 398.667866225166

    # Requirement 1: Check if the robot starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if all cities are visited exactly once, except city 0
    city_visits = {i: 0 for i in range(20)}
    for city in tour:
        city_visits[city] += 1

    if not all(count == 1 for i, count in city_visits.items() if i != 0) or city_visits[0] != 2:
        return "FAIL"

    # Requirement 3: Verify the tour cost
    calculated_cost = sum(calculate_euclidean_distance(cities[tour[i-1]][0], cities[tour[i-1]][1],
                                                       cities[tour[i]][0], cities[tour[i]][1]) for i in range(1, len(tour)))
    if not math.isclose(calculated_cost, reported_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_solution()
print(result)