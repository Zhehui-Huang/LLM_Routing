import unittest
import math

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        # Set coordinates for cities
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
            6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
            12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        self.proposed_tour = [0, 6, 8, 11, 2, 3, 12, 10, 9, 14, 0]
        self.proposed_cost = 281.7117403388051
        
    def test_start_and_end_at_depot(self):
        # Check if the tour starts and ends at depot city 0
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_visit_exactly_ten_cities(self):
        # Check if exactly 10 cities are visited
        self.assertEqual(len(set(self.proposed_tour)), 10)

    def test_calculate_total_travel_cost(self):
        # function to calculate Euclidean distance
        def euclidean_distance(city1, city2):
            x1, y1 = city1
            x2, y2 = city2
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        
        # Calculate total travel cost from the proposed tour
        total_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            city1 = self.proposed_tour[i]
            city2 = self.proposed_tour[i + 1]
            total_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        
        # Check if calculated cost matches the proposed cost
        self.assertAlmostEqual(total_cost, self.proposed_cost, places=5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
    print("FAIL")