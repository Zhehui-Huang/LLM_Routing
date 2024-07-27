import unittest
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the unit test class
class TestKTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
            0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
            5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
        }
        # Provided solution tour and cost
        self.tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
        self.reported_cost = 235.38

    def test_tour_length(self):
        self.assertEqual(len(set(self.tour)), 9, "Tour must visit 9 cities including repeats of the depot")

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0")

    def test_travel_cost(self):
        calculated_cost = sum(calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                               for i in range(len(self.tour) - 1))
        calculated_cost = round(calculated_cost, 2)  # rounding to match the given precision
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, 
                               msg="Travel cost should match the reported cost")

    def test_unique_cities_count(self):
        unique_cities = set(self.tour) - {0}
        self.assertEqual(len(unique_cities), 7, "Must visit exactly 8 unique cities including the depot")

# Function to run the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestKTravelingSalesmanSolution('test_tour_length'))
    suite.addTest(TestKTravelingSalesmanSolution('test_tour_start_end_at_depot'))
    suite.addTest(TestKTravelingSalesmanSolution('test_travel_cost'))
    suite.addTest(TestKTravelingSalesmanSolution('test_unique_cities_count'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Run tests and print result
print(run_tests())