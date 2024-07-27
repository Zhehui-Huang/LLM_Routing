import unittest
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
            5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
            10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        self.groups = {
            0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10],
            3: [4, 11], 4: [2, 8], 5: [3, 9]
        }
        self.expected_tour = [0, 6, 14, 1, 4, 10, 8, 9, 5, 0]
        self.expected_cost = 196.77

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.expected_tour[0], 0)
        self.assertEqual(self.expected_tour[-1], 0)

    def test_visits_one_city_per_group(self):
        visited_groups = {}
        for city in self.expected_tour[1:-1]:  # Exclude depot start and end
            for group_id, group_cities in self.groups.items():
                if city in group_cities:
                    visited_groups[group_id] = visited_groups.get(group_id, 0) + 1
                    break
        self.assertEqual(len(visited_groups), 6)
        self.assertTrue(all(count == 1 for count in visited_groups.values()))

    def test_all_cities_from_different_groups(self):
        visited = []
        for city in self.expected_tour[1:-1]: # Exclude depot start and end
            for group_id, cities in self.groups.items():
                if city in cities:
                    visited.append(group_id)
        self.assertEqual(len(visited), len(set(visited)))

    def test_travel_cost_calculation(self):
        calculated_cost = 0
        for i in range(len(self.expected_tour) - 1):
            current_city = self.expected_tour[i]
            next_city = self.expected_tour[i + 1]
            calculated_cost += calculate_distance(self.cities[current_city], self.cities[next_city])
        self.assertAlmostEqual(calculated_diff, self.expected_diff, places=2)

    def test_output_format(self):
        # Checking that the tour is in list format and ends and starts at depot
        self.assertIsInstance(self.expected_tour, list)
        self.assertEqual(self.expected_tour[0], 0)
        self.assertEqual(self.expected_tour[-1], 0)

        # Checking that the total cost is a numerical value
        self.assertIsInstance(self.expected_cost, (int, float))

def test_solution():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

test_output = test_solution()
print(test_output)