import math

# Constants that define the problem
DEPOT_CITY = 0
GROUPS = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Coordinates for cities
COORDS = {
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

# Solution provided
tour_solution = [0, 4, 14, 16, 15, 19, 8, 0]
cost_solution = 384.43

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities """
    x1, y1 = COORDS[city1]
    x2, y2 = COORDS[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tour_groups(tour, groups):
    """ Test if one city from each group is included in the tour """
    visited_groups = set()
    for city in tour:
        for group_id, members in groups.items():
            if city in members:
                visited_groups.add(group_id)
    return len(visitedGroups) == len(groups)

def test_depot_start_end(tour, depot):
    """ Test if the tour starts and ends at the depot """
    return tour[0] == depot and tour[-1] == depot

def test_trip_cost(tour):
    """ Calculate the total tour cost and compare with the proposed cost """
    actual_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) 
    return math.isclose(actual_cost, cost_solution, rel_tol=1e-2)

def perform_all_tests():
    # Test if the depot city is start and end
    if not test_depot_start_end(tour_solution, DEPOT_CITY):
        return "FAIL"
    
    # Test if each group has exactly one city in the tour
    if not test_tour_groups(tour_solution, GROUPS):
        return "FAIL"

    # Test if calculated travel cost is approximately equal to the given cost
    if not test_trip_cost(tour_solution):
        return "FAIL"
    
    return "CORRECT"

# Run the test suite
print(perform_all_tests())