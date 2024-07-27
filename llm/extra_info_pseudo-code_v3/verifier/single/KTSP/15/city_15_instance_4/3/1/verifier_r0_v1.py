import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of each city
        self.city_coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        # Provided Tour solution
        self.tour = [0, 1, 5, 9, 2, 7, 12, 11, 6, 3, 14, 8, 0]
        # Provided total travel cost
        self.reported_cost = 240.9523727089619

    def test_tour_starts_and_ends_at_depot(self):
        """Test that the tour starts and ends at the depot city."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_exactly_12_cities(self):
        """Ensure exactly 12 unique cities are visited including the depot."""
        self.assertEqual(len(set(self.tour)), 12)

    def test_total_travel_cost_calculation(self):
        """Verify the total travel cost matches the reported cost with a small margin of error."""
        def euclidean_distance(c1, c2):
            x1, y1 = self.city_coordinates[c1]
            x2, y2 = self.city_coordinates[c2]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        total_distance = sum(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        
        self.assertAlmostEqual(total_distance, self.reported_cost, places=5)

    def test_tour_contains_depot(self):
        """Check that the tour starts and ends at the depot."""
        self.assertTrue(self.tour[0] == self.tour[-1] == 0)

    def test_output_format(self):
        """Check the output format of the tour and cost."""
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)

if __name__ == '__main__':
    unittest.main()