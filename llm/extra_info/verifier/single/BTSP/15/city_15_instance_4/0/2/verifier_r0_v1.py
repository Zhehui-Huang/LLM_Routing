import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.expected_total_cost = 337.84
        self.expected_max_distance = 60.67

    def test_tour_validity(self):
        # Verify tour starts and ends at the city 0, and all cities are visited exactly once
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot city 0.")
        all_cities = list(range(15))
        self.assertCountEqual(all_cities, sorted(self.tour[:-1]), "Tour should visit all cities exactly once, apart from depot.")

    def test_travel_cost_and_distances(self):
        # Calculate the travel costs and verify with expected values
        total_cost = 0
        max_distance = 0
        for i in range(1, len(self.tour)):
            dist = euclidean_list(self.tour[i-1], self.tour[i], self.cities)
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=2, "Total travel cost should match expected value.")
        self.assertAlmostEqual(max_distance, self.expected_max_distance, places=2, "Maximum distance between consecutive cities should match expected value.")

def euclidean_list(city1_index, city2_index, cities):
    city1 = cities[city1_index]
    city2 = cities[city2_index]
    return euclidean_distance(city1, city2)

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

main()