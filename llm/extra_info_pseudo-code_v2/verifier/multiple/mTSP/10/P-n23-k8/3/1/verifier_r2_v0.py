import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
            5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
            10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
            15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35), 21: (32, 39), 22: (56, 37)
        }
        self.robot_tours = [
            ([0, 1, 9, 17, 0], 81.65415032740114),
            ([0, 10, 18, 2, 0], 81.81803428067735),
            ([0, 3, 19, 11, 0], 108.81482905718964),
            ([0, 20, 12, 4, 0], 82.89654293014993),
            ([0, 21, 5, 13, 0], 68.39261497384648),
            ([0, 6, 22, 14, 0], 67.67055146540517),
            ([0, 7, 15, 0], 83.62034367443502),
            ([0, 16, 8, 0], 64.92216653342012)
        ]

    def test_tour_start_end_at_depot(self):
        for tour, _ in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_visitation_uniqueness(self):
        all_visited_cities = [city for tour, _ in self.robot_tours for city in tour[1:-1]]
        unique_visited_cities = set(all_visited_cities)
        self.assertEqual(len(all_visited_cities), len(unique_visited_cities))
        self.assertEqual(len(unique_visited_cities), 22)  # Since there are 22 cities excluding the depot
    
    def test_correctness_of_travel_costs(self):
        for tour, reported_cost in self.robot_tours:
            computed_cost = sum(sqrt((self.cities[tour[i]][0] - self.cities[tour[i+1]][0])**2 +
                                      (self.cities[tour[i]][1] - self.cities[tour[i+1]][1])**2)
                                for i in range(len(tour) - 1))
            self.assertAlmostEqual(computed_cost, reported_cost, places=5)
    
    def test_total_travel_cost(self):
        reported_total_cost = 639.7892332425249
        computed_total_cost = sum(cost for _, cost in self.robot_tours)
        self.assertAlmostEqual(computed_total_cost, reported_total_cost, places=5)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestRobotTours))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")