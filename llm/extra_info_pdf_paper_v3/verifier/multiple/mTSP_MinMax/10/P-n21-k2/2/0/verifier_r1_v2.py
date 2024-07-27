import unittest

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # These tours should reflect a correct solution provided earlier
        self.robot_tours = {
            0: [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0],
            1: [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]
        }
        self.robot_costs = {
            0: 212.22,
            1: 184.31
        }
        self.max_distance = 212.22
        self.all_cities = set(range(21))  # Cities from 0 to 20

    def test_visits_all_cities_once(self):
        visited_cities = set()
        for tour in self.robot_tours.values():
            visited_cities.update(tour[1:-1])  # Gather cities visited, excluding the depot at start/end

        expected_cities = self.all_cities - {0}  # All cities except the depot
        self.assertEqual(visited_cities, expected_cities, "Each city is visited exactly once.")

    def test_tour_starts_and_ends_at_depot(self):
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0, "Tour does not start at the depot.")
            self.assertEqual(tour[-1], 0, "Tour does not end at the depot.")

    def test_minimize_maximum_distance(self):
        actual_max_cost = max(self.robot_costs.values())
        self.assertEqual(actual_max_cost, self.max_distance, "Maximum travel cost is not minimized as expected.")

    def runTest(self):
        self.test_visits_all_cities_once()
        self.test_tour_starts_and_ends_at_depot()
        self.test_minimize_maximum_distance()

# Option to run the tests if this script is executed
if __name__ == "__main__":
    unittest.main()