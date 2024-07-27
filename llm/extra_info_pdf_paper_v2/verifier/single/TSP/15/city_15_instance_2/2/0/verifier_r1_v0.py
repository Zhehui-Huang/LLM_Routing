import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities including the depot
        self.coordinates = [
            (54, 87),  # Depot city 0
            (21, 84),  # City 1
            (69, 84),  # City 2
            (53, 40),  # City 3
            (54, 42),  # City 4
            (36, 30),  # City 5
            (52, 82),  # City 6
            (93, 44),  # City 7
            (21, 78),  # City 8
            (68, 14),  # City 9
            (51, 28),  # City 10
            (44, 79),  # City 11
            (56, 58),  # City 12
            (72, 43),  # City 13
            (6, 99),   # City 14
        ]
        self.tour = [0, 6, 11, 14, 1, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
        self.reported_cost = 311.877641807867
    
    def test_tour_starts_and_ends_at_depot(self):
        """Check if the tour starts and ends at the depot city 0."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_all_cities_visited_exactly_once(self):
        """Check if all cities except the depot are visited exactly once."""
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), len(self.coordinates))  # includes the depot, counting only once
        self.assertEqual(sorted(unique_cities), list(range(15)))  # all cities from 0 to 14 are visited
    
    def test_calculated_travel_cost(self):
        """Check if the calculated travel cost is close to the reported total travel cost."""
        cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.coordinates[self.tour[i]]
            x2, y2 = self.coordinates[self.tour[i+1]]
            cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.assertAlmostEqual(cost, self.reported_cost, places=5)
    
    def runTest(self):
        self.test_tour_starts_and_ends_at_depot()
        self.test_all_cities_visited_exactly_once()
        self.test_calculated_travel_cost()

# Run the suite
test_suite = unittest.TestSuite()
test_suite.addTest(TestTSPSolution())

runner = unittest.TextTestRunner()
result = runner.run(test_suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")