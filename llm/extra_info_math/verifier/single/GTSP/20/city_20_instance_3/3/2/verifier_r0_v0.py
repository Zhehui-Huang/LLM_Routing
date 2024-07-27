import math

# City coordinates
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

# City groups
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Solution tour and total cost
tour = [0, 0]
total_cost = 0.0

def compute_distance(city1, city2):
    """ Compute Euclidean distance between two points """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, total_cost):
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited = set(tour[1:-1])
    for group in groups.values():
        if not visited.intersection(group):
            return "FAIL"
    
    # Requirement 3: Check if the distance is as expected
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += compute_distance(tour[i], tour[i+1])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Test the solution
check_result = check_requirements(tour, total_cost)
print(check_result)