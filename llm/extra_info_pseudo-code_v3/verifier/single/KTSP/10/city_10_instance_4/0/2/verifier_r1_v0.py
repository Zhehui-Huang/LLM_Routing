import unittest
from math import sqrt

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
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
        # Provided solution tour and cost
        self.tour = [0, 4, 3, 6, 9, 1, 5, 7, 0]
        self.reported_cost = 246.14
    
    def calculate_distance(self, city1, city2):
        # Calculate Euclidean distance between two cities
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_tour_start_and_end_at_depot(self):
        # Check if tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_exactly_eight_cities_including_depot(self):
        # Check if there are exactly 8 cities visited, including the depot
        self.assertEqual(len(set(self.tour)), 8)

    def test_correct_travel_cost_calculation(self):
        # Calculate the travel cost from the tour
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += self.calculate_distance(self.tour[i], self.tour[i + 1])
        # Check if the total cost matches the reported cost
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_output_tour_format(self):
        # Check if tour output format is correct [0, ..., 0]
        self.assertEqual(self.tour[0], self.tour[-1])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_tour_start_and_end_at_depot'))
    suite.addTest(TestTravelingSalesmanSolution('test_exactly_eight_cities_including_depot'))
    suite.addTest(TestTravelingSalesmanSolution('test_correct_travel_cost_calculation'))
    suite.addTest(TestTravelingSalesmanSolution('test_output_tour_format'))
    
    # Running the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Determining if the result is correct based on the test results
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Output based on the unit test results
output = run_tests()
print(output)