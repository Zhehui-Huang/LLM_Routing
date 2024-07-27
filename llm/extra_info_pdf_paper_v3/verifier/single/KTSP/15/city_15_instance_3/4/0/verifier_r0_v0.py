import unittest
import math

# Data provided, including given tour and cost
city_coordinates = [
    (16, 90),  # Depot city
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Provided tour and travel cost
provided_tour = [0, 1, 4, 5, 6, 8, 9, 10, 13, 14, 0]
provided_cost = 208.79

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_tour_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return round(total_cost, 2)

class TestTSPSolution(unittest.TestCase):
    def test_total_cities(self):
        self.assertEqual(len(city_coordinates), 15)

    def test_depot_city_coordinates(self):
        self.assertEqual(city_coordinates[0], (16, 90))

    def test_robot_starts_and_ends_at_depot(self):
        self.assertEqual(provided_tour[0], 0)
        self.assertEqual(provided_tour[-1], 0)

    def test_robot_visits_exactly_10_cities(self):
        self.assertEqual(len(set(provided_tour)), 10)

    def test_travel_cost_calculation(self):
        calculated_cost = calculate_total_tour_cost(provided_tour, city_coordinates)
        self.assertEqual(calculated_cost, provided_cost)

    def test_tour_output_format(self):
        self.assertIsInstance(provided_tour, list)
        for city in provided_tour:
            self.assertIsInstance(city, int)

    def test_cost_output(self):
        self.assertIsInstance(provided_cost, float)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_total_cities'))
    suite.addTest(TestTSPSolution('test_depot_city_coordinates'))
    suite.addTest(TestTSPSolution('test_robot_starts_and_ends_at_depot'))
    suite.addTest(TestTSPSolution('test_robot_visits_exactly_10_cities'))
    suite.addTest(TestTSPSolution('test_travel_cost_calculation'))
    suite.addTest(TestTSPSolution('test_tour_output_format'))
    suite.addTest(TestTSPSolution('test_cost_output'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return "CORRECT" if result.wasSuccessful() else "FAIL"

# Run the tests
print(run_tests())