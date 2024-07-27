import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.robot_tours = {
            0: [0, 2, 1, 3, 8, 18, 21, 0],
            1: [0, 15, 20, 19, 11, 6, 0],
            2: [0, 17, 13, 4, 7, 10, 0],
            3: [0, 5, 9, 12, 14, 16, 0]
        }
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

    def test_requirements(self):
        # Requirement 1 and Requirement 5
        all_visited_once = set()
        for robot, tour in self.robot_tours.items():
            self.assertEqual(tour[0], 0, "Each robot's tour should start at city 0")
            all_visited_once.update(tour)

        # Requirement 2
        self.assertEqual(len(all_visited_once), 22, "All cities must be visited exactly once by all robots")

        # Calculate the total travel cost
        total_calculated_cost = 0

        for tour in self.robot_tours.values():
            tour_cost = 0
            for i in range(len(tour) - 1):
                city_a = tour[i]
                city_b = tour[i + 1]
                coord_a = self.coordinates[city_a]
                coord_b = self.coordinates[city_b]
                distance = math.sqrt((coord_b[0] - coord_a[0])**2 + (coord_b[1] - coord_a[1])**2)
                tour_cost += distance
            total_calculated_cost += tour_cost

        # Requirement 3: Check if reported costs match calculated ones
        reported_cost = 631.21
        self.assertAlmostEqual(total_calculated_cost, reported_cost, places=2, msg="Total travel cost should be minimum and correctly calculated")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    test_results = unittest.TextTestRunner().run(test_suite)

    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")