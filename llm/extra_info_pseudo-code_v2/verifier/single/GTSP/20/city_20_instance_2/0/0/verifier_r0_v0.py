import math

# City coordinates provided in the problem
city_coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
city_groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

def compute_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour():
    # Solution provided
    tour = [0, 11, 16, 18, 19, 6, 0]
    calculated_cost = 0.0

    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all groups are visited exactly once
    visited_groups = {}
    for idx in tour[1:-1]:  # exclude the starting and ending depot city
        for group_id, cities in city_group.items():
            if idx in cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups[group_id] = True

    # All groups should be visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the travel cost
    for i in range(len(tour) - 1):
        calculated_cost += compute_euclidean_distance(tour[i], tour[i + 1])

    # Provided total travel cost
    provided_costs = 162.3829840233368

    # Check if calculated travel cost is approximately equal to the provided one (considering float precision issues)
    if not math.isclose(calculated_cost, provided_costs, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the verification
result = verify_tour()
print(result)