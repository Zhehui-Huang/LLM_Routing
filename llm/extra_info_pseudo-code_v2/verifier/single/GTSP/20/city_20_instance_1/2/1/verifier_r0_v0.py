import unittest
from math import sqrt

class TestSolutionCorrectness(unittest.TestCase):
    def setUp(self):
        # Provided city coordinates indexed by their stated indices
        self.cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
            5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
            10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
            15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }

        # Groups definition
        self.groups = {
            0: [5, 6, 7, 11, 17],
            1: [1, 4, 8, 13, 16],
            2: [2, 10, 15, 18, 19],
            3: [3, 9, 12, 14]
        }
        
        # Provided results
        self.output_tour = [0, 17, 1, 18, 9, 0]
        self.output_cost = 186.00039018840883

    def test_tour_ends_start_at_depot(self):
        self.assertEqual(self.output_tour[0], 0)
        self.assertEqual(self.output_tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        visited_groups = {group_id: False for group_id in self.groups.keys()}
        for city in self.output_tour[1:-1]:  # Exclude the depot, starting at index 1
            for group_id, cities in self.groups.items():
                if city in cities:
                    visited_groups[group_id] = True
        self.assertTrue(all(visited_groups.values()))

    def test_calculate_travel_cost(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.output_tour) - 1):
            calculated_cost += euclidean_distance(self.output_tour[i], self.output_tour[i + 1])
        self.assertAlmostEqual(calculated_cost, self.output_cost, places=5)

    def test_solution_correctness(self):
        self.test_tour_ends_start_at_depot()
        self.test_visit_one_city_from_each_circle()
        self.test_calculate_travel_cost()
        print("CORRECT")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)