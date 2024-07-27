import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coords = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
            (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
            (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.groups = [
            [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
            [2, 4, 14], [10, 17], [7, 15]
        ]
        self.solution_tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]
        self.reported_cost = 266.72

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_tour_visits_one_city_from_each_group(self):
        visited = set(self.solution_tour[1:-1])
        for group in self.groups:
            self.assertEqual(len(visited.intersection(group)), 1)

    def test_tour_validity(self):
        # Check all cities in the tour are valid
        all_cities = set(range(len(self.coords)))
        self.assertTrue(set(self.solution_tour).issubset(all_cities))

    def test_travel_cost(self):
        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            x1, y1 = self.coords[self.solution_tour[i]]
            x2, y2 = self.coords[self.solution_tour[i + 1]]
            total_cost += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_output_format(self):
        # Tour format check: list of integers
        self.assertIsInstance(self.solution_tour, list)
        self.all(isinstance(city, int) for city in self.solution_tour)
        # Total travel cost format: float or int
        self.assertIsInstance(self.reported_cost, (float, int))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")