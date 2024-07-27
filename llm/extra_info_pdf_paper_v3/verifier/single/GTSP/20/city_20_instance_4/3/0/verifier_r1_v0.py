import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
            (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
            (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
            (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        
        # Groups of cities
        self.groups = [
            [5, 6, 16], [8, 18, 19], [11, 12, 13],
            [1, 3, 9],   [2, 4, 14],  [10, 17],  [7, 15]
        ]
        
        # Given solution
        self.tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        self.total_cost_reported = 266.72

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_visit_one_city_per_group(self):
        visited = []
        for i in self.tour:
            for g_id, group in enumerate(self.groups):
                if i in group:
                    visited.append(g_id)
                    break
        self.assertEqual(len(set(visited)), len(self.groups), "Not exactly one city from each group is visited")

    def test_travel_cost_calculation(self):
        def euclidean_distance(pt1, pt2):
            return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

        total_cost_computed = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) 
                                  for i in range(len(self.tour) - 1))
        
        # Check if the reported total cost is approximately equal to the computed cost
        self.assertAlmostEqual(total_cost_computed, self.total_cost_reported, places=2, 
                               msg="Reported travel cost does not match computed cost")

    def test_verify_tour_completeness(self):
        all_cities_covered = set(sum(self.groups, []))
        tour_cities = set(self.tour)
        self.assertTrue(all_cities_covered.issubset(tour_cities), "Not all cities are covered in the tour")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)  # Adjusting default behavior for interactive environments