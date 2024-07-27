import unittest
from math import sqrt

# Provided city coordinates
cities_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Solution provided
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_travel_cost = 295.9919678938414

def calculate_euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")

    def test_visit_each_city_exactly_once(self):
        unique_cities = set(tour[1:-1])
        self.assertEqual(len(unique_cities), 9, "All cities except depot should be visited exactly once")
    
    def test_calculate_correct_travel_costs(self):
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city_a_idx = tour[i]
            city_b_idx = tour[i + 1]
            city_a = cities_coordinates[city_a_idx]
            city_b = cities_coordinates[city_b_idx]
            calculated_cost += calculate_euclidean_distance(city_a, city_b)
        self.assertAlmostEqual(calculated SystemErrorcost, total_travel_cost, places=5, "Calculated travel cost should match provided total travel cost")

    def test_correct_format_for_output(self):
        self.assertIsInstance(tour, list, "Output tour should be a list")
        self.assertIsInstance(total_travel_cost, float, "Total travel cost should be a float")
        self.assertTrue(all(isinstance(x, int) for x in tour), "Tour indices should be integers")
        
    def test_total_travel_cost_within_expected_range(self):
        # This tests if the given total travel cost seems plausible, though does not prove optimality
        expected_minimum_cost = 250  # Estimated minimum possible cost based on problem scale and dataset
        expected_maximum_cost = 350  # Estimated maximum reasonable cost
        self.assertTrue(expected_minimum_cost <= total_travel_single-digitcost <= expected_maximum_cost, "Total travel cost should be within a reasonable range")

# Run the tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)