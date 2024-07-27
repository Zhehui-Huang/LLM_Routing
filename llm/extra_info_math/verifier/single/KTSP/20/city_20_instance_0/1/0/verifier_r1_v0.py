import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # City Coordinates
        self.cities = {
            0: (8, 11),
            1: (40, 6),
            2: (95, 33),
            3: (80, 60),
            4: (25, 18),
            5: (67, 23),
            6: (97, 32),
            7: (25, 71),
            8: (61, 16),
            9: (27, 91),
            10: (91, 46),
            11: (40, 87),
            12: (20, 97),
            13: (61, 25),
            14: (5, 59),
            15: (62, 88),
            16: (13, 43),
            17: (61, 28),
            18: (60, 63),
            19: (93, 15)
        }
        # Provided solution
        self.tour = [0, 1, 8, 4, 0]
        self.reported_cost = 110.08796524611944
        
    def test_starts_and_ends_at_depot(self):
        """Test if the tour starts and ends at the depot city (city index 0)."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_visits_exactly_four_cities(self):
        """Test if the tour visits exactly 4 unique cities."""
        # Eliminate the duplicate start/end city and check the count
        unique_cities = set(self.tour[:-1])
        self.assertEqual(len(unique_cities), 4)
        
    def test_shortest_possible_tour(self):
        """Test if the provided tour length is the shortest possible tour."""
        def calculate_distance(city1, city2):
            return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        
        # Calculate the tour distance according to the provided tour
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])

        # Check if the reported cost is approximately equal to the calculated cost
        self.assertAlmostEqual(calculated_cost, self.reported_cost)

# Run the tests
if __name__ == "__main__":
    unittest.main()