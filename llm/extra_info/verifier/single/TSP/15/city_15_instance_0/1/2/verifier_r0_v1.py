import math
import unittest

# Provided solution
solution_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
solution_cost = 373.97393412233544

# Coordinates of cities including the depot city (0)
cities = [
    (9, 93), # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39),
]

class TestVRPSolution(unittest.TestCase):
    def test_tour_start_end_depot(self):
        # Check if the tour starts and ends at depot city 0
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_unique_visit_except_depot(self):
        # Check if all cities are visited exactly once (excluding the redundant visit to depot city)
        visits = sorted(solution_tour[1:-1])
        expected_visits = list(range(1, 15))
        self.assertEqual(visits, expected_visits)

    def test_correct_number_of_cities(self):
        # Check the number of cities (15 including depot)
        self.assertEqual(len(cities), 15)

    def test_travel_cost(self):
        # Calculate euclidean distance function
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        # Calculate total tour distance
        total_distance = 0
        for i in range(len(solution_tour) - 1):
            city_a = solution_tour[i]
            city_b = solution_tour[i + 1]
            total_distance += euclidean_lifetime_distance(cities[city_a], cities[city_b])

        # Compare the calculated tour cost with the provided solution cost
        self.assertAlmostEqual(total_distance, solution_cost, places=5)

def main():
    # Load tests from TestVRPSolution
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestVRPSolution)
    
    # Run tests and determine correctness
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()