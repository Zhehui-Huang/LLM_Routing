import unittest
import math

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution_tour = [0, 1, 7, 3, 9, 4, 0]
        self.calculated_cost = 128.66
        self.cities_coordinates = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }
    
    def test_starts_and_ends_at_depot(self):
        """ Test if the tour starts and ends at the depot city 0 """
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_visits_exactly_six_cities(self):
        """ Test if the robot visits exactly 6 cities, including the depot city """
        unique_cities = set(self.solution_tour)
        self.assertEqual(len(unique_cities), 6)
    
    def test_correct_travel_cost_calculation(self):
        """ Test if the travel cost is correctly calculated using Euclidean distance """
        total_distance = 0
        for i in range(len(self.solution_tour) - 1):
            x1, y1 = self.cities_coordinates[self.solution_tour[i]]
            x2, y2 = self.cities_coordinates[self.solution_tour[i + 1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total_distance += distance
        self.assertAlmostEqual(total_distance, self.calculated_cost, places=2)

    def test_output_format(self):
        """ Test if the output is in the correct format """
        # Checking if the first and last elements in the output tour list are 0
        self.assertTrue(self.solution_tour[0] == self.solution_tour[-1] == 0)
        # Checking if the total length of the tour is correct
        self.assertEqual(len(self.solution_tour), 7)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_starts_and_ends_at_depot'))
    suite.addTest(TestSolution('test_visits_exactly_six_cities'))
    suite.addTest(TestSolution('test_correct_travel_cost_calculation'))
    suite.addTest(TestSolution('test_output_format'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()