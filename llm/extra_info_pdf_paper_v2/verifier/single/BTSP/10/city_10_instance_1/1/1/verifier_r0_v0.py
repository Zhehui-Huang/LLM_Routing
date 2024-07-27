import unittest
import math

class TestTSPSolution(unittest.TestCase):
    cities = {
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

    tour = [0, 5, 2, 9, 7, 1, 6, 3, 8, 4, 0]
    total_travel_cost = 293.11
    max_distance = 81.61

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_exactly_once(self):
        visited_cities = self.tour[1:-1]
        unique_cities = set(visited_cities)
        self.assertEqual(len(visited_cities), len(unique_cities))
        self.assertEqual(set(range(1, 10)), unique_cities)

    def test_travel_cost(self):
        calculated_total_cost = 0.0
        max_calculated_distance = 0.0
        
        for i in range(1, len(self.tour)):
            start = self.tour[i - 1]
            end = self.tour[i]
            dist = math.sqrt((self.cities[end][0] - self.cities[start][0]) ** 2 + (self.cities[end][1] - self.cities[start][1]) ** 2)
            calculated_total_cost += dist
            if dist > max_calculated_distance:
                max_calculated_distance = dist

        self.assertAlmostEqual(calculated_total_cost, self.total_travel_cost, places=2)
        self.assertAlmostEqual(max_calulated_distance, TestTSPSolution.max_distance, places=2)

    def test_max_distance(self):
        max_calculated_distance = 0.0
        for i in range(1, len(self.tour)):
            start = self.tour[i - 1]
            end = self.tour[i]
            dist = math.sqrt((self.cities[end][0] - self.cities[start][0]) ** 2 + (self.cities[end][1] - self.cities[start][1]) ** 2)
            if dist > max_calculated_distance:
                max_calculated_distance = dist

        self.assertAlmostEqual(max_calculated_distance, self.max_distance, places=2)

    def test_solution_correctness(self):
        try:
            self.test_starts_and_ends_at_depot()
            self.test_visit_each_city_exactly_once()
            self.test_travel_cost()
            self.test_max_distance()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Create a test suite and add the desired test cases
suite = unittest.TestSuite()
suite.addTest(TestTSPSolution('test_solution_correctness'))

# Run the test suite
runner = unittest.TextTestRunner()
runner.run(suite)