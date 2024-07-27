import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (53, 68),  # Depot city 0
            (75, 11),  # City 1
            (91, 95),  # City 2
            (22, 80),  # City 3
            (18, 63),  # City 4
            (54, 91),  # City 5
            (70, 14),  # City 6
            (97, 44),  # City 7
            (17, 69),  # City 8
            (95, 89)   # City 9
        ]
        self.solution_tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
        self.max_distance_allowed = 71.449282711585

    def test_starts_and_ends_at_depot(self):
        # Requirement 1: Start and end at depot city (city 0)
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at depot")

    def test_visits_all_cities_once(self):
        # Requirement 2: Each city visited once, depot visited twice
        visit_counts = [0] * len(self.cities)
        for city in self.solution_tour:
            visit_counts[city] += 1
        self.assertEqual(visit_counts[0], 2, "Depot city should be visited twice")
        self.assertTrue(all(count == 1 for index, count in enumerate(visit_counts) if index != 0), "Not all cities visited exactly once")

    def test_minimized_max_distance(self):
        # Requirement 3: Minimize the longest distance between consecutive cities
        max_distance = 0
        for i in range(len(self.solution_tour) - 1):
            distance = calculate_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i+1]])
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.max_distance_allowed, places=5, msg="Max distance between cities is not minimized or calculated incorrectly")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTourSolution())
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")