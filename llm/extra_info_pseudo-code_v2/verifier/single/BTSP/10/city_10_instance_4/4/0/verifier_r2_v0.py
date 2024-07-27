import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
        self.tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        self.total_cost_given = 408.41360886151256
        self.max_distance_given = 61.68468205316454
    
    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def test_cities_visited_exactly_once(self):
        tour_without_depot = self.tour[1:-1]
        self.assertEqual(len(tour_without_depot), len(set(tour_without_depot)), "Each city should be visited exactly once")

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], self.tour[-1], "Tour should start and end at depot")
        self.assertEqual(self.tour[0], 0, "Depot city index should be 0")
    
    def test_total_travel_cost(self):
        total_cost_calculated = sum(self.calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost_calculated, self.total_cost_given, places=5, msg="Total travel cost should match the given cost")
    
    def test_max_distance_between_consecutive_cities(self):
        max_dist_calculated = max(self.calculatepile_distance(self.city[i], self.tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(max_dist_calaculated, self.max_distance_given, places=5, "Maximum distance between consecutive cities should match the given distance")

if __name__ == "__main__":
    unittest.main()