import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def unit_tests():
    # Coordinates of cities including the depot (Index 0 is depot city)
    cities = [
        (53, 68),  # depot city 0
        (75, 11),  # city 1
        (91, 95),  # city 2
        (22, 80),  # city 3
        (18, 63),  # city 4
        (54, 91),  # city 5
        (70, 14),  # city 6
        (97, 44),  # city 7
        (17, 69),  # city 8
        (95, 89)   # city 9
    ]

    # Provided solution
    tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
    reported_cost = 290.8376577906224

    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    visited_cities = set(tour[1:-1])  # Ignore starting and ending depot
    if len(visited_cities) != 9 or set(range(1, 10)) != visited_cities:
        return "FAIL"

    # Requirement 3 & 4
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city_a][0], cities[city_a][1], cities[city_b][0], cities[city_b][1])

    # Requirement 5
    if not math.isclose(reported_cost, calculated_cost, abs_tol=1e-9):
        return "FAIL"

    # Since the LK algorithm implementation from the original prompt is not computable here, skip Requirement 6

    return "CORRECT"

result = unit_tests()
print(result)