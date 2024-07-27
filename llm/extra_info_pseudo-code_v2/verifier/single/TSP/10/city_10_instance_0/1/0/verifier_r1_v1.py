import unittest
from math import sqrt

# Helper function to calculate Euclidean distance
def euorean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = [
            (50, 42),  # Depot city 0
            (41, 1),
            (18, 46),
            (40, 98),
            (51, 69),
            (47, 39),
            (62, 26),
            (79, 31),
            (61, 90),
            (42, 49)
        ]
        # Expected results
        self.expected_tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
        self.expected_cost = 295.9919678938414
    
    def test_tour(self):
        # Test the tour starts and ends at the depot city
        self.assertEqual(self.expected_tour[0], 0, "The tour should start at the depot city.")
        self.assertEqual(self.expected_tour[-1], 0, "The tour should end at the depot city.")
        
        # Test the tour visits all cities exactly once, except the depot
        tour_cities = sorted(self.expected_tour[1:-1])
        self.assertEqual(tour_cities, list(range(1, 10)), "The tour should visit all other cities exactly once.")
    
    def test_travel_cost(self):
        # Calculate the travel cost from the provided tour
        total_cost = sum(euclidean_distance(self.cities[self.expected_tour[i]], self.cities[self.expected_tour[i + 1]])
                         for i in range(len(self.expected_tour) - 1))
        # Compare the calculated travel cost to the expected cost
        self.assertAlmostEqual(total_cost, self.expected_cost, places=5, msg="The total travel cost should match the expected cost.")
        
# Running the tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasIncessful():
        print("CORRECT")
    else:
        print("FAIL")