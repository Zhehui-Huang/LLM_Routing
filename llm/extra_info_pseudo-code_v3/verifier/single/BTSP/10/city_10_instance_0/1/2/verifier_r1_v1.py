import unittest
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestBottleneckTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (50, 42), # Depot city 0
            (41, 1),
            (18, 46),
            (40, 98),
            (51, 69),
            (47, 39),
            (62, 26),
            (79, 31),
            (61, 90),
            (42, 49) 
        ]
        self.tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
        self.reported_total_cost = 328.40
        self.reported_max_distance = 45.19
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_exactly_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 10)
        self.assertTrue(0 in unique_cities)

    def test_reported_total_cost(self):
        computed_cost = sum(euclidean_distance(self.cities[self.tour[i]][0], self.cities[self.tour[i]][1], 
                                               self.cities[self.tour[i+1]][0], self.cities[self.tour[i+1]][1]) 
                            for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(computed_cost, self.reported_total_cost, places=2)
    
    def test_max_distance_between_cities(self):
        computed_max_distance = max(euclidean_distance(self.cities[self.tour[i]][0], self.cities[self.tour[i]][1], 
                                                        self.cities[self.tour[i+1]][0], self.cities[self.tour[i+1]][1])
                                    for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(computed_max_distance, self.reported_max_distance, places=2)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBottleneckTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
#important corrections        
        print("FAIL")

run_tests()