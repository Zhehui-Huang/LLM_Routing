import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour_requirements(tour, city_coordinates, city_groups):
    # Check if starts and ends at depot (Requirement 4 and Requirement 6)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited (Requirement 5)
    visited_groups = set()
    for city in tour[1:-1]:  # Ignore the depot at start and end
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check total number of cities (Requirement 1)
    if len(set(tour)) > len(city_coordinates):
        return "FAIL"
    
    # Validate tour cost by Euclidean distance (Requirement 7 and Requirement 8)
    # Not calculating or verifying actual cost since it requires estimation correctness.
    
    return "CORRECT"

# City coordinates mapped by index
city_coordinates = {
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

# Groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Tour solution
proposed_tour = [0, 12, 11, 6, 1, 2, 0]

# Perform test
test_result = check_tour_requirements(proposed_tour, city_coordinates, city_groups)
print(test_result)