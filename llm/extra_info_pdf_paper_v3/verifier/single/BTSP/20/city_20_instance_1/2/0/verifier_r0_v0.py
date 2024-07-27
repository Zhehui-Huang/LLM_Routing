import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
            (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
            (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
            (50, 28), (69, 9)
        ]
        self.tour = [1, 8, 13, 2, 9, 6, 0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 19, 12, 1]
        self.total_cost = 414.2331847041342
        self.max_distance = 63.788713735268246

    def test_unique_visit(self):
        # Check if each non-depot city is visited exactly once
        tour_without_depot_and_end = self.tour[1:-1]
        unique_cities = set(tour_without_depot_and_end)
        self.assertEqual(len(unique_cities), 19)  # should be 19 unique cities besides depot

    def test_depot_start_and_end(self):
        # Check if tour starts and ends at the depot
        self.assertEqual(self.tour[0], self.tour[-1])  # starts and ends at the same point (depot)
        self.assertEqual(self.tour[0], 0)  # depot city index is 0

    def test_minimum_max_distance(self):
        # Validate that the given max distance is accurate
        max_dist = 0
        for i in range(len(self.tour)-1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if dist > max_dist:
                max_dist = dist
        self.assertAlmostEqual(max_dist, self.max_distance, places=5)

    def test_total_travel_cost(self):
        # Calculate and test total travel distance
        calculated_cost = 0
        for i in range(len(self.tour)-1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            calculated_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)

# Running the test
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTour))
    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")