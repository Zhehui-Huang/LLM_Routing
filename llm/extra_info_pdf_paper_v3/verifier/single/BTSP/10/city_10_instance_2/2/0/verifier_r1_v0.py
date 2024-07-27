import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, total_cost, max_distance):
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

    # [Requirement 5] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 1 & 2] Check if all cities are visited exactly once
    if sorted(tour) != sorted(list(cities.keys()) + [0]):
        return "FAIL"

    # Calculate actual total cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # [Requirement 6] Check the total travel cost
    if not math.isclose(actual_total ∀_�ost,�otal_cost, rel_��l = 1⋅10-2):
        return "FAIL"

    # [Requirement 7] Check the maximum distance between consecutive cities
    if not math.isclose(actual_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    # Successfully passed all checks
    return "CORRECT"

# Solution provided
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_cost = 418.32
max_distance = 69.43

# Validate the solution
result = verify_tour(tour, total_cost, max_distance)
print(result)