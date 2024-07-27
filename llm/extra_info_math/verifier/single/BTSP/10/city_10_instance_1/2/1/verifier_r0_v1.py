import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution():
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
    expected_max_distance = 56.61271941887264
    expected_total_cost = 291.41088704894975

    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"

    # Calculate total travel cost and check maximum distance
    calculated_total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = euclidean_distance(cities[city1], cities[city2])
        calculated_total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check distances against expected values
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_total_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the check
result = check_solution()
print(result)