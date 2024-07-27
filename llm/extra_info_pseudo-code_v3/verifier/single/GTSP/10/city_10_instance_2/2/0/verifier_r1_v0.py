import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour(tour, city_coordinates, city_groups):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each city group is visited
    visited = set(tour)
    for group in city_groups:
        if not any(city in visited for city in group):
            return "FAIL"

    # Calculate and verify the travel cost
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    expected_cost = 281.60273931778477
    if not math.isclose(total_travel_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks are passed
    return "CORRECTION"

# City coordinates as provided
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups as provided
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Solution tour provided
solution_tour = [0, 3, 5, 9, 1, 2, 0]

# Perform the test
test_result = test_tour(solution_tour, city_coordinates, city_groups)
print(test_result)