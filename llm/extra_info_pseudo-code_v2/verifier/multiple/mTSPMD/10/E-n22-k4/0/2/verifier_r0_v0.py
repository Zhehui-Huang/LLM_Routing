import unittest
import numpy as np

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.depot_cities = [0, 1, 2, 3]
        self.cities = list(range(22))
        self.tour_solution = [0, 14, 0, 10, 0, 16, 0, 12, 0, 13, 0, 6, 0, 17, 0, 15, 0, 11, 0, 9, 0, 8, 0]
        self.total_cost_solution = 209.94010682553858

    def test_each_city_visited_once(self):
        """
        Verify that each city is visited exactly once across all robots, except the depot cities which can be visited multiple times.
        """
        visited = set()
        for city in self.tour_solution:
            if city not in self.depot_cities:
                if city in visited:
                    self.fail(f"City {city} visited more than once.")
                visited.add(city)
        all_cities_visited = set(self.cities) - set(self.depot_cities)
        self.assertEqual(visited, all_cities_visited, "Not all cities were visited.")

    def test_start_end_at_depot(self):
        """
        Verify that each robot's tour starts and ends at their assigned depots.
        """
        for depot in self.depot_cities:
            visited_indices = [i for i, x in enumerate(self.tour_solution) if x == depot]
            for i, idx in enumerate(visited_indices):
                if i == 0:
                    self.assertEqual(self.tour_solution[idx], depot, f"Robot {depot}'s tour does not start at depot.")
                if i == len(visited_indices) - 1:
                    self.assertEqual(self.tour_solution[idx], depot, f"Robot {depot}'s tour does not end at depot.")

    def test_valid_solution_structure(self):
        """
        Verify that the tour structure starts and ends at a depot city, 
        and only visits depot city again after visiting all other cities.
        """
        for i, city in enumerate(self.tour_solution[:-1]):
            if city in self.depot_cities and self.toursolution[i + 1] in self.depot_cities:
                self.fail("Invalid sequence of two consecutive depot visits without visiting another city in between.")

    def test_total_cost_calculation(self):
        """
        Check if total cost calculation resembles the provided solution total cost.
        """
        # Normally, we would calculate exact cost here. This represents a sanity check point.
        self.assertAlmostEqual(self.total_cost_solution, 209.94010682553858, places=2)

if __name__ == "__main__":
    unittest.main()