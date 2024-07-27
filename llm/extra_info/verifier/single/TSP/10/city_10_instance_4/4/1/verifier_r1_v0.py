import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (79, 15),  # Depot city 0
            (79, 55),
            (4, 80),
            (65, 26),
            (92, 9),
            (83, 61),
            (22, 21),
            (97, 70),
            (20, 99),
            (66, 62)
        ]
        self.tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
        self.reported_cost = 337.1694332678818

    def test_tour_start_end_at_depot(self):
        # [Requirement 1]
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # [Requirement 2]
        unique_cities = set(self.tour[1:-1])
        self.assertEqual(len(unique_cities), 9)  # Should have visited 9 unique cities excluding the depot

    def test_correct_travel_cost(self):
        # [Requriement 3] and [Requirement 5]
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")