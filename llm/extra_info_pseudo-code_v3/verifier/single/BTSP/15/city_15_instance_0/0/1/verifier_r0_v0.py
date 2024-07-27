import unittest
from math import sqrt

# Coordinates of the cities
cities = [
    (9, 93),  # Depot city-0
    (8, 51),  # City-1
    (74, 99), # City-2
    (78, 50), # City-3
    (21, 23), # City-4
    (88, 59), # City-5
    (79, 77), # City-6
    (63, 23), # City-7
    (19, 76), # City-8
    (21, 38), # City-9
    (19, 65), # City-10
    (11, 40), # City-11
    (3, 21),  # City-12
    (60, 55), # City-13
    (4, 39)   # City-14
]

# Solution provided
solution_tour = [0, 8, 10, 1, 11, 14, 9, 12, 4, 7, 3, 5, 13, 6, 2, 0]
solution_total_cost = 358.43
solution_max_distance = 65.28

def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTourSolution(unittest.TestCase):
    def test_number_of_cities(self):
        # Includes the depot city
        self.assertEqual(len(cities), 15)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_all_cities_visited_exactly_once(self):
        self.assertCountEqual(solution_tour[1:-1], list(range(1, 15)))

    def test_total_travel_cost(self):
        computed_cost = 0
        max_distance = 0
        for i in range(1, len(solution_tour)):
            dist = calculate_distance(cities[solution_tour[i-1]], cities[solution_tour[i]])
            computed_cost += dist
            if dist > max_distance:
                max_distance = dist
        self.assertAlmostEqual(computed_cost, solution_total_cost, places=2)
        self.assertAlmostEqual(max_distance, solution_max_distance, places=2)

    def test_output_exists(self):
        self.assertIsInstance(solution_tour, list)
        self.assertIsInstance(solution_total_cost, float)
        self.assertIsInstance(solution_max_distance, float)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTourSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")