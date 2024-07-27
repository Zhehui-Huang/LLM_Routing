import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.total_cost = 132.12

        # Cities coordinates
        self.cities = {
            0: (54, 87),
            2: (69, 84),
            13: (72, 43),
            3: (53, 40),
            4: (54, 42),
            12: (56, 58),
            11: (44, 79),
            6: (52, 82)
        }

    def test_tour_starts_and_ends_at_depot(self):
        # Check if the first and last city in the tour is the depot city 0
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")

    def test_exactly_eight_cities_visited(self):
        # Check if there are exactly 8 unique cities visited
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 8, "Tour should visit exactly 8 unique cities")

    def test_total_travel_distance(self):
        # Compute the actual travel cost from given tour
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        actual_cost = 0
        for i in range(len(self.tour) - 1):
            actual_cost += calculate_distance(self.tour[i], self.tour[i + 1])

        # Check if the computed total travel cost is approximately equal to the provided total cost
        self.assertAlmostEqual(actual_cost, self.total_cost, places=2,
                               msg="The computed total travel distance should be approximately equal to the provided total cost")

suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
result = unittest.TextTestRunner().run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")