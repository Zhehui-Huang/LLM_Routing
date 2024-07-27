import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    # City coordinates
    cities = {
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

    # Provided solution
    tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
    reported_total_cost = 384.7863591860825

    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except the depot city
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"

    # Calculate the travel cost from the tour
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the total travel cost matches the reported cost
    if not math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the test
test_result = test_solution()
print(test_result)