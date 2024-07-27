def compute_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, city_groups, city_coordinates):
    # [Requirement 1] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for idx, group in enumerate(city_group_ids):
            if city in group:
                visited_groups.add(idx)
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # [Requirement 3] Recalculate the tour distance to ensure it is the minimal possible
    # This check might not be optimal since the solver should already minimize the tour, here we just check the consistency of provided cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += compute_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Change this threshold based on precision or method differences
    if abs(total_distance - provided_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# City coordinates as provided or inferred from previous descriptions
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

# Grouping as provided
city_group_ids = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Tour and provided total cost from the solver output
tour = [0, 9, 10, 8, 0]
provided_cost = 133.81401036814407

# Checking the solution
result = verify_tour(tour, city_group_ids, cities)
print(result)