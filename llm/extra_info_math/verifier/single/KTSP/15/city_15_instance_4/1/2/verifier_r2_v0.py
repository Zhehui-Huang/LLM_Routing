import unittest
from math import sqrt

# Function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Class to perform unit tests
class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40),  # Depot city 0
            (39, 41),
            (81, 30),
            (5, 50),
            (72, 90),
            (54, 46),
            (8, 70),
            (97, 62),
            (14, 41),
            (70, 44),
            (27, 47),
            (41, 74),
            (53, 80),
            (21, 21),
            (12, 39)
        ]
        self.tour = [0, 1, 2, 4, 5, 6, 8, 10, 11, 12, 13, 14, 0]
        self.total_cost = 405.6627467584108  # Provided solution total cost

    def test_tour_start_end_at_depot(self):
        """Test that the robot tour starts and ends at city 0."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visits_exactly_12_cities(self):
        """Test that the robot tour visits exactly 12 cities, including the depot."""
        self.assertEqual(len(set(self.tour)), 12)

    def test_tour_total_travel_cost(self):
        """Test that the calculated total cost of the tour matches the given value."""
        calculated_total_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) 
                                    for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_total_cost, self.total_cost, places=5)

# Function to run the unit tests
def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTourSolution('test_tour_start_end_at_depot'))
    test_suite.addTest(TestTourSolution('test_tour_visits_exactly_12_cities'))
    test_suite.addTest(TestTourSolution('test_tour_total_travel_cost'))
    
    runner = unittest.TextTestRunner()
    test_result = runner.run(test_suite)
    
    if test_result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Print out the result of tests
print(run_tests())