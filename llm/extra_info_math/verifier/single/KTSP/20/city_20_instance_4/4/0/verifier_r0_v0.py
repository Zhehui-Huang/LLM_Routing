import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 8, 9, 5, 7, 12, 6, 10, 15, 4, 3, 14, 2, 11, 13, 1, 0]
        self.total_cost = 381.76206338723176
        self.coordinates = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
            4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
            8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
            12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
            16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
        }

    def calculate_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city")

    def test_tour_visits_exactly_16_cities(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 16, "Tour does not visit exactly 16 different cities")

    def test_total_travel_cost_is_minimal(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += self.calculate_distance(self.tour[i], self.tour[i+1])
        self.assertAlmostEqual(self.total_cost, calculated_cost, places=5, msg="Calculated travel cost is not as expected")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_tour_starts_and_ends_at_depot'))
    suite.addTest(TestTSPSuite('test_tour_visits_exactly_16_cities'))
    suite.addTest(TestTSPSuite('test_total_travel_cost_is_minimal'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")