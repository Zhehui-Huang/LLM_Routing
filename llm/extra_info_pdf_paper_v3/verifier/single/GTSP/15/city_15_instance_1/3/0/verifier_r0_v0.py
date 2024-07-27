import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = [
            (29, 51),  # Depot city 0
            (49, 20),  # City 1
            (79, 69),  # City 2
            (17, 20),  # City 3
            (18, 61),  # City 4
            (40, 57),  # City 5
            (57, 30),  # City 6
            (36, 12),  # City 7
            (93, 43),  # City 8
            (17, 36),  # City 9
            (4, 60),   # City 10
            (78, 82),  # City 11
            (83, 96),  # City 12
            (60, 50),  # City 13
            (98, 1)    # City 14
        ]
        self.groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.solution_tour = [0, 5, 10, 4, 11, 0]
        self.reported_total_cost = 184.24203302868492

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at depot city")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at depot city")

    def test_tour_visits_one_city_from_each_group(self):
        visited_cities = set(self.solution_tour[1:-1])  # omit the depot city
        for group in self.groups:
            self.assertEqual(len(visited_cities.intersection(set(group))), 1,
                             f"Tour should visit exactly one city from group {group}")

    def test_travel_cost_computed_correctly(self):
        computed_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i + 1]
            computed_cost += calculate_distance(
                self.city_coordinates[city1], self.city_conditions[city2])

        self.assertAlmostEqual(computed_cost, self.reported_total_cost, places=5,
                               msg="Computed travel cost should match the reported cost")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()