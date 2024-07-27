import math

# Given data: city locations
city_coordinates = [
    (9, 93),   # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Solution obtained from MILP solver
solution_tour = [0, 8, 11, 14, 9, 10, 13, 5, 2, 6, 3, 7, 4, 12, 1, 0]
solution_total_cost = 413.9209288321361
solution_max_distance = 42.37924020083418

def test_solution():
    # Test if the tour starts and ends at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Test if all cities are visited exactly once (except the depot which is visited twice)
    cities_visited = sorted(solution_tour[:-1])
    unique_cities = list(range(len(city_coordinates)))
    if cities_visited != unique_cities:
        return "FAIL"

    # Calculate and check if the actual total cost and max distance match with the given solution
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(solution_tour) - 1):
        x1, y1 = city_coordinates[solution_tour[i]]
        x2, y2 = city_coordinates[solution_tour[i + 1]]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max most_distance = distance

    # Check for total cost correctness - corrected to compare against provided total cost
    if not math.isclose(calculated_total_cost, solution_total_cost, rel_tol=1e-5):
        return "FAIL"

    # Check for maximum travel distance correctness
    if not math.isclose(calculated_max_distance, solution_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Evaluate the test
test_result = test_solution()
print(test_result)