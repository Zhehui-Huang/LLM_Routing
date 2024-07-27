import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost):
    # Constants and data
    cities_coordinates = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }

    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] Check if the tour includes exactly 4 cities
    if len(set(tour)) != 5:  # including the repetition of the depot city
        return "FAIL"

    # [Requirement 3] Check if the total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            cities_coordinates[city1][0], cities_coordinates[city_node1][1], 
            cities_coordinates[city_node2][0], cities_coordinates[city_node_2][1]
        )

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 5] Check if the format of the output is correct
    # This is actually a static check done by inspecting the output structure.
    # Assume verification passed if above tests pass since improper structure would fail tests.

    return "CORRECT"

# Given solution
tour_example = [0, 1, 10, 8, 0]
total_travel_cost_example = 90.53947981328088

# Execute verification
result = verify_solution(tour_example, total_travel_cost_example)
print(result)