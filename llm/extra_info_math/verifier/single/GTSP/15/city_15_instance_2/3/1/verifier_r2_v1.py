import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, travel_cost):
    # City groups as lists of city indexes
    city_groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]

    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }

    # [Requirement 1]: One city from each group must be visited.
    visited_groups = [False] * len(city_groups)
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    print(f"Group {i} is visited more than once.")
                    return "FAIL"
                visited_groups[i] = True
    if not all(visited_groups):
        print("Not all groups have been visited exactly once.")
        return "FAIL"

    # [Requirement 2]: Correct travel cost calculation.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])

    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-9):
        print(f"Calculated cost {calculated_cost} does not match provided cost {travel_mag}avel_cost.")
        return "FAIL"

    # [Requirement 3]: Starts and ends at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        print("Tour does not start and end at depot city.")
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 1, 0]
travel_cost = 66.27

result = check_requirements(tour, travel_cost)
print(result)