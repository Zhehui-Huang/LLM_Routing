import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40),  # depot city 0
            (39, 41),  # city 1
            (81, 30),  # city 2
            (5, 50),   # city 3
            (72, 90),  # city 4
            (54, 46),  # city 5
            (8, 70),   # city 6
            (97, 62),  # city 7
            (14, 41),  # city 8
            (70, 44),  # city 9
            (27, 47),  # city 10
            (41, 74),  # city 11
            (53, 80),  # city 12
            (21, 21),  # city 13
            (12, 39)   # city 14
        ]
        self.tour = [0, 10, 8, 13, 14, 3, 6, 11, 12, 4, 7, 9, 2, 5, 1, 0]
        self.reported_total_cost = 306.76

    def test_all_cities_visited_exactly_once(self):
        visited_each_city_once = len(self.tour) - 1 == len(self.cities) and len(set(self.tour[1:-1])) == len(self.cities)-1
        self.assertTrue(visited_each_city_once)

    def test_tour_starts_and_ends_at_depot(self):
        starts_at_depot = self.tour[0] == 0
        ends_at_depot = self.tour[-1] == 0
        self.assertTrue(starts_at_depot and ends_at_depot)

    def test_total_cost_calculated_correctly(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i + 1]]
            distance = math.sqrt((city_b[0] - city_a[0]) ** 2 + (city_b[1] - city_a[1]) ** 2)
            total_distance += distance
        self.assertAlmostEqual(total_distance, self.reported_total_cost, places=2)

    def runTest(self):
        try:
            self.test_all_cities_visited_exactly_once()
            self.test_tour_starts_and_ends_at_depot()
            self.test_total_cost_calculated_correctly()
            print("CORRECT")
        except AssertionError as e:
            print("FAIL")

# Create and run the test case
case = TestTravelingSalesmanSolution()
case.runTest()