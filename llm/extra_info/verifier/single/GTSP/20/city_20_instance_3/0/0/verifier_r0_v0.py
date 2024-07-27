import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.groups = {
            0: [4, 10, 13, 17],
            1: [6, 7, 14],
            2: [9, 12, 16],
            3: [2, 5, 15],
            4: [1, 3, 19],
            5: [8, 11, 18]
        }
        self.solution_tour = [0, 19, 6, 2, 13, 12, 18, 0]
        self.provided_cost = 158.65862319241174

    def euclidean_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)  # Start at depot
        self.assertEqual(self.solution_tour[-1], 0)  # End at depot

    def test_visit_one_city_from_each_group(self):
        visited = set(self.solution_tour[1:-1])  # exclude the depot city at start and end
        for group in self.groups.values():
            self.assertTrue(any(city in visited for city in group))

    def test_calculate_travel_cost_correctly(self):
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1, city2 = self.solution_tour[i], self.solution_tour[i + 1]
            calculated_cost += self.euclidean_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=5)
        
    def test_output_format(self):
        self.assertIsInstance(self.solution_tour, list)
        self.assertIsInstance(self.provided_cost, float)
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    results = unittest.TextTestRunner().run(suite)
    if not results.failures and not results.errors:
        print("CORRECT")
    else:
        print("FAIL")

run_tests()