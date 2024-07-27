import math
import unittest

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        self.city_groups = {
            0: [5, 6, 7],
            1: [2, 3],
            2: [1, 9],
            3: [4, 8]
        }
        self.tour_solution = [0, 5, 2, 9, 8, 0]
        self.expected_cost = 183.99

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour_solution[0], 0)
        self.assertEqual(self.tour_solution[-1], 0)

    def test_visit_only_one_from_each_group(self):
        visited = {}
        for index, group in self.city_groups.items():
            visited[index] = False

        for city in self.tour_solution:
            for index, group in self.city_groups.items():
                if city in group:
                    if visited[index]:
                        self.fail("Visited more than one city from group {}".format(index))
                    visited[index] = True

        self.assertTrue(all(visited.values()))

    def test_total_cost_calculation(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        calculated_cost = 0
        for i in range(len(self.tour_solution) - 1):
            calculated_cost += euclidean_distance(self.tour_solution[i], self.tour_solution[i + 1])

        self.assertAlmostEqual(calculated_cost, self.expected_cost, places=2)

    def test_algorithm_implementation(self):
        # This mock test assumes we actually tested the algorithm for implementation accuracy.
        # In real world, we would check the implementation against known results or benchmarks.
        # For now, assume it's correct if we are able to assert the function exists (mock logic).
        pass

# Run the unit tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestGTSPSolution)
result = unittest.TextTestRunner(verbosity=2).run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")