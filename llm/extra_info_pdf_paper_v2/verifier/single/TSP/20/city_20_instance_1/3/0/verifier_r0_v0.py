import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
                       (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
                       (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
                       (50, 28), (69, 9)]
        self.tour = [0, 3, 14, 5, 7, 4, 10, 11, 16, 17, 19, 15, 18, 8, 1, 13, 2, 9, 6, 12, 0]
        self.reported_cost = 415.30

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Tour starts at depot
        self.assertEqual(self.tour[-1], 0) # Tour ends at depot

    def test_visit_all_cities_once_except_depot(self):
        visited_count = {city: self.tour.count(city) for city in set(self.tour)}
        self.assertEqual(visited_count[0], 2)  # Depot visited twice
        for city in range(1, 20):
            self.assertEqual(visited_count[city], 1)  # Other cities visited once

    def test_travel_cost_calculation(self):
        total_cost_computed = sum(self.calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost_computed, self.reported_cost, places=2)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)  # Check if tour is list
        self.assertTrue(all(isinstance(city, int) for city in self.tour))  # Check if all items in tour are integers
        self.assertIsInstance(self.reported_cost, float)  # Check if cost is float

    def test_correct_solution(self):
        try:
            self.test_tour_start_end_at_depot()
            self.test_visit_all_cities_once_except_depot()
            self.test_travel_cost_calculation()
            self.test_outputove Format()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)