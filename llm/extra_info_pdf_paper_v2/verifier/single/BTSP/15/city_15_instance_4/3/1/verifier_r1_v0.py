import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
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
        # Provided tour and stats
        self.tour = [0, 1, 5, 9, 2, 7, 10, 8, 14, 13, 3, 6, 11, 12, 4, 0]
        self.total_cost = 382.17543977534353
        self.max_distance = 71.58910531638176

    def test_tour_start_end_at_depot(self):
        """Test that the robot starts and ends at the depot."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_all_cities_visited_once(self):
        """Test that each city is visited exactly once, apart from the depot."""
        tour_without_depot = self.treat_tour = [self.tour[i] for i in range(1, len(self.tour) - 1)]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14)
        self.assertTrue(all(city in unique_cities for city in range(1, 15)))

    def test_total_travel_cost(self):
        """Test the sum of the distances matches provided total cost."""
        computed_cost = sum(
            sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i + 1]][0])**2 +
                 (self.cities[self.tour[i]][1] - self.cities[self.tour[i + 1]][1])**2)
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(computed_cost, self.total_cost, places=5)

    def test_max_distance_check(self):
        """Test that the maximum distance between consecutive cities is calculated correctly."""
        computed_max_distance = max(
            sqrt((self.cities[self.tour[i]][0] - self.cities[self.tour[i + 1]][0])**2 +
                 (self.cities[self.tour[i]][1] - self.cities[self.tour[i + 1]][1])**2)
            for i in range(len(self.tour) - 1)
        )
        self.assertAlmostEqual(computed_max_distance, self.max_distance, places=5)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTourSolution('test_tour_start_end_at_depot'))
    suite.addTest(TestTourName('test_all_cities_visited_once'))
    suite.addTest(TestTourName('test_total_travel_cost'))
    suite.addTest(TestTourName('test_max_distance_check'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.failures or result.errors:
        print("FAIL")
    else:
        print("CORRECT")