import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        self.tour_solution = [0, 1, 2, 4, 9, 6, 8, 3, 5, 7, 0]
        self.total_cost_solution = 418.64
    
    def test_tour_starts_and_ends_with_depot(self):
        # Requirement 1
        self.assertEqual(self.tour_solution[0], 0)
        self.assertEqual(self.tour_solution[-1], 0)

    def test_each_city_visited_once_except_depot(self):
        # Requirement 2
        visited = set(self.tour_solution)
        for city in self.cities:
            if city == 0:
                self.assertEqual(self.tour_solution.count(city), 2)
            else:
                self.assertEqual(self.tour_solution.count(city), 1)

    def test_correct_total_travel_cost(self):
        # Requirement 3 and 5
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        total_cost = 0
        for i in range(len(self.tour_solution) - 1):
            city_from = self.tour_solution[i]
            city_to = self.tour_solution[i+1]
            total_cost += calculate_distance(city_from, city_to)
        
        self.assertAlmostEqual(total_cost, self.total_cost_solution, places=2)

    def test_correct_tour_output(self):
        # Requirement 4
        self.assertIsInstance(self.tour_solution, list)
        for city in self.tour_solution:
            self.assertIn(city, self.cities)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTSPSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")