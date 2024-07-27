import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (26, 60), 
            1: (73, 84), 
            2: (89, 36), 
            3: (15, 0), 
            4: (11, 10), 
            5: (69, 22), 
            6: (28, 11), 
            7: (70, 2), 
            8: (47, 50), 
            9: (60, 29), 
            10: (29, 26), 
            11: (85, 68), 
            12: (60, 1), 
            13: (71, 73), 
            14: (82, 47), 
            15: (19, 25), 
            16: (75, 9), 
            17: (52, 54), 
            18: (64, 72), 
            19: (14, 89)
        }
        self.proposed_tour = [0, 15, 4, 3, 6, 10, 9, 5, 14, 11, 1, 13, 18, 17, 8, 19, 0]
        self.reported_cost = 336.2246435926221

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.proposed_tour[-1], 0, "Tour does not end at the depot.")

    def test_exact_number_of_cities_visited(self):
        # Including the depot city which is counted as visited twice (start and end)
        self.assertEqual(len(set(self.proposed_tour)), 16, "Number of unique cities visited is not 16.")

    def test_tour_length_calculation(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        calculated_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            calculated_cost += euclidean_distance(self.cities[self.proposed_tour[i]], self.cities[self.proposed_tour[i + 1]])

        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=5, msg="Reported travel cost does not match calculated cost.")

    def test_output_format(self):
        self.assertIsInstance(self.proposed_tour, list, "Tour is not a list.")
        self.assertTrue(all(isinstance(city, int) for city in self.proposed_tour), "Tour does not consist of city indices.")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestKTSPSolution))
    test_runner = unittest.TextTestRunner()

    results = test_runner.run(test_suite)

    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")