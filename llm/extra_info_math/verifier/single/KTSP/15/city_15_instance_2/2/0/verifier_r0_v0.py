import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Cities coordinates
        self.cities = {
            0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
            4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
            8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
            12: (56, 58), 13: (72, 43), 14: (6, 99)
        }
        self.tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.claimed_cost = 132.12

    def test_tour_starts_ends_depot(self):
        """Requirement 1: Tour starts and ends at the depot city."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_visits_exactly_8_cities_including_depot(self):
        """Requirement 2: Tour visits exactly 8 cities, including the depot."""
        self.assertEqual(len(set(self.tour)), 8)

    def test_tour_travel_cost(self):
        """Requirement 3: Travel cost calculation based on the Euclidean distance."""
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        total_distance = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                             for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_distance, self.claimed_cost, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)

    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")