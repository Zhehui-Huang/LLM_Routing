import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (79, 15),  # Depot
            (79, 55),
            (4, 80),
            (65, 26),
            (92, 9),
            (83, 61),
            (22, 21),
            (97, 70),
            (20, 99),
            (66, 62)
        ]
        self.tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        self.total_cost = 408.41  # Approximated
        self.max_distance = 61.68  # Approximated
        
    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_unique_visit(self):
        self.assertEqual(len(set(self.tour)), len(self.coordinates))  # +1 for return to start
        
    def test_total_travel_cost(self):
        calculated_cost = sum(self.euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)
    
    def test_max_distance_between_consecutive_cities(self):
        max_dist = max(self.euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(max_dist, self.max_distance, places=2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)