import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56),
            1: (53, 42),
            2: (1, 95),
            3: (25, 61),
            4: (69, 57),
            5: (6, 58),
            6: (12, 84),
            7: (72, 77),
            8: (98, 95),
            9: (11, 0),
            10: (61, 25),
            11: (52, 0),
            12: (60, 95),
            13: (10, 94),
            14: (96, 73),
            15: (14, 47),
            16: (18, 16),
            17: (4, 43),
            18: (53, 76),
            19: (19, 72)
        }
        self.tour_proposed = [0, 3, 19, 6, 13, 2, 0]
        self.total_cost_proposed = 101.35
        self.max_distance_proposed = 48.6

    def test_tour(self):
        # Check if tour starts and ends at the depot, and all cities are visited exactly once
        self.assertEqual(self.tour_proposed[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.tour_proposed[-1], 0, "Tour should end at depot city 0")
        self.assertEqual(len(set(self.tour_proposed)), len(self.cities), "Each city should be visited exactly once")
    
    def test_total_travel_cost_and_max_distance(self):
        total_cost_calculated = 0.0
        max_distance_calculated = 0.0
        for i in range(len(self.tour_proposed) - 1):
            city1 = self.tour_proposed[i]
            city2 = self.tour_proposed[i + 1]
            distance = math.sqrt((self.cities[city2][0] - self.cities[city1][0])**2 + (self.cities[city2][1] - self.cities[city1][1])**2)
            total_cost_calculated += distance
            if distance > max_distance_calculated:
                max_distance_calculated = distance
        
        self.assertAlmostEqual(total_cost_calculated, self.total_cost_proposed, places=2, msg="Total travel cost should match the proposed solution")
        self.assertAlmostEqual(max_distance_calculated, self.max_distance_proposed, places=2, msg="Maximum distance between consecutive cities should match the proposed solution")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTourSolution('test_tour'))
    suite.addTest(TestTourSolution('test_total_travel_cost_and_max_distance'))
    
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")