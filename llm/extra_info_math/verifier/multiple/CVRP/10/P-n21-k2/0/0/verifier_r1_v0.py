import unittest
import math

class TestCVRPSolution(unittest.TestCase):
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    demands = [
        0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
    ]
    robot_capacities = [160, 160]
    tours = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
    ]
    travel_costs = [187.81, 287.43]
    overall_cost = 475.24  # Provided overall cost for verification

    def test_routes_start_and_end_at_depot(self):
        for tour in self.tours:
            with self.subTest(tour=tour):
                self.assertEqual(tour[0], 0)
                self.assertEqual(tour[-1], 0)

    def test_each_city_visited_exactly_once(self):
        visited = sum((tour[1:-1] for tour in self.tours), [])
        self.assertEqual(sorted(visited), list(range(1, 21)))

    def test_demand_within_capacity_limits(self):
        for tour, capacity in zip(self.tours, self.robot_capacities):
            total_demand = sum(self.demands[city] for city in tour[1:-1])
            with self.subTest(tour=tour):
                self.assertLessEqual(total_demand, capacity)

    def test_travel_cost_calculation(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        for tour, expected_cost in zip(self.tours, self.travel_costs):
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            with self.subTest(tour=tour):
                self.assertAlmostEqual(cost, expected_cost, places=2)

    def test_total_travel_cost(self):
        total = sum(self.travel_costs)
        self.assertAlmostEqual(total, self.overall_cost, places=2)

    def test_correct_solution(self):
        all_tests = [
            (self.test_routes_start_and_end_at_depot, "Start/End at Depot"),
            (self.test_each_city_visited_exactly_once, "Unique Visit"),
            (self.test_demand_within_capacity_limits, "Capacity Check"),
            (self.test_travel_cost_calculation, "Travel Cost"),
            (self.test_total_travel_cost, "Overall Cost")
        ]

        for test_func, desc in all_tests:
            with self.subTest(description=desc):
                test_func()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for method_name in dir(TestCVRPSolution):
        if method_name.startswith('test_'):
            suite.addTest(TestCVRPSolution(method_name))

    result = unittest.TextTestRunner().run(suite)
    # Check if all tests passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")