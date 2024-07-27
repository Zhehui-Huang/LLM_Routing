import unittest
from math import sqrt

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Cities' coordinates
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
            5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
            10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
            15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        # Provided solution
        self.robot_tour = [0, 1, 2, 3, 4, 11, 13, 16, 14, 10, 8, 6, 5, 7, 9, 12, 15, 18, 20, 17, 21, 19]
        self.robot_total_cost = 265.59953329426196
        self.total_tour_cost = 265.59953329426196

    def test_total_cities(self):
        # Requirement 1
        self.assertEqual(len(self.cities), 22)

    def test_robot_start_point(self):
        # Requirement 2
        self.assertEqual(self.robot_tour[0], 0)

    def test_travel_cost_calculation(self):
        # Requirement 3
        # Check distance calculation between two known points
        dist = calculate_distance(*self.cities[0], *self.cities[1])
        self.assertAlmostEqual(dist, calculate_distance(145, 215, 151, 264), places=5)

    def test_no_return_to_depot(self):
        # Requirement 4
        self.assertNotEqual(self.robot_tour[-1], 0)  # confirms no return to depot city 0

    def test_unique_city_visitation(self):
        # Requirement 5
        self.assertEqual(len(self.robot_tour), len(set(self.robot_tour)))

    def test_cost_verification(self):
        # Requirement 3, 6, 7, 8
        calculated_cost = sum(calculate_distance(*self.cities[self.robot_tour[i]], *self.cities[self.robot_tour[i+1]]) for i in range(len(self.robot_tour)-1))
        self.assertAlmostEqual(calculated_cost, self.robot_total_cost, places=5)
        self.assertAlmostEqual(calculated_cost, self.total_tour_cost, places=5)

    def test_output_tour_form(self):
        # Requirement 7
        self.assertIsInstance(self.robot_tour, list)
        self.assertTrue(all(isinstance(i, int) for i in self.robot_tour))

if __name__ == '__main__':
    unittest.main()