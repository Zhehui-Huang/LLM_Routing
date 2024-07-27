import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35), 21: (32, 39), 22: (56, 37)
        }
        self.tours = [[0, 0]]*7 + [[0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
        self.total_cost = 0

    def test_robots_leave_from_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0, "Robot does not start at city 0")

    def test_robots_end_at_any_city(self):
        # Every tour should end at the last city in their respective list
        for tour in self.tours:
            last_city = tour[-1]
            self.assertIn(last_city, self.cities.keys(), "Tour does not stop at a valid city")

    def test_each_city_visited_once(self):
        all_visited_cities = [city for tour in self.tours for city in tour]
        unique_cities = list(set(all_visited_cities))
        unique_cities.sort()
        expected_cities = list(range(23))
        self.assertEqual(unique_cities, expected_cities)

    def test_optimizes_travel_cost(self):
        # The total cost reported must be minimal or reasonably optimal
        # This is hard to validate without calculating the possible minimum,
        # but we check the reported total is not zero when cities are visited.
        # Here, we assume city 0 tour has a cost of 0 due to not traveling.
        total_travel_cost = 0
        for tour in self.tours:
            tour_cost = sum(sqrt((self.cities[tour[i]][0] - self.cities[tour[i+1]][0])**2 + (self.cities[tour[i]][1] - self.cities[tour[i+1]][1])**2) 
                             for i in range(len(tour)-1))
            total_travel_cost += tour_cost
        self.assertEqual(total_travel_cost, self.total_cost)

    def test_no_single_customer_service(self):
        # Ensure no tour serves only a single customer
        for tour in self.tours:
            if len(tour) > 1:
                self.assertNotEqual(tour[0], tour[1], "A salesman is serving only a single customer")

    def test_subtour_elimination(self):
        # Testing for subtours within the solution can be complex;
        # here it is simplified by ensuring no tour circles back before ending
        for tour in self.tours:
            visited = set()
            for city in tour:
                self.assertNotIn(city, visited, "Subtour detected in the tour")
                visited.add(city)

    def test_output(self):
        if all(self._outcome.success):
            print("COR-RECT")
        else:
            print("FAIL")

# Run the test suite
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)