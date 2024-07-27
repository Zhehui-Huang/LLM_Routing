import math

# Data setup
depot_and_cities = {
    0: (14, 77),  # depot city
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

group_cities = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Tour provided
tour = [0, 6, 2, 13, 9, 0]
reported_cost = 108.66296159815982


def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    # Check the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the robot visits 5 unique cities, 1 from each set
    visited_groups = set()
    for city in tour:
        for index, group in enumerate(group_cities):
            if city in group:
                visited_groups.add(index)

    if len(visited_groups) != 4 or len(tour) != 6:
        return "FAIL"

    # Checking calculated distances match the reported cost
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = depot_and_cities[tour[i]]
        x2, y2 = depot_and_cities[tour[i + 1]]
        total_distance += calculate_euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(total_distance, reported_cost, abs_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"


# Run the test
result = main()
print(result)