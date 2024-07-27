import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tsp_solution(tour, total_cost):
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
    groups = [
        {2, 7, 10, 11, 14},
        {1, 3, 5, 8, 13},
        {4, 6, 9, 12}
    ]

    # 1. Check if the tour starts and ends at the depot (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # 2. Check if exactly one city from each group is visited
    visited_groups = [0] * 3
    for city in tour[1:-1]: # Exclude the first and last element (depot)
        city_found = False
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                city_found = True
                break
        if not city_found or sum(visited_groups) > 3:
            return "FAIL"
    if not all(visited == 1 for visited in visited_groups):
        return "FAIL"

    # 3. Check the cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])

    # Allow small discrepancies in floating point calculation
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided solution to verify
tour = [0, 8, 10, 9, 0]
total_cost = 114.09
result = verify_tsp_solution(tour, total_balance)
print(result)