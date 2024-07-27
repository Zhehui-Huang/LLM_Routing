import unittest
import math

city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
        total_travel_cost = 410.04
        max_distance_between_cities = 89.01
        
        # Requirement 1: All cities visited exactly once and tour starts/ends at city 0
        unique_cities = set(tour)
        self.assertEqual(len(unique_cities), 20)
        self.assertEqual(tour[0], tour[-1], 0)
        
        # Calculate total travel cost and check with provided value
        calculated_total_cost = sum(
            math.sqrt(
                (city_coordinates[tour[i]][0] - city_coordinates[tour[i+1]][0]) ** 2 +
                (city_coordinates[tour[i]][1] - city_coordinates[tour[i+1]][1]) ** 2
            )
        for i in range(len(tour) - 1))

        # Compare calculated total cost with given using a small tolerance due to possible floating point arithmetic differences
        self.assertAlmostEqual(calculated_total_cost, total_travel_cost, places=2)

        # Check maximum distance between any two consecutive cities
        calculated_max_distance = max(
            math.sqrt(
                (city_coordinates[tour[i]][0] - city_coordinates[tour[i+1]][0]) ** 2 +
                (city_coordinates[tour[i]][1] - city_coordinates[tour[i+1]][1]) ** 2
            )
        for i in range(len(tour) - 1))

        self.assertAlmostEqual(calculated_max_distance, max_distance_between_cities, places=2)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")