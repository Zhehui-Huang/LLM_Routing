import math
import unittest

# Provided tour and cost
provided_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
provided_total_cost = 373.97

# Coordinates for each city including depot city
city_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def compute_euclidean_distance(pt1, pt2):
    """Compute and return the Euclidean distance between two points."""
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def validate_tour(tour, coordinates):
    """Validate the robot tour meets all requirements and calculate total travel cost."""
    # Check all cities are visited exactly once
    if sorted(tour[:-1]) != sorted(list(range(len(coordinates)))):
        return False, None
    
    # Check starting and ending city is the depot (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, None
    
    # Calculate total travel cost
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += compute_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    return True, round(tour_cost, 2)

class TestRobotTour(unittest.TestCase):
    def test_tour_validity_and_cost(self):
        is_valid, calculated_cost = validate_tour(provided_tour, city_coordinates)
        # Validate tour covers all cities exactly once and returns to depot
        self.assertTrue(is_valid)
        # Validate provided cost is same as calculated cost from the provided tour
        self.assertAlmostEqual(calculated_cost, provided_total_cost, places=2)

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")