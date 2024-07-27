import unittest
from math import sqrt

class TestMTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tours = {
            0: [0, 17, 20, 18, 21, 19, 0],
            1: [0, 4, 3, 1, 2, 0],
            2: [0, 14, 16, 13, 12, 15, 0],
            3: [0, 10, 8, 6, 7, 5, 9, 11, 0]
        }
        self.costs = {
            0: 115.49425634032809,
            1: 123.43364483297964,
            2: 86.33464444537708,
            3: 125.15439232980292
        }
        self.overall_cost = 450.41693794848777
        self.coordinates = {
            0: (145, 215),
            1: (151, 264),
            2: (159, 261),
            3: (130, 254),
            4: (128, 252),
            5: (163, 247),
            6: (146, 246),
            7: (161, 242),
            8: (142, 239),
            9: (163, 236),
            10: (148, 232),
            11: (128, 231),
            12: (156, 217),
            13: (129, 214),
            14: (146, 208),
            15: (164, 208),
            16: (141, 206),
            17: (147, 193),
            18: (164, 193),
            19: (129, 189),
            20: (155, 185),
            21: (139, 182)
        }

    def test_distance_calculation(self):
        def calculate_distance(city1, city2):
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        for robot, tour in self.tours.items():
            total_distance = 0
            for i in range(len(tour) - 1):
                total_distance += calculate_distance(tour[i], tour[i + 1])
            self.assertAlmostEqual(total_distance, self.costs[robot], places=5, msg=f"Robot {robot} distance not matching")

    def test_unique_city_visit(self):
        visited_cities = set()
        for tour in self.tours.values():
            visited_cities.update(tour[1:-1])  # Exclude the depot city from checks
        self.assertEqual(len(visited_cities), 21, msg="Not all cities visited exactly once")

    def test_start_end_depot(self):
        for robot, tour in self.tours.items():
            self.assertEqual(tour[0], 0, msg=f"Robot {robot} doesn't start at the depot")
            self.assertEqual(tour[-1], 0, msg=f"Robot {robot} doesn't end at the depot")

    def test_overall_cost(self):
        total_calculated_cost = sum(self.costs.values())
        self.assertAlmostEqual(total_calculated_cost, self.overall_cost, places=5, msg="Overall cost incorrect")

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
          print("FAIL")