import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for the cities
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
        # The provided solution tour and its total cost
        self.tour = [0, 14, 16, 4, 0]
        self.reported_cost = 112.10
    
    def test_tour_length(self):
        # Test if the tour length is exactly 5 (includes 4 cities + depot city start and end)
        self.assertEqual(len(self.tour), 5)
    
    def test_start_end_depot(self):
        # Test if the tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_travel_cost(self):
        # Test if the total travel cost matches the reported value
        def euclidean_distance(city1, city2):
            return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        # Calculate actual travel cost
        actual_cost = 0
        for i in range(len(self.tour) - 1):
            actual_cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        
        self.assertAlmostEqual(actual_cost, self.reported_cost, places=2)
    
    def test_unique_cities(self):
        # Test if exactly 4 unique cities (including depot) are visited
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 4)

# Run the test cases
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")