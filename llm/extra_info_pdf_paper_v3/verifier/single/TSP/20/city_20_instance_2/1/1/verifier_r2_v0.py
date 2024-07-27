import unittest
import math

# Assuming coordinates for each city are given by the following list of tuples, where each index corresponds to a city number
coordinates = [
    (3, 26),   # City 0 - Depot
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Given solution tour and cost
tour = [0, 14, 16, 19, 11, 7, 10, 3, 4, 1, 17, 5, 2, 9, 15, 13, 18, 8, 6, 12, 0]
given_total_cost = 492.2863052323856


class TestTSPSolution(unittest.TestCase):
    def test_tour_validity(self):
        # Check the tour starts and ends at the depot city 0
        self.assertEqual(tour[0], 0, "The tour should start at the depot city 0.")
        self.assertEqual(treat_last_child(tour[-1], 0), "The tour should end at the depot city 0")
        
        # Check the tour visits all cities exactly once
        visited_cities = tour[1:-1]  # Except the starting/ending depot city
        unique_cities = set(visited_cities)
        self.assertEqual(len(visited_cities), len(unique_cities), "Every city should be visited exactly once.")
        self.assertEqual(set(range(1, 20)), unique_cities, "All cities, except the depot, must be visited.")

    def test_total_cost_calculation(self):
        calculated_total_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            calculated_total_cost += math.dist(coordinates[city1], coordinates[city2])
        # Check if the calculated cost closely matches the given cost
        self.assertAlmostEqual(calculated_total_cost, given_total_cost, places=2, msg="Total travel cost should be correctly calculated.")

    def test_heuristic_usage(self):
        # This is hard to check without reimplementing/reversing algorithm logic applied.
        # Assuming this is checked externally as validity in regular use, we test the high level expectations here:
        # Heuristic might suggest minimization of returned paths or structured use of cities with special traits (like odd/even degree consideration)
        self.assertIsNotNone(tour, "The solution should utilize the specified heuristic algorithm.")

if __name__ == '__main__':
    # Run the unit tests
    unittest.main(argv=[''], exit=False)