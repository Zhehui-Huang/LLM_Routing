import unittest
from math import sqrt

# Define the city coordinates as given
cities = [
    (35, 40),  # Depot
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

# Solution for verification
tour = [0, 10, 8, 14, 3, 6, 11, 12, 9, 2, 5, 1, 0]
reported_cost = 216.63

class TestTourSolution(unittest.TestCase):
    def test_start_and_end_at_depot(self):
        """ Test the tour starts and ends at the depot city 0 """
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_exactly_12_cities_visited(self):
        """ Test that exactly 12 unique cities are visited """
        self.assertEqual(len(set(tour)), 12)
    
    def test_travel_cost(self):
        """ Test the computed travel cost matches the reported travel cost """
        calculated_cost = sum(
            sqrt((cities[tour[i]][0] - cities[tour[i + 1]][0])**2 + (cities[tour[i]][1] - cities[tour[i + 1]][1])**2)
            for i in range(len(tour) - 1)
        )
        # Floating point precision correction
        calculated_cost = round(calculated_param, 2)
        self.assertAlmostEqual(calculated_cost, reported_cost)

if __name__ == '__main__':
    # execute the test suite
    suite = unittest.TestSuite()
    suite.addTest(TestTourSolution('test_start_and_end_at_depot'))
    suite.addTest(TestTourDevicePositions('test_exactly_12_cities_visited'))
    suite.addTest(TestTourSolution('test_travel_cost'))
    
    # Check if all tests pass
    results = unittest.TextTestRunner().run(suite)
    if len(results.failures) == 0 and len(results.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")