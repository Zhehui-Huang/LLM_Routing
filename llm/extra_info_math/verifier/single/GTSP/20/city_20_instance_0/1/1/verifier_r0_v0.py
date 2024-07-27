import math

# Given city coordinates and groupings
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46),
    11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]


def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, total_cost):
    """ Check the requirements based on the tour and calculated cost """
    # [Requirement 1] The tour must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit exactly one city from each of the three city groups.
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start/end
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(i)
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # [Requirement 3] The path must be a complete tour where the robot travels between cities.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Sample output from solver
tour = [0, 1, 2, 3, 0]
total_cost = 100

# Checking the requirements
check_result = check_requirements(tour, total_cost)
print(check_result)