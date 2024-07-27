import unittest
import math

# Given data
city_positions = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]
proposed_tour = [0, 14, 5, 9, 8, 10, 4, 0]
proposed_cost = 138.22028342379204

def euclidean_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

class TestSolutionCorrectness(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)

    def test_visit_one_city_from_each_group(self):
        visited = set(proposed_tour[1:-1])  # ignoring start and end depot assertions
        successful_group_visit = all(len(visited.intersection(set(group))) == 1 for group in city_groups)
        self.assertTrue(successful_group_visit)

    def test_total_travel_cost(self):
        calculated_cost = calculate_total_travel_cost(proposed_tour)
        self.assertAlmostEqual(calculated_cost, proposed_cost, places=5)

# Running the tests
if __name__ == "__main__":
    unittest.main()