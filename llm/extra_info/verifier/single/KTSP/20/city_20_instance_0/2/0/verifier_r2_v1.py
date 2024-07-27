import math
import unittest

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # city coordinates as provided
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            4: (25, 18),
            16: (13, 43)
        }
        
        # details of the tour solution to test
        self.solution_tour = [0, 1, 4, 16, 0]
        self.solution_cost = 111.71676092282922
        
        # expected algorithm to compute the travel cost
        self.expected_cost = 0
        for i in range(len(self.solution_tour)-1):
            self.expected_cost += compute_euclidean_distance(
                self.cities[self.solution_tour[i]], 
                self.cities[self.solution_tour[i + 1]]
            )
    
    def test_start_end_at_depot(self):
        # Test if the tour starts and ends at depot city 0
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
        
    def test_exactly_four_cities(self):
        # Test if the tour visits exactly 4 cities (including the depot)
        unique_cities = set(self.solution_tour)
        self.assertEqual(len(unique_cities), 4)
        
    def test_calculate_travel_costs(self):
        # Test if the travel cost computation is correct (Euclidean distance)
        computed_cost = round(self.expected_cost, 10)
        solution_cost = round(self.solution_cost, 10)
        self.assertAlmostEqual(computed_cost, solution_cost, places=5)
    
    def test_return_correct_format(self):
        # Test if the proper return format is provided (cities list and total cost)
        self.assertIsInstance(self.solution_tour, list)
        self.assertIsInstance(self.solution_cost, float)

def main():
    # Run the tests
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRobotTour))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Check if all tests passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()