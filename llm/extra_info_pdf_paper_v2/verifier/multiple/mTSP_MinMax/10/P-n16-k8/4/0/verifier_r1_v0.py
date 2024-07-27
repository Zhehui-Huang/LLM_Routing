import math

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Robot tour data
robot_tours = [
    ([0, 1, 9, 0], 72.88),
    ([0, 2, 10, 0], 52.46),
    ([0, 3, 11, 0], 86.04),
    ([0, 4, 12, 0], 64.99),
    ([0, 5, 13, 0], 68.36),
    ([0, 6, 14, 0], 64.17),
    ([0, 7, 15, 0], 83.62),
    ([0, 8, 0], 64.90)
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Test requirements
def test_solution():
    all_cities_visited = set()
    max_cost_calculated = 0

    for tour, reported_cost in robot_tours:
        # Check each tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate travel cost
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

        # Compare reported and calculated cost
        if not math.isclose(cost, reported_cost, abs_tol=0.1):
            return "FAIL"

        # Gather all visited cities
        all_cities_visited.update(tour[1:-1])

        # Track the maximum cost
        if cost > max_cost_calculated:
            max_cost_calculated = cost

    # All cities except the depot should be visited exactly once
    if all_cities_visited != set(range(1, 16)):
        return "FAIL"

    # Ensure the maximum cost matches the expected maximum
    expected_max_cost = max(report[1] for report in robot_tours)
    if not math.isclose(max_cost_calculated, expected_max_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Check if solution meets all requirements
result = test_solution()
print(result)