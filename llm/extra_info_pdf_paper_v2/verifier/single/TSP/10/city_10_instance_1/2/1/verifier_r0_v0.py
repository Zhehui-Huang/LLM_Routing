import unittest
from math import sqrt

# Define the class to hold the TestCases
class TestTourSolution(unittest.TestCase):
    
    def setUp(self):
        # Cities coordinates (city index: (x, y))
        self.cities = {
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
        # Provided tour and cost
        self.tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
        self.cost = 279
    
    def test_tour_start_and_end(self):
        # Check if tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot")
    
    def test_visit_each_city_once(self):
        # Check if all cities are visited
        visited_cities = sorted(self.tour[1:-1])
        expected_cities = list(range(1, 10))
        self.assertEqual(visited_cities, expected_cities, "Not all cities are visited exactly once")
    
    def test_travel_cost(self):
        # Calculate the travel cost based on the Euclidean distance
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            calculated_cost += sqrt((x2 - x1)**2 + (y2 - y1)**2)
        calculated_cost = round(calculated_cost)
        self.assertEqual(calculated_cost, self.cost, f"Expected cost {self.cost}, but got {calculated_cost}")
    
    def test_output_format(self):
        # Check the format of the tour and cost output
        self.assertIsInstance(self.tour, list, "Tour should be list type")
        self.assertIsInstance(self.cost, int, "Cost should be integer type")
        self.assertTrue(all(isinstance(city, int) for city in self.tour), "All elements in the tour should be integers")
        
# Running the tests
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTourSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")