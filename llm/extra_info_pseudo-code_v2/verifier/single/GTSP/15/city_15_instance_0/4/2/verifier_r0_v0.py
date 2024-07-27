import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, claimed_cost):
    # Cities and their coordinates
    cities = {
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
    # City groups
    city_groups = {
        0: [2, 7, 10, 11, 14],
        1: [1, 3, 5, 8, 13],
        2: [4, 6, 9, 12]
    }

    # Requirement 1: Tour must start and end at the depot city, index 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Calculate travel cost and compare
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(total_cost, claimed_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 3: Check exact one city from each group
    visited_groups = {0: False, 1: False, 2: False}
    for city in tour[1:-1]:  # omit the depot city at the start and the end
        for group in city_groups:
            if city in city_groups[group]:
                if visited_groups[group]:
                    return "FAIL"
                visited_groups[group] = True
    if not all(visited_groups.values()):
        return "FAIL"

    # Requirement 4: Already implicitly checked by parsing the input and calculation

    return "CORRECT"

# Provided solution
tour = [0, 8, 10, 9, 0]
total_travel_cost = 114.09

# Run verification
test_result = verify_solution(tour, total_travel_cost)
print(test_result)