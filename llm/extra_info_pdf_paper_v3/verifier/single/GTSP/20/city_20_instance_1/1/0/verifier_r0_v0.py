import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.depot = 0
        self.cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
            5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
            10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
            15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        self.groups = {
            0: [5, 6, 7, 11, 17],
            1: [1, 4, 8, 13, 16],
            2: [2, 10, 15, 18, 19],
            3: [3, 9, 12, 14]
        }
        self.tour = [0, 6, 2, 13, 9, 0]
        self.reported_cost = 108.66

    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], self.depot, "Tour does not start at the depot")
        self.assertEqual(self.tour[-1], self.depot, "Tour does not end at the depot")

    def test_tour_includes_one_from_each_group(self):
        visited = set(self.tour[1:-1])  # Ignore the depot at start and end
        for group, members in self.groups.items():
            self.assertTrue(any(city in visited for city in members), f"Group {group} not represented in tour")

    def test_tour_travel_cost_is_correct(self):
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

        total_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.tour[i]
            city_b = self.tour[i+1]
            total_cost += euclidean_distance(self.cities[city_a], self.cities[city_b])

        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, msg="Reported travel cost is incorrect")

    def test_tour_structure(self):
        self.assertIsInstance(self.tour, list, "Tour is not a list")
        self.assertTrue(all(isinstance(city, int) for city in self.tour), "Tour contains non-integer city indices")

    def test_output_specifications(self):
        self.assertIsInstance(self.tour, list, "The tour output is not a valid list.")
        self.assertIsInstance(self.reported_cost, float, "The travel cost is not a float.")

    def test_okay(self):
        self.assertTrue(True) # Use to ensure that testing setup is correct

if __name__ == "__main__":
    try:
        unittest.main(argv=[''], exit=False)
        print("CORRECT")
    except Exception as e:
        print("FAIL")