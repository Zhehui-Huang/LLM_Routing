import unittest
import math

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution_tour = [0, 8, 10, 2, 6, 5, 7, 4, 12, 14, 1, 11, 9, 13, 3, 0]
        self.solution_cost = 436.81
        self.cities_coordinates = {
            0: (9, 93),
            1: (8, 51),
            2: (74, 99),
            3: (78, 50),
            4: (21, 23),
            5: (88, 59),
            6: (79, 77),
            7: (63, 23),
            8: (19, 76),
            9: (21, 38),
            10: (19, 65),
            11: (11, 40),
            12: (3, 21),
            13: (60, 55),
            14: (4, 39)
        }

    def euclidean_distance(self, coord_a, coord_b):
        return math.sqrt((coord_a[0] - coord_b[0]) ** 2 + (coord_a[1] - coord_b[1]) ** 2)

    def calculate_total_tour_cost(self):
        total_cost = 0
        coordinates = self.cities_coordinates
        tour = self.solution_tour
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            total_cost += self.euclidean_distance(coordinates[city_from], coordinates[city_to])
        return round(total_cost, 2)

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Should start at depot city 0")
        self.assertEqual(self.solution_tur[-1], 0, "Should end at depot city 0")

    def test_visit_each_city_once(self):
        except_depot = set(range(1, 15))
        tour_without_depot = set(self.solution_tour[1:-1])
        self.assertSetEqual(tour_without_depot, except_depot, "Each city must be visited exactly once")

    def test_correct_travel_cost(self):
        calculated_cost = self.calculate_total_tour_cost()
        self.assertAlmostEqual(calculated_cost, self.solution_cost, "The reported total travel cost should match the calculated cost")

    def test_output_format(self):
        self.assertIsInstance(self.solution_tour, list, "Tour should be a list of city indices")
        self.assertIsInstance(self.solution_cost, float, "Total travel cost should be a float")

    def run_all_tests(self):
        # Activating the testing process
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestSolution))
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        if result.wasSuccessful():
            print("CORRECT")
        else:
            print("FAIL")

# Assuming the script execution is to trigger test routine
if __name__ == '__main__':
    test_solution = TestSolution()
    test_solution.run_all_tests()