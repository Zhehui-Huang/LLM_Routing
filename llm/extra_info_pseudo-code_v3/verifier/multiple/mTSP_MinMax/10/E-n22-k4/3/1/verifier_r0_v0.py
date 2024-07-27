import unittest
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
            (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ]
        self.tours = [
            [0, 14, 3, 11, 19, 1, 2, 9, 0],
            [0, 16, 4, 20, 21, 7, 0],
            [0, 15, 18, 6, 8, 10, 13, 5, 0],
            [0, 12, 17, 0]
        ]
        self.travel_costs = [260.5536533340566, 241.45596812982933, 218.77252193343912, 58.903073157826064]
        self.num_robots = 4
        self.minimize_max_distance = 260.5536533340566
        self.num_cities = 22

    def test_city_count(self):
        unique_cities = set()
        for tour in self.tours:
            unique_cities.update(tour)
        unique_cities.remove(0)  # Excluding depot city
        self.assertEqual(len(unique_cities), self.num_cities - 1)

    def test_each_robot_starts_ends_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_calculate_travel_cost(self):
        for i, tour in enumerate(self.tours):
            travel_cost = 0
            for j in range(len(tour) - 1):
                travel_cost += calculate_distance(self.coordinates[tour[j]], self.coordinates[tour[j+1]])
            self.assertAlmostEqual(travel_cost, self.travel_costs[i], places=2)

    def test_minimize_maximum_travel_cost(self):
        calculated_costs = []
        for tour in self.tours:
            cost = 0
            for i in range(len(tour) - 1):
                cost += calculate_distance(self.coordinates[tour[i]], self.coordinates[tour[i+1]])
            calculated_costs.append(cost)
        self.assertAlmostEqual(max(calculated_costs), self.minimize_max_distance, places=2)
    
    def test_number_of_robots(self):
        self.assertEqual(len(self.tours), self.num_robots)

    def test_output_structure(self):
        # Test with specific example given
        self.assertEqual(len(self.tours), 4)
        for tour in self.tours:
            self.assertIsInstance(tour, list)
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

unittest.main(argv=[''], exit=False)  # Run the test