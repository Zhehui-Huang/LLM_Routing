import unittest
import math

class TestTSPSolution(unittest.TestCase):
    cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
              (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
              (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
              (50, 28), (69, 9)]
    solution_tour = [0, 6, 2, 19, 15, 18, 17, 12, 13, 8, 9, 11, 10, 16, 4, 7, 5, 14, 3, 1, 0]
    reported_cost = 610.8605077173856

    def calculate_total_distance(self):
        total_calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            x1, y1 = self.cities[self.solution_tour[i]]
            x2, y2 = self.cities[self.solution_tour[i + 1]]
            total_calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return total_calculated_cost

    def test_solution(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
        
        tour_without_depot = self.solution_tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 19)  # making sure every city is visited exactly once

        calculated_cost = self.calculate_total_distance()
        self.assertAlmostEqual(calculated, self.reported_cost, places=5)

        self.assertTrue(self.solution_tour[0] == self.solution_tour[-1] == 0)
        self.assertTrue(isinstance(self.solution_tour, list))
        all_integers = all(isinstance(x, int) for x in self.solution_tour)
        self.assertTrue(all_integers)
        self.assertIsInstance(self.reported_cost, float)

        # Presuming correctness based on test passed status
        print("CORRECT")

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_solution'))
    runner = unittest.TextTestRunner()

    results = runner.run(test_suite)
    if not results.wasSuccessful():
        print("FAIL")

if __name__ == "__main__":
    main()