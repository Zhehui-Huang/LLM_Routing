import unittest
import math

# Define a function to calculate the Euclidean distance between two cities based on coordinates
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Class containing the unit tests
class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities
        self.cities = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
            5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50),
            9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1),
            13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
            17: (52, 54), 18: (64, 72), 19: (14, 89)
        }
        self.tour = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 17, 18, 19, 0]
        self.total_cost = 615.2159197778357
    
    def test_tour_start_end_at_depot(self):
        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_visit_16_cities_including_depot(self):
        # Check if exactly 16 unique cities are visited
        self.assertEqual(len(set(self.tour)), 16)
    
    def test_correct_distance_calculation(self):
        # Verify the calculation of the tour distance
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            calculated_cost += distance(self.cities[self.tour[i - 1]], self.cities[self.tour[i]])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)
    
    def test_output_format(self):
        # Ensure the output format is a list of city indices followed by the total travel cost
        self.assertIsInstance(self.tour, list)
        for city in self.ther:
            self.assertIsInstance(city, int)
        self.assertIsInstance(self.total_cost, float)

# Main function to run the tests
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)