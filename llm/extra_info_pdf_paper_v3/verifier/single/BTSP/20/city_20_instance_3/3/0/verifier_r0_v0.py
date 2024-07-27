import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
            (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
            (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
            (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.proposed_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.proposed_tour[-1], 0, "Tour should end at depot city 0")
    
    def test_visits_all_cities_once(self):
        visited_cities = self.proposed_tour[:-1]  # removing the last entry as it should be the same as the first
        self.assertCountEqual(visited_cities, list(range(20)), "Each city must be visited exactly once")
    
    def test_minimizes_longest_distance(self):
        max_distance = 0
        for i in range(len(self.proposed_tour) - 1):
            city1, city2 = self.proposed_tour[i], self.proposed_tour[i + 1]
            distance = calculate_distance(self.cities[city1], self.cities[city2])
            if distance > max_distance:
                max_distance = distance
        
        target_max_distance = 68.15423684555495  # From the provided solution
        self.assertAlmostEqual(max_distance, target_max_distance, places=5, msg="The maximum distance between consecutive cities should be minimized")
        
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTSPSolution)
    test_result = unittest.TextTestRunner().run(test_suite)
    print("CORRECT" if test_result.wasSuccessful() else "FAIL")