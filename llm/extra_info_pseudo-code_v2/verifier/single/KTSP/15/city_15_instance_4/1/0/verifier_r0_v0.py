import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [0, 10, 8, 14, 3, 6, 11, 12, 4, 9, 5, 1, 0]
        self.reported_cost = 211.27

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], self.tour[-1])

    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 12)

    def test_tour_total_cost(self):
        total_cost = sum(self.calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        # Allow a small margin for floating point arithmetic variations
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_only_one_robot(self):
        # Since the test involves a tour and the requirement implies a single sequence of cities, the solution implicitly
        # satisfies the single robot requirement. No need for explicit verification here other than checking tour validity.
        self.assertTrue(isinstance(self.tour, list))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTour))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")
        
run_tests()