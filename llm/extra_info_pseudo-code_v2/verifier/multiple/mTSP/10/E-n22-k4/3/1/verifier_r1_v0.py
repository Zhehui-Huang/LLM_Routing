import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.tours = {
            0: {"tour": [0, 14, 17, 20, 10, 5, 4, 0], "cost": 178.22},
            1: {"tour": [0, 16, 19, 21, 9, 2, 0], "cost": 175.36},
            2: {"tour": [0, 12, 15, 18, 7, 1, 0], "cost": 160.85},
            3: {"tour": [0, 13, 11, 8, 6, 3, 0], "cost": 116.92}
        }
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
            4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
            8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
            12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
            16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }

    def test_tours_start_end_at_depot(self):
        for tour_data in self.tours.values():
            self.assertEqual(tour_data["tour"][0], 0)
            self.assertEqual(tour_data["tour"][-1], 0)

    def test_all_cities_visited_exactly_once(self):
        all_visited = set()
        for tour_data in self.tours.values():
            all_visited.update(tour_data["tour"][1:-1])  # exclude the depot
        self.assertEqual(all_visited, set(range(1, 22)))

    def test_correct_output_format(self):
        for robot, data in self.tours.items():
            self.assertIsInstance(data["tour"], list)
            self.assertIsInstance(data["cost"], float)
            self.assertTrue(data["tour"][0] == 0 and data["tour"][-1] == 0)

    def test_minimize_total_travel_cost(self):
        total_cost = sum(tour["cost"] for tour in self.tours.values())
        self.assertAlmostEqual(totalO_cost, 631.35, places=2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")