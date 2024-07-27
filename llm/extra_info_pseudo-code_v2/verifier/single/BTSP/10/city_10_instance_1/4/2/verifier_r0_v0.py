import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TSPTest(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        self.tour = [0, 5, 3, 8, 4, 0, 2, 9, 7, 1, 6, 0]
        self.total_cost = 311.36
        self.max_distance = 56.61

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city 0")
    
    def test_all_cities_visited_once(self):
        unique_cities = set(self.tour[1:-1])  # Excludes the repeated depot city at the start/end
        self.assertEqual(len(unique_cities), 9, "Some cities are not visited or are visited more than once")

    def test_output_list_format(self):
        self.assertIsInstance(self.tour, list, "Tour is not a list")
        self.assertIsInstance(self.total_cost, float, "Total travel cost is not a float")
        self.assertIsInstance(self.max_distance, float, "Max distance is not a float")
    
    def test_output_tour_total_max_cost(self):
        calculated_cost = 0
        calculated_max_distance = 0
        for i in range(len(self.tour) - 1):
            dist = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            calculated_cost += dist
            if dist > calculated_max_distance:
                calculated_max_distance = dist
        
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2, msg="Reported total travel cost is incorrect")
        self.assertAlmostEqual(calculated_max_distance, self.max_distance, places=2, msg="Reported max distance is incorrect")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TSPTest))
    result = unittest.TextTestRunner().run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")