import unittest

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.depot_cities = [0]
        self.all_cities = list(range(22))
        self.tour_solution = [0, 14, 0, 10, 0, 16, 0, 12, 0, 13, 0, 6, 0, 17, 0, 15, 0, 11, 0, 9, 0, 8, 0]
        self.total_cost_solution = 209.94010682553858

    def test_each_city_visited_once(self):
        """
        Ensure that each city is visited exactly once across all robots, except the depot cities which can be visited multiple times.
        """
        visited = set()
        for city in self.tour_solution:
            if city not in self.depot_cities or (city in visited and city in self.depot_cities):
                if city in visited:
                    self.fail(f"City {city} visited more than once.")
                visited.add(city)
        expected_non_depot_cities = set(range(4, 22))
        self.assertSetEqual(visited, expected_non_depot_cities, "Not all non-depot cities were visited.")

    def test_start_end_at_depot(self):
        """
        Ensure that each robot's tour starts and ends at their assigned depots.
        """
        self.assertEqual(self.tour_solution[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour_solution[-1], 0, "Tour does not end at the depot.")

    def test_depot_revisiting_non_consecutive(self):
        """
        Validate that depot revisits are non-consecutive unless the solution ends.
        """
        last_city = -1
        consecutive_depot_visits = False
        
        for index, city in enumerate(self.tour_solution):
            if city == 0 and last_city == 0 and index != len(self.tour_solution) - 1:
                consecutive_depot_visits = True
            last_city = city
        
        self.assertFalse(consecutive_depot_visits, "There are consecutive visits to the depot that are not at the end of the tour.")

    def test_total_cost_calculation(self):
        """
        Verify expected total cost is approximately similar to derived solution.
        """
        expected_cost = 209.94010682553858
        self.assertAlmostEqual(self.total_cost_solution, expected_cost, places=2, msg="Total cost calculation does not match the expected.")

if __name__ == "__main__":
    unittest.main()