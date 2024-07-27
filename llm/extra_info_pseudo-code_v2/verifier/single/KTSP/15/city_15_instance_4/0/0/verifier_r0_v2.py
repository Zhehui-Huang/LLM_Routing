import unittest
from math import sqrt

# Coordinates of the cities
cities = {
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

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 5, 9, 2, 4, 12, 6, 3, 14, 8, 10, 1, 0]
        self.total_cost = 250.0416611502525
    
    def test_tour_validity(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at city 0")
        self.assertEqual(len(set(self.tour)), 12, "Tour does not visit exactly 12 distinct cities")
    
    def test_cost_accuracy(self):
        calculated_cost = calculate_total_travel_cost(self.tour, cities)
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5,
                               msg="Calculated cost does not match given total cost.")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTour))
    result = unittest.TextTestRunner().run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")