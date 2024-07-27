import unittest
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class EvaluateSolution(unittest.TestCase):
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    tours = [
        [0, 14, 3, 11, 19, 1, 2, 9, 0],
        [0, 16, 4, 20, 21, 7, 0],
        [0, 15, 18, 6, 8, 10, 13, 5, 0],
        [0, 12, 17, 0]
    ]
    num_robots = 4
    num_cities = 22

    def test_unique_city_visit(self):
        all_cities = {i for i in range(self.num_cities)}
        tour_cities = set()
        for tour in self.tours:
            tour_cities.update(tour)
        self.assertTrue(tour_cities == all_cities)
    
    def test_minimize_max_distance(self):
        max_distance = 0
        for tour in self.tours:
            tour_distance = 0
            for i in range(len(tour) - 1):
                tour_distance += calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i + 1]])
            max_distance = max(max_distance, tour_distance)
        expected_max_distance = 260.5536533340566
        self.assertAlmostEqual(max_distance, expected_max_distance, places=2)

    def test_valid_tours(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(EvaluateSolution))
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")