import unittest
import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
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

    expected_costs = [
        21.455612434792677, 
        21.455612434792677,
        42.98294694244445, 
        21.455612434792677, 
        31.64892678707713, 
        31.64892678707713, 
        38.849793111247195,
        21.455612434792677
    ]

    def test_unique_city_visitation(self):
        # Determine all cities visited excluding the depot (city 0).
        visited_cities = sum((tour[1:-1] for tour in self.robot_tours), [])
        visited_cities_set = set(visited_cities)
        # Check if every city except the depot has been visited at least once.
        self.assertSetEqual(visited_cities_set, set(range(1, 23)))
        # Check if visitation count for each city is exactly once.
        self.assertTrue(all(visited_cities.count(city) == 1 for city in range(1, 23)))

    def test_tour_start_end_depot(self):
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_correct_travel_costs(self):
        for i, tour in enumerate(self.robot_tours):
            total_cost = sum(calculate_euclidean_distance(self.cities[tour[j]], self.cities[tour[j + 1]]) 
                             for j in range(len(tour) - 1))
            self.assertAlmostEqual(total_cost, self.expected_costs[i])

    def test_total_sum_of_costs(self):
        total_cost = sum(self.expected_costs)
        self.assertAlmostEqual(total_cost, 230.95304336701662)

if __name__ == "__main__":
    unittest.main()