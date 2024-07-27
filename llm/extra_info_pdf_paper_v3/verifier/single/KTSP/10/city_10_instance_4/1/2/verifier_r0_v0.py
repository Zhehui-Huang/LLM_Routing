import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
        self.reported_total_cost = 235.38

    def test_coordinates_count(self):
        # [There are 10 cities with specified coordinates]
        self.assertEqual(len(self.coordinates), 10)

    def test_start_end_at_depot(self):
        # [The tour should start and end at the depot city 0]
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_total_cities_visited(self):
        # [The robot must visit exactly 8 cities, including the depot city]
        self.assertEqual(len(set(self.tour)), 8)

    def test_calculate_total_cost(self):
        # [Travel cost is calculated as the Euclidean distance between cities]
        def cost(a, b):
            return math.sqrt((self.coordinates[a][0] - self.coordinates[b][0]) ** 2 + 
                             (self.coordinates[a][1] - self.coordinates[b][1]) ** 2)
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += cost(self.tour[i], self.tour[i + 1])
        # Rounding off to match the precision in the reported cost
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2)

    def test_solution_correctness(self):
        # This combines all the tests to assert the total correctness
        try:
            self.test_coordinates_count()
            self.test_start_end_at_depot()
            self.test_total_cities_visited()
            self.test_calculate_total_cost()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Run the tests
suite = unittest.TestSuite()
suite.addTest(TestTourSolution('test_solution_correctness'))
runner = unittest.TextTestRunner()
runner.run(suite)