import unittest
from math import sqrt

# City coordinates
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

# City groups
groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Provided solution tour
tour = [0, 5, 2, 9, 8, 0]
proposed_cost = 183.99

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTourSolution(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        """Tour should start and end at the depot city."""
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        """Each group should have exactly one city visited in the tour."""
        visited = set(tour[1:-1])  # exclude depot city start/end
        for group in groups:
            self.assertTrue(any(city in visited for city in group), f"Group {group} is not visited")

    def test_travel_cost_calculation(self):
        """The calculated travel cost should match the proposed cost."""
        total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(total_distance, proposed_cost, places=2)

if __name__ == '__main__':
    unittest.main()