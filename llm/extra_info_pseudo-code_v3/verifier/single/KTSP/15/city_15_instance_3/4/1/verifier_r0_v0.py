import unittest
from math import sqrt

# Given city coordinates indexed by their numbers
city_coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def calculate_distance(c1, c2):
    """Calculates Euclidean distance between two cities given their coordinates."""
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # Given solution
        tour = [0, 1, 4, 12, 3, 10, 8, 9, 5, 14, 0]
        reported_cost = 194.26
        
        # Check if the tour starts and ends at the depot
        self.assertEqual(tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot.")
        
        # Check if exactly 10 cities are visited including the depot
        self.assertEqual(len(tour), 11, "Tour does not visit exactly 10 cities.")
        
        # Calculate the actual travel cost in the tour
        actual_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coords[tour[i + 1]]) for i in range(len(tour) - 1))
        
        # Check if travel cost is accurately calculated
        self.assertAlmostEqual(actual_cost, reported_cost, places=2, msg="Reported cost does not match calculated cost.")
        
        # Check if all cities except the depot are visited exactly once
        unique_cities = set(tour)
        self.assertEqual(len(unique_cities), 10, "Not exactly 10 distinct cities visited.")
        
        # Check for any city index out of bounds
        max_city_index = max(city_coordinates.keys())
        for city in tour:
            self.assertTrue(0 <= city <= max_city_index, f"City index {city} out of bounds.")
        
        # Verify that the tour visits only the assigned cities
        expected_cities = {0, 1, 4, 12, 3, 10, 8, 9, 5, 14}
        visited_cities = set(tour) - {0}
        self.assertSetEqual(expected_cities, visited_cities, "Tour visits incorrect cities.")

# Run tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
unittest.TextTestRunner().run(suite)