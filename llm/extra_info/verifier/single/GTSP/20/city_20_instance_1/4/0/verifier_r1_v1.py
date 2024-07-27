import unittest
from math import sqrt

# Coordinates of cities (index corresponds to city number)
cities_coordinates = {
    0: (14, 77),
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

# Define city groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Test tour and travel cost provided
test_tour = [0, 6, 13, 2, 9, 0]
test_total_travel_cost = 114.66

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at depot city 0."
    
    if len(tour) != 6:
        return False, "Tour does not have an exact number of cities required, including the depot."
    
    for group in city_groups:
        if not any(city in group for city in tour):
            return False, f"No city from group {group} was visited."
    
    return True, ""

class TestTourSolution(unittest.TestCase):
    def test_requirements(self):
        # Check Requirements
        self.assertEqual(test_tour[0], 0, "Tour should start at city 0.")
        self.assertEqual(test_tour[-1], 0, "Tour should end at city 0.")
        
        # Count visits in each city group
        is_valid, message = validate_tour(test_tour, city_groups)
        self.assertTrue(is_valid, message)

        # Calculate and validate the total cost
        calculated_cost = sum(calculate_euclidean_distance(test_tour[i], test_tour[i+1]) for i in range(len(test_tour) - 1))
        self.assertAlmostEqual(calculated_cost, test_total_travel_cost, delta=0.1, "Total travel cost does not match.")

if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")