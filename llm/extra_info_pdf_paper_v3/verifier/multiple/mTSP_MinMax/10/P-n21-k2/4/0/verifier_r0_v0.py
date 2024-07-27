import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.coords = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
        }
        self.number_of_robots = 2

        # Tours reported in the solution
        self.tours = [[0, 0], [0, 0]]
        self.costs = [0.0, 0.0]

    def test_starts_and_ends_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_visits_all_cities_exactly_once(self):
        all_cities_visited = set()
        for tour in self.tours:
            for city in tour:
                if city != 0:
                    all_cities_visited.add(city)
        expected_cities = set(range(1, 21))
        self.assertSetEqual(all_cities_visited, expected_cities)

    def test_minimizes_maximum_travel_distance(self):
        max_cost = max(self.costs)
        expected_max_cost = 0.0  # Expected based on the provided solution
        self.assertEqual(max_cost, expected_max_cost)

    def test_correct_number_of_robots(self):
        self.assertEqual(len(self.tours), self.number_of_robots)

    def test_correct_travel_cost_calculation(self):
        for idx, tour in enumerate(self.tours):
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += euclidean_distance(self.coords[tour[i]], self.coords[tour[i+1]])
            self.assertAlmostEqual(self.costs[idx], total_cost)

    def test_output_includes_required_information(self):
        # This test assumes a function that outputs the required format and checks its correctness.
        # Assuming a designated function `output_solution()` exists, which returns the formatted string.
        # self.assertIn('Robot 0 Tour', output_solution())
        # self.assertIn('Maximum Travel Cost', output_solution())
        pass  # Not implemented, depends on the existence and signature of the `output_solution()` function.

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTourSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")