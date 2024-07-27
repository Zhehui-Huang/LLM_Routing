import unittest
from math import sqrt

# Given cities and groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

groups = {
    0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 
    3: [1, 3, 9], 4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestTour(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        self.assertEqual(tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot city.")

    def test_visit_one_from_each_group(self):
        tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        visited = set(tour[1:-1])  # Exclude depot city from visit check
        unique_groups_visited = set()
        for city in visited:
            for group_idx, group_cities in groups.items():
                if city in group_cities:
                    unique_groups_visited.add(group_idx)
        self.assertEqual(len(unique_groups_visited), len(groups), "Not all groups are visited by the robot.")

    def test_minimize_travel_distance(self):
        tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        given_cost = 266.71610174713
        computed_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(computed_cost, given_cost, delta=0.001, msg="Provided travel cost does not match computed cost.")

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)