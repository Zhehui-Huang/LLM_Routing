import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
            (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
        ]
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.reported_cost = 315.5597914831042

    def test_visits_all_cities_exactly_once(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), len(self.cities))
        self.assertIn(0, unique_cities)  # Check depot city is included

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_correct_calculation_of_travel_cost(self):
        calculated_cost = calculate_total_cost(self.tour, self.cities)
        self.assertAlmostEqual(self.reported_cost, calculated_cost, places=5)

    def test_check_full_output(self):
        expected_output = "CORRECT"
        unique_cities = set(self.tour)
        if len(unique_cities) == len(self.cities) and self.tour[0] == 0 and self.tour[-1] == 0:
            calculated_cost = calculate_total_cost(self.tour, self.cities)
            if abs(calculated_cost - self.reported_cost) < 0.001:
                output = "CORRECT"
            else:
                output = "FAIL"
        else:
            output = "FAIL"
        self.assertEqual(output, expected_last_output)

if __name__ == '__main__':
    unittest.main()