import unittest
import math

# Define a function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Define the coordinates of the cities
        self.cities = {
            0: (26, 60),
            1: (73, 84),
            2: (89, 36),
            3: (15, 0),
            4: (11, 10),
            5: (69, 22)
        }

        # Solution provided
        self.tour = [0, 1, 2, 5, 3, 4, 0]
        self.expected_max_distance = 58.309518948453004
        self.provided_total_cost = 249.0640341092713

        # Calculate actual total cost and max distance between consecutive cities
        self.calculated_total_cost = 0
        self.distances = []

        for i in range(len(self.tour) - 1):
            distance = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            self.distances.append(distance)
            self.calculated_total_cost += distance

        self.calculated_max_distance = max(self.distances)

    def test_path_validity(self):
        self.assertEqual(self.tour[0], 0, "Does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Does not end at the depot.")

    def test_visit_all_cities_once(self):
        unique_cities = set(self.tour[:-1])  # exclude the last return to depot
        self.assertEqual(len(unique_cities), 6, "Not all cities are visited exactly once.")

    def test_max_distance(self):
        self.assertAlmostEqual(self.calculated_max_distance, self.expected_max_distance, "Maximum distance does not match.")

    def test_total_cost(self):
        self.assertAlmostEqual(self.calculated_total_cost, self.provided_total_cost, "Total cost does not match.")

# Function to execute unit tests and check results
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_path_validity'))
    suite.addTest(TestTSPSolution('test_visit_all_cities_once'))
    suite.addTest(TestTSPSolution('test_max_distance'))
    suite.addTest(TestTSPSolution('test_total_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    correct = result.wasSuccessful()
    
    if correct:
        print("CORRECT")
    else:
        print("FAIL")

# Execute tests
run_tests()