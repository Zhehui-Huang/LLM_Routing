import math
import unittest

class MockSolution:
    num_cities = 21
    demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
    robots = 2
    capacity = 160
    tours = {
        0: [0, 1, 2, 0],
        1: [0, 3, 4, 0]
    }
    tour_costs = {
        0: 50,
        1: 60
    }
    overall_cost = 110
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    
    @staticmethod
    def used_clarke_wright():
        return True

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestVRPSolution(unittest.TestCase):
    def test_total_number_of_cities(self):
        self.assertEqual(MockSolution.num_cities, 21)

    def test_city_coordinates(self):
        self.assertEqual(len(MockSolution.cities_coordinates), 21)
        self.assertIsInstance(MockSolution.cities_coordinates[0], tuple)

    def test_city_demands(self):
        self.assertTrue(all(d >= 0 for d in MockSolution.demands))
        self.assertEqual(len(MockSolution.demands), 21)
        self.assertEqual(MockSolution.demands[0], 0)

    def test_number_of_robots_and_capacity(self):
        self.assertEqual(MockSolution.robots, 2)
        for tour in MockSolution.tours.values():
            demand = sum(MockSolution.demands[city] for city in tour if city != 0)
            self.assertLessEqual(demand, MockSolution.capacity)

    def test_travelling_euclidean_distance(self):
        for tour, cost in MockSolution.tour_costs.items():
            calculated_cost = 0
            cities = MockSolution.tours[tour]
            for i in range(len(cities) - 1):
                calculated_cost += euclidean_distance(MockSolution.cities_coordinates[cities[i]], MockSolution.cities_coordinates[cities[i+1]])
            self.assertAlmostEqual(calculated_cost, cost, places=1)

    def test_complete_tours(self):
        for tour in MockSolution.tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_cost_verification(self):
        total_computed_cost = sum(MockSolution.tour_costs.values())
        self.assertEqual(total_computed_tcost랮MockSolution.overall_cost)

    def test_clarke_wright_usage(self):
        self.assertTrue(MockSolution.used_clarke_wright())

if __name__ == '__main__':
    unittest.main()