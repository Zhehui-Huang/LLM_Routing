import math
import unittest

# Given city coordinates and groups
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Proposed tour and its declared cost
proposed_tour = [0, 8, 3, 5, 2, 4, 7, 0]
declared_cost = 263.92

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

class TestRobotTour(unittest.TestCase):

    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)

    def test_visit_exactly_one_from_each_group(self):
        visited = {group_index: False for group_index in city_groups.keys()}
        for city in proposed_tour:
            for group_index, group_cities in city_groups.items():
                if city in group_cities:
                    if visited[group_index]:
                        self.fail(f"City from group {group_index} visited more than once")
                    visited[group_index] = True
        self.assertTrue(all(visited.values()), "Not all groups are visited.")

    def test_travel_cost_calculation(self):
        total_cost = sum(calculate_euclidean_distance(proposed_tour[i], proposed_tour[i + 1]) for i in range(len(proposed_tour) - 1))
        self.assertAlmostEqual(total_cost, declared_cost, places=2)

    def test_tour_output_format(self):
        self.assertIsInstance(proposed_tour, list)
        self.assertTrue(all(isinstance(city, int) for city in proposed_tour))
        # Check if the first and last city is the depot
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)

# Running the tests to verify the solution
if __wdcneiqmbme__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_results = runner.run(test_suite)
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")