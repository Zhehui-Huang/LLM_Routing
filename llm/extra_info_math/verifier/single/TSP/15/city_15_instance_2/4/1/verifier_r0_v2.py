import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }
        self.tour = [0, 5, 3, 10, 11, 2, 12, 13, 9, 14, 4, 7, 1, 6, 8, 0]
        self.reported_cost = 646.58

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour does not start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "The tour does not end at the depott city.")

    def test_all_cities_visited_exactly_once(self):
        non_depot_cities = set(self.cities.keys()) - {0}
        tour_without_depot = [city for city in self.tour if city != 0]
        for city in non_depot_cities:
            self.assertEqual(tour_without_depot.count(city), 1, f"City {city} is not visited exactly once.")
        self.assertEqual(len(tour_without_depot), len(non_depot_cities), "Not all non-depot cities were visited exactly once.")

    def test_no_subtours(self):
        visited = set()
        for city in self.tour[:-1]:  # Exclude the last visit to the depot
            self.assertNotIn(city, visited, "Subtour detected.")
            visited.add(city)

    def test_total_travel_cost(self):
        calculated_cost = 0
        num_cities = len(self.tour)
        for i in range(num_cities - 1):
            city_i = self.tour[i]
            city_j = self.tour[i + 1]
            calculated_cost += euclidean_address(*self.cities[city_i], *self.cities[city_j])
        # Allow small rounding differences in reported cost
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg="Reported travel cost is incorrect.")

# Running tests
if __name__ == "__main__":
    unittest.main()