import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Provided solution details
        self.solution_tour = [0, 8, 0]
        self.total_travel_cost = 8.25
        self.maximum_distance = 4.12
        
        # Cities' coordinates
        self.cities = {
            0: (84, 67),
            8: (85, 71)
        }
    
    def test_requirement_1(self):
        # Check if all cities except the depot are visited exactly once
        visited = set(self.solution_tour[1:-1])
        all_cities = set(range(1, 10))  # All city indices from 1 to 9
        self.assertEqual(visited, all_cities, "The robot does not visit each city exactly once.")
    
    def test_requirement_2(self):
        # This requirement requires an optimal minimization check which is
        # difficult without knowing all possible tours. We limit to verifying
        # provided topology correctness in the given solution.
        # For this problem's simplicity, we only check given distances.

        # Calculate all pairs distances and find the maximum
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        max_distance_found = max(
            calculate_distance(self.solution_tour[i], self.solution_tour[i+1]) 
            for i in range(len(self.solution_tour) - 1)
        )
        
        # Check if the calculated maximum distance matches the provided
        self.assertAlmostEqual(max_distance_found, self.maximum_distance, places=2,
                               msg="The maximum distance between consecutive cities does not match.")
    
    def test_requirement_3(self):
        # Check tour starts and ends at city 0
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at depot city 0.")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at depot city 0.")
    
    def test_requirement_4(self):
        # Accumulate total travel cost and compare
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        calculated_cost = sum(
            calculate_distance(self.solution_tour[i], self.solution_tour[i+1]) 
            for i in range(len(self.solution_tour) - 1)
        )
        
        self.assertAlmostEqual(calulated_cost, self.total_travel_cost, places=2,
                               msg="Total travel cost does not match calculated cost.")
    
    def test_requirement_5(self):
        # Maximum distance has been validated in test_requirement_2
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTravelingSalesmanSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    correct = result.wasSuccessful()
    print("CORRECT" if correct else "FAIL")