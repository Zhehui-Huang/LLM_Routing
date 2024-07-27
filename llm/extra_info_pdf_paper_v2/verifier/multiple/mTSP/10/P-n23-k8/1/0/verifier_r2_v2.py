import unittest
import math

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

class MTSPValidator(unittest.TestCase):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }

    robot_tours = [
        [0, 16, 21, 0],
        [0, 16, 21, 0],
        [0, 21, 2, 0],
        [0, 16, 21, 0],
        [0, 21, 20, 0],
        [0, 21, 20, 0],
        [0, 16, 20, 0],
        [0, 16, 21, 0]
    ]

    def test_all_cities_visited_exactly_once(self):
        city_visits = {i: 0 for i in range(1, 23)}
        # Count each city visit except the depot city (0)
        for tour in self.robot_tours:
            for city in tour:
                if city != 0:
                    city_visits[city] += 1
        # Check if each city is visited exactly once
        for city in range(1, 23):
            self.assertEqual(city_visits[city], 1, f"City {city} visit count should be exactly 1.")

    def test_tour_starts_and_ends_at_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_correct_travel_cost(self):
        total_cost_calculated = 0
        for tour in self.robot_tours:
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += calculate_euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            total_cost_calculated += tour_cost
        expected_total_cost = 230.95304336701662
        self.assertAlmostEqual(total_cost_calculated, expected_total_cost, places=5)

if __name__ == '__main__':
    unittest.main()