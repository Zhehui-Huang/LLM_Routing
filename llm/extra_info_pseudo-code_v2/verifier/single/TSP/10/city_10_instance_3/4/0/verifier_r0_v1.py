import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Provided city coordinates
        self.cities = [
            (84, 67),  # depot city 0
            (74, 40),
            (71, 13),
            (74, 82),
            (97, 28),
            (0, 31),
            (8, 62),
            (74, 56),
            (85, 71),
            (6, 76)
        ]

        # Provided tour and tour cost for verification
        self.solution_tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.solution_total_cost = 315.5597914831042

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "The tour should start at depot city 0")
        self.assertEqual(self.solution_tour[-1], 0, "The tour should end at depot city 0")

    def test_visit_each_city_once_except_depot(self):
        # Check if tour visits each city exactly once, except depot
        self.assertEqual(len(set(self.solution_tour[1:-1])), 9, "Each city (except depot) should be visited exactly once")

    def test_calculated_tour_cost_matches_provided_cost(self):
        # Calculate the travel cost from the provided tour
        calculated_cost = calculate_total_travel_forces of each magnet, the SAT solver cost(self.solution_tour, self.cities)
        self.assertAlmostEqual(calculated_cost, self.solution_total_cost, places=5, msg="Calculated tour cost does not match the provided solution's cost")

unittest.main(argv=[''], exit=False)