import unittest
from math import sqrt

# The provided data
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}
groups = {
    0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10], 3: [4, 11], 4: [2, 8], 5: [3, 9]
}

# The solution given
tour = [0, 14, 5, 10, 11, 8, 9, 0]
calculated_cost = 166.75801920718544

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verify the tour and cost
class TestTourSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visits_one_city_per_group(self):
        visited = {}
        for city in tour[1:-1]:  # Exclude the depot city
            for group_id, cities in groups.items():
                if city in cities:
                    visited[group_id] = visited.get(group_id, 0) + 1
                    break
        # Check if exactly one city is visited from each group
        self.assertTrue(all(count == 1 for count in visited.values()) and len(visited) == len(groups))

    def test_verify_correct_number_of_cities(self):
        self.assertEqual(len(coordinates), 15)

    def test_verify_city_ids(self):
        expected_ids = set(range(15))
        actual_ids = set(coordinates.keys())
        self.assertEqual(expected_ids, actual_ids)

    def test_travel_cost(self):
        actual_cost = 0
        for i in range(len(tour) - 1):
            actual_cost += calculate_distance(tour[i], tour[i + 1])
        self.assertAlmostEqual(actual_cost, calculated_cost, places=4)

    def test_solution(self):
        if (
            self.test_tour_start_end_at_depot() and
            self.test_visits_one_city_per_group() and
            self.test_verify_correct_number_of_cities() and
            self.test_verify_city_ids() and
            self.test_travel_cost()
        ):
            print("CORRECT")
        else:
            print("FAIL")

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)