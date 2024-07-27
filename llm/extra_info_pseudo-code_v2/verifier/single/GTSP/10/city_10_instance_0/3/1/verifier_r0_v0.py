import math
import unittest

# Coordinates for the cities indexed from 0 to 9
cities_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# City groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_estimate_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTourSolution(unittest.TestCase):
    def test_tour_requirements(self):
        # Provided solution details
        tour = [0, 6, 7, 5, 0]
        total_cost_given = 74.94753083872993
        
        # Check the tour starts and ends at the depot (city 0)
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check each city group is represented exactly once
        visited_groups = [set(group) & set(tour) for group in city_groups]
        all_groups_visited = all(len(group) == 1 for group in visited_groups)
        self.assertTrue(all_groups_visited)
        
        # Calculate the total travel cost from the tour
        calculated_total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check if total travel cost is correct (allowing for minor floating point variations)
        self.assertAlmostEqual(calculated_total_cost, total_cost_given, places=5)
        
        # Check the output format
        self.assertIsInstance(tour, list)
        # Each element in the tour list should be an integer representing the city
        self.assertTrue(all(isinstance(x, int) for x in tour))

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)