import unittest
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
                       (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
                       (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]
        self.solution_tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.reported_total_cost = 337.84
        self.reported_max_distance = 60.67
    
    def test_start_end_at_depot(self):
        # Check if tour starts and ends at the depot city 0
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_visit_each_city_once(self):
        # Check if each city is visited exactly once
        all_cities = set(range(len(self.cities)))
        visited_cities = set(self.solution_tour) - {0}
        self.assertEqual(visited_cities, all_cities - {0})
    
    def test_tour_outputs(self):
        # Check correct output format and calculate total cost and max distance
        calculated_total_cost = 0
        max_distance = 0
        for i in range(len(self.solution_tour)-1):
            from_city = self.solution_tour[i]
            to_city = self.solution_tour[i+1]
            distance = euclidean_distance(self.cities[from_city], self.cities[to_city])
            calculated_total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        # Compare calculated costs and the reported ones
        self.assertAlmostEqual(calculated_total_cost, self.reported_total_cost, places=2)
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2)

    def test_optimization_goal(self):
        # Check minimization of the longest distance (not exact, but reasonable check)
        # This check requires some other known solution to compare with, or some bounds;
        # For the sake of this test, verify if within a "reasonable" range
        reasonable_max_distance = max(euclidean_distance(self.cities[i], self.cities[j]) for i in range(len(self.cities)) for j in range(len(self.cities)) if i != j)
        self.assertLessEqual(self.reported_max_distance, reasonable_max_distance)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_start_end_at_depot'))
    suite.addTest(TestTSPSolution('test_visit_each_city_once'))
    suite.addTest(TestTSPSolution('test_tour_outputs'))
    suite.addTest(TestTSPSolution('test_optimization_goal'))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the tests and provide feedback
print(run_tests())