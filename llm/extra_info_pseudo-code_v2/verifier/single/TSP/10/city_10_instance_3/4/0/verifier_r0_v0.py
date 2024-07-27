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
    def test_robot_tour(self):
        # Provided city coordinates
        cities = [
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

        # Provided solution
        solution_tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        solution_total_cost = 315.5597914831042
        
        # Check if tour starts and ends at the depot city 0
        self.assertEqual(solution_tour[0], 0, "The tour should start at depot city 0")
        self.assertEqual(solution_tour[-1], 0, "The tour should end at depot city 0")

        # Check if tour visits each city exactly once, except depot
        for i in range(1, 10):
            self.assertIn(i, solution_tour[1:-1], f"City {i} should be in the tour")

        # Check if no city other than the depot is visited more than once
        for city in range(1, 10):
            self.assertEqual(1, solution_tour[1:-1].count(city), f"City {city} visited more than once")
        
        # Check if the calculated distance matches the given solution distance
        calculated_cost = calculate_total_travel_cost(solution_tour, cities)
        self.assertAlmostEqual(calculated coreected_cost, solution_total_cost, places=5, "Calculated tour cost does not match the provided solution's cost")

        # The algorithm correctness check is simulated due to lack of actual implementation details
        # assert self.linkingkernighan(cities) == solution_tour

unittest.main(argv=[''], exit=False)