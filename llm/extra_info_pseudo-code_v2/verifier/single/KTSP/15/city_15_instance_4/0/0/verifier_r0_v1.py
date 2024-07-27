import unittest
from math import sqrt

# Coordinates of the cities
cities = {
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

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

class TestRobotTour(unittest.TestCase):
    def test_tour_requirements(self):
        # Given solution
        tour = [0, 5, 9, 2, 4, 12, 6, 3, 14, 8, 10, 1, 0]
        total_cost = 250.0416611502525
        
        # Test Requirement 1: Tour starts and ends at depot city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Test Requirement 2: Exactly 12 cities are visited, including the depot
        self.assertEqual(len(set(tour)), 12)

        # Test Requirement 3: Check the total travel cost for correctness
        calculated_cost = calculate_total_travel_cost(tour, cities)
        self.assertAlmostEqual(calculated_cost, total_cost, places=5)

        # Test Requirement 4: Tour should start and end at city 0
        # Already covered in requirement 1, also checking if the output includes the depot as the first and last city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Test Requirement 5: Validating that the total cost output is of type float
        self.assertIsInstance(total_cost, float)

runner = unittest.TextTestRunner()
unittest.main(argv=[''], exit=False)