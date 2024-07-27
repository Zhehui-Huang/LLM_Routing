import math

# Definition of city coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Definition of groups
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Provided tour and its total travel cost
tour = [0, 4, 7, 12, 15, 3, 18, 0]
provided_total_cost = 227.40171050114

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour():
    # Check Requirement 2:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 1:
    visited_groups = set()
    for city in tour[1:-1]:
        for group_id, group_cities in groups.items():
            if city in group_cities:
                visited_groups.add(group_id)
    if len(visited_groups) != 6:
        return "FAIL"
    
    # Check Requirement 3 and 4:
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if abs(calculated_cost - provided_total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Output the result based on the verification
print(verify_tour())