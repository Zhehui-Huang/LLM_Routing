import math
import unittest

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), 
                       (22, 21), (97, 70), (20, 99), (66, 62)]
        self.proposed_tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
        self.proposed_cost = 337.17

    def test_tour_starts_and_ends_at_depot(self):
        """Check if the tour starts and ends at the depot city."""
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)

    def test_visits_all_cities_once(self):
        """Check that all cities are visited exactly once, except depot city."""
        tour_without_depot = self.proposed_tour[1:-1]
        unique_cities_visited = set(tour_without_depot)
        self.assertEqual(len(tour_without_depot), len(unique_cities_visited))
        self.assertEqual(len(unique_cities_visited), len(self.cities) - 1)

    def test_travel_cost_calculation(self):
        """Calculate total travel cost using Euclidean distance and compare with proposed cost."""
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        computed_cost = 0
        for i in range(len(self.proposed_tour) - 1):
            start_city_idx = self.proposed_tour[i]
            end_city_idx = self.proposed_tour[i + 1]
            computed_cost += euclidean_distance(self.cities[start_city_idx], self.cities[end_city_idx])

        self.assertAlmostEqual(computed_cost, self.proposed_cost, places=2)

if __name__ == '__main__':
    unittest.main()