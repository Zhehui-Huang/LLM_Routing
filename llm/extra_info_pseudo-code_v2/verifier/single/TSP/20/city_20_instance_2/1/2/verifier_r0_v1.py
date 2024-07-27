import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, reported_cost, city_coordinates):
    # Requirement 2: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 1: Visit all cities exactly once (except the depot, returned to)
    if sorted(tour) != list(range(len(city_coordinates))):
        return "FAIL"

    # Requirement 3: Travel cost as Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Comparing the calculated total cost with the reported total travel cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 4: Use of Lin-Kernighan algorithm - Assuming this requirement is handled during the solution phase.

    # Requirement 5 and 6: Output checks
    if not isinstance(tour, list) or not isinstance(reported_cost, float):
        return "FAIL"

    return "CORright"

# City coordinates mapping from the problem description
city_coordinates = [
    (3, 26),  # City 0
    (85, 72),  # City 1
    (67, 0),  # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),  # City 6
    (38, 68),  # City 7
    (3, 92),  # City 8
    (59, 8),  # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48),  # City 19
]

# Solution details
tour_solution = [0, 6, 8, 10, 3, 4, 17, 1, 5, 15, 13, 18, 7, 11, 14, 16, 19, 2, 9, 12, 0]
reported_total_cost = 448.6884596554647

# Check the solution
result = test_solution(tour_solution, reported_total_cost, city_modules)
print(result)