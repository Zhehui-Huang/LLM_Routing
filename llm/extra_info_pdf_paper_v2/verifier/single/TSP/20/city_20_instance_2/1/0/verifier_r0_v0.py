import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (3, 26),
            1: (85, 72),
            2: (67, 0),
            3: (50, 99),
            4: (61, 89),
            5: (91, 56),
            6: (2, 65),
            7: (38, 68),
            8: (3, 92),
            9: (59, 8),
            10: (30, 88),
            11: (30, 53),
            12: (11, 14),
            13: (52, 49),
            14: (18, 49),
            15: (64, 41),
            16: (28, 49),
            17: (91, 94),
            18: (51, 58),
            19: (30, 48),
        }
        self.proposed_tour = [0, 6, 8, 10, 3, 4, 17, 1, 5, 15, 13, 18, 7, 11, 14, 16, 19, 9, 2, 12, 0]
        self.proposed_cost = 446.84
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)
    
    def test_each_city_visited_once(self):
        unique_cities_visited = list(set(self.proposed_tour))
        self.assertEqual(len(unique_cities_visited), len(self.cities))
        self.assertEqual(len(self.proposed_tour) - 1, len(unique_cities_visited))  # -1 to account for duplicated depot city
    
    def test_correct_distance_calculation(self):
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        
        tour_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            city_a = self.cities[self.proposed_tour[i]]
            city_b = self.cities[self.proposed_tour[i + 1]]
            tour_cost += euclidean_distance(city_a, city_b)
        
        self.assertAlmostEqual(tour_cost, self.proposed_cost, places=2)
    
    def test_output(self):
        self.assertEqual(f"Tour: {self.proposed_tour}\nTotal travel cost: {self.proposed_cost:.2f}", 
                         f"Tour: [0, 6, 8, 10, 3, 4, 17, 1, 5, 15, 13, 18, 7, 11, 14, 16, 19, 9, 2, 12, 0]\nTotal travel cost: 446.84")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")