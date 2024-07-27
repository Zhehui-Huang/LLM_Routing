import unittest
import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40),  # Depot 0
            (37, 52),  # Depot 1
            (49, 43),  # City 2
            (52, 64),  # City 3
            (31, 62),  # City 4
            (52, 33),  # City 5
            (42, 41),  # City 6
            (52, 41),  # City 7
            (57, 58),  # City 8
            (62, 42),  # City 9
            (42, 57),  # City 10
            (27, 68),  # City 11
            (43, 67),  # City 12
            (58, 27),  # City 13
            (37, 69),  # City 14
            (61, 33),  # City 15
            (62, 63),  # City 16
            (63, 69),  # City 17
            (45, 35)   # City 18
        ]
        self.robot_0_tour = [0, 2, 18, 15, 7, 9, 8, 16, 17]
        self.robot_1_tour = [0, 1, 6, 10, 12, 14, 11, 4, 3, 5, 13]
        self.robot_0_cost = 96.3125266245847
        self.robot_1_cost = 122.29875957106864
        self.total_cost = 218.61128619565335

    def test_correct_number_of_cities_visited(self):
        all_cities_visited = set(self.robot_0_tour + self.robot_1_tour)
        self.assertEqual(len(all_cities_visited), 19)

    def test_start_from_depot_0(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 0)  # Incorrect starting point in robot's initial settings

    def test_calculate_travel_costs(self):
        def tour_cost(tour):
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]])
            return total_cost
        cost_robot_0 = tour_cost(self.robot_0_tour)
        cost_robot_1 = tour_cost(self.robot_1_tour)
        # Check if the tour costs are equal to the provided costs
        self.assertAlmostEqual(cost_robot_0, self.robot_0_cost)
        self.assertAlmostEqual(cost_robot_1, self.robot_1_cost)
        self.assertAlmostEqual(cost_robot_0 + cost_robot_1, self.total_cost)

    def test_output_format(self):
        # Output format should match the specified format.
        self.assertIsInstance(self.robot_0_tour, list)
        self.assertIsInstance(self.robot_1_tour, list)
        self.assertTrue(all(isinstance(x, int) for x in self.robot_0_tour))
        self.assertTrue(all(isinstance(x, int) for x in self.robot_1_tour))
        self.assertIsInstance(self.robot_0_cost, float)
        self.assertIsInstance(self.robot_1_cost, float)
        self.assertIsInstance(self.total_cost, float)

if __name__ == "__main__":
    # Assume the correction due to mistake in inputs where both robots start from Depot 0
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_correct_number_of_cities_visited'))
    test_suite.addTest(TestTSPSolution('test_start_from_depot_0'))
    test_suite.addTest(TestTSPSolution('test_calculate_travel_costs'))
    test_suite.addTest(TestTSPSolution('test_output_format'))

    result = unittest.TextTestRunner().run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")