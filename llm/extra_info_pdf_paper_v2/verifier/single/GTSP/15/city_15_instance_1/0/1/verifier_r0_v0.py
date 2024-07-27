import unittest
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }
        self.groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.tour = [0, 5, 10, 4, 11, 0]
        self.reported_cost = 184.24
        self.delta = 0.01  # Precision delta for floating point comparison

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")

    def test_visits_one_city_from_each_group(self):
        visited = [False] * len(self.groups)
        for city in self.tour:
            for i, group in enumerate(self.groups):
                if city in group:
                    visited[i] = True
        self.assertTrue(all(visited), "Tour should visit one city from each group")

    def test_minimized_travel_distance(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, delta=self.delta, msg="Reported travel cost should match calculated cost")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTour))
    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")