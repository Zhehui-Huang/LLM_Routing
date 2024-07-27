import unittest
from math import sqrt

# Nested dictionary for city coordinates.
cities = {
    0: (53, 68), 
    1: (75, 11), 
    2: (91, 95), 
    3: (22, 80), 
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups containing city indices.
groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Tour given in the solution.
tour = [0, 5, 2, 9, 8, 0]
proposed_cost = 183.99

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        """Tour should start and end at the depot city."""
        self.assertEqual(tour[0], 0, "Tour does not start at depot")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot")

    def test_visit_one_city_from_each_group(self):
        """Ensure exactly one city from each group is visited."""
        visited = set(tour[1:-1])  # exclude the depot city in the beginning and end
        for group in groups:
            self.assertEqual(len(set(group).intersection(visited)), 1,
                            f"More than one or no cities visited from group {group}")

    def test_travel_cost_calculation(self):
        """Verify total travel cost calculation."""
        total_distance = sum(calculate_address(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(total_distance, proposed_cost, places=2, msg="Incorrect cost calculation")

unittest.main()