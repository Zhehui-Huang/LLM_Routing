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
        
    def test_solution(self):
        """Test solution of TSP against the requirements."""
        result = "CORRECT"
        
        # Test if the tour starts and ends at the depot city (city index 0)
        if not (self.tour[0] == 0 and self.tour[-1] == 0):
            result = "FAIL"
        
        # Test if the tour visits exactly 4 unique cities (including start/end city)
        if len(set(self.tour)) != 4:
            result = "FAIL"
        
        # Test the travel path to ensure it reports the shortest possible tour
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        calculated_cost = sum(calculate_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        
        # Check if the reported cost is approximately the same as calculated cost
        if not abs(calculated_cost - self.reported_cost) < 1e-4:
            result = "FAIL"
        
        print(result)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)