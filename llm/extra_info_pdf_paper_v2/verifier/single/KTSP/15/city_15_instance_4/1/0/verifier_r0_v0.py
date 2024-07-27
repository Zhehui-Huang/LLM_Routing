import unittest
from math import sqrt

# Coordinates of the cities
cities_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_blocks[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total_distance

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Provided solution
        self.tour = [0, 10, 13, 14, 8, 3, 6, 4, 7, 2, 5, 1, 0, 0]
        self.expected_cost = 284.9033417753605

    def test_robot_starts_and_ends_depot_city(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_robot_visits_12_cities_excluding_duplicates(self):
        unique_cities = set(self.tour)
        # Account for the depot city being counted twice as it starts/ends the tour
        self.assertEqual(len(unique_cities), 12)

    def test_tour_representation_format(self):
        self.assertIsInstance(self.tour, list)
        all_integers = all(isinstance(item, int) for item in self.tour)
        self.assertTrue(all_integers)

    def test_total_travel_costs(self):
        calculated_cost = calculate_total_travel_cost(self.tour)
        self.assertAlmostEqual(calculated_cost, self.expected_cost, places=5)

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTourSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Check if all tests passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()