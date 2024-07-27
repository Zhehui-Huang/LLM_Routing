import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40),
            1: (37, 52),
            2: (49, 49),
            3: (52, 64),
            4: (31, 62),
            5: (52, 33),
            6: (42, 41),
            7: (52, 41),
            8: (57, 58),
            9: (62, 42),
            10: (42, 57),
            11: (27, 68),
            12: (43, 67),
            13: (58, 48),
            14: (58, 27),
            15: (37, 69)
        }
        self.robot_tours = [
            [0, 1, 0],
            [0, 2, 0],
            [0, 3, 0],
            [0, 4, 0],
            [0, 5, 0],
            [0, 6, 0],
            [0, 7, 0],
            [0, 8, 9, 14, 13, 12, 11, 10, 15, 0]
        ]
        self.expected_costs = [27.78, 42.05, 65.12, 44.05, 46.17, 24.08, 44.05, 187.41]
        self.total_cost = 480.71
    
    def test_unique_city_visit(self):
        visited_cities = set()
        for tour in self.robot_tours:
            # Exclude the start and end depot city
            cities_in_tour = set(tour[1:-1])
            self.assertTrue(visited_cities.isdisjoint(cities_in_tour))
            visited_cities.update(cities_in_tour)
        self.assertEqual(len(visited_cities), 15)
    
    def test_correct_tour_and_cost_calculation(self):
        calc_total_cost = 0
        for robot_id, tour in enumerate(self.robot_tours):
            tour_cost = 0
            for i in range(len(tour) - 1):
                city1 = self.cities[tour[i]]
                city2 = self.cities[tour[i+1]]
                distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
                tour_cost += distance
            calc_total_cost += round(tour_cost, 2)
            self.assertAlmostEqual(self.expected_costs[robot_id], round(tour_cost, 2))
        self.assertAlmostEqual(self.total_cost, calc_total_cost)
    
    def test_tour_start_end_at_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_performance_optimization(self):
        # Assert that the result is better or equal to a hypothetical previous total
        # Here we assume a hypothetical previous result could have been 500
        self.assertTrue(self.total_endurance <= 500)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)