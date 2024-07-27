import unittest
import math

# Define city coordinates with city index as key
city_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define city groups
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Expected tour output and its cost
expected_tour = [0, 8, 13, 1, 14, 5, 12, 10, 0]
expected_cost = 225.43

def calculate_euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coef_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, tour_cost):
    """ Validate if the proposed tour and cost meet the constraints """
    if len(city_coordinates) != 15:
        return False
    if tour[0] != 0 or tour[-1] != 0:
        return False
    city_in_group_visited = [False] * len(city_groups)
    for i, group in enumerate(city_groups):
        group_visit = False
        for city in group:
            if city in tour:
                if group_visit:  # More than one visit in the same group
                    return False
                group_visit = True
        if not group_visit:
            return False
        city_in_group_visited[i] = group_visit
    
    # Verify all groups are visited
    if not all(city_in_group_visited):
        return False
    
    # Check if the first and last cities are the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Calculate actual tour cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    # Compare costs with a reasonable floating point tolerance
    if not math.isclose(actual_cost, tour_cost, abs_tol=1e-2):
        return False
    
    return True

class TestTourSolution(unittest.TestCase):
    def test_solution(self):
        result = validate_tour(expected_tour, expected_cost)
        self.assertTrue(result)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTourSolution))
    result = unittest.TextTestRunner().run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")