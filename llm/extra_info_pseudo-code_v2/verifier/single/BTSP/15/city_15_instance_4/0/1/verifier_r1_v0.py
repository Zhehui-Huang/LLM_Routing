import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Provided solution
        self.solution = {
            "Tour": [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0],
            "Total travel cost": 337.8447016788252,
            "Maximum distance between consecutive cities": 60.67124524847005
        }
        
        # City coordinates indexed by city number
        self.coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1
        tour = self.solution["Tour"]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visit_each_city_once(self):
        # Requirement 2
        tour_without_depot_ends = self.solution["Tour"][1:-1]
        self.assertEqual(len(set(tour_without_depot_ends)), 14)
        self.assertEqual(set(tour_without_depot_ends), set(range(1, 15)))

    def test_total_travel_cost_calculation(self):
        # Requirements 3 and 6
        tour = self.solution["Tour"]
        total_cost_calculated = sum(
            self.euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) 
            for i in range(len(tour) - 1)
        )
        self.assertAlmostEqual(total_cost_calculated, self.solution["Total travel cost"], places=5)

    def test_max_distance_between_consecutive_cities(self):
        # Requirement 7
        tour = self.solution["Tour"]
        max_distance = max(
            self.euclidean_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]]) 
            for i in range(len(tour) - 1)
        )
        self.assertAlmostEqual(max_distance, self.solution["Maximum distance between consecutive cities"], places=5)

# Run the test
if __name__ == '__main__':
    unittest.main()