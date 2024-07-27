import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates for each of the 20 cities
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.tour = [0, 1, 3, 15, 5, 17, 16, 11, 10, 4, 7, 12, 18, 14, 8, 2, 13, 6, 19, 0]
        self.provided_cost = 492.29
    
    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def test_tour_validity_and_cost(self):
        # Check if tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Check if all cities are visited exactly once, except the depot city visited twice
        visited = set(self.tour)
        self.assertTrue(all(city in visited for city in self.cities))  # Check all cities are visited
        self.assertEqual(len(self.tour) - 1, len(self.cities))  # Check visits count (including repeat of depot city)
        
        # Calculate the travel cost of the tour
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            calculated_cost += self.calculate_distance(self.tour[i], self.tour[i + 1])
        
        # Check if the calculated tour cost matches the provided total cost
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=2)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)