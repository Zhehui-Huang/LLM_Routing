import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
        self.total_cost_provided = 279.02
        self.city_coords = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.city_groups = [
            [1, 4],
            [2, 6],
            [7],
            [5],
            [9],
            [8],
            [3]
        ]

    def calculate_euclidean_distance(self, coord1, coord2):
        return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
        
    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "The tour does not end at the depot city.")
    
    def test_visit_each_group_once(self):
        # Check if each group has exactly one city visited
        visited = set(self.tour)
        for group in self.city_groups:
            self.assertTrue(any(city in visited for city in group), 
                            f"No city from group {group} is visited.")
            # Ensuring only one city per group is visited
            self.assertEqual(sum(city in visited for city in group), 1,
                             f"More than one city from group {group} is visited.")
    
    def test_travel_cost_calculation(self):
        computed_total_cost = sum(
            self.calculate_euclidean_distance(self.city_coords[self.tour[i]], self.city_coords[self.tour[i + 1]])
            for i in range(len(self.tour) - 1)
        )
        # Allowing a small margin for floating-point errors
        self.assertAlmostEqual(computed_total_cost, self.total_cost_provided, places=2,
                               msg=f"The provided total travel cost is incorrect. Calculated cost: {computed_total_cost}")

    def test_tour_output(self):
        expected_tour_start = [0]
        expected_tour_end = [0]
        self.assertEqual(self.tour[:1], expected_tour_start, "Tour does not start correctly")
        self.assertEqual(self.tour[-1:], expected_tour_end, "Tour does not end correctly")
    
if __name__ == '__main__':
    unittest.main()