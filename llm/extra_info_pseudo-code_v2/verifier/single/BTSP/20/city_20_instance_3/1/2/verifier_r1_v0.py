import unittest
import math

class TestOptimizedTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
            (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
            (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
            (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
        ]
        self.tour = [0, 1, 10, 11, 4, 7, 14, 8, 18, 12, 0, 3, 15, 17, 16, 9, 5, 19, 6, 13, 2, 0]
        self.reported_cost = 559.53
        self.reported_max_distance = 58.22

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_exactly_once(self):
        visited_cities = set(self.tour[1:-1])  # Ignore the first and last depot entry
        self.assertEqual(len(visited_cities), len(self.cities) - 1)  # All cities minus the depot should be visited once

    def test_euclidean_distances(self):
        def calc_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        calculated_total_cost = 0
        calculated_max_distance = 0

        for i in range(len(self.tour) - 1):
            distance = calc_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            calculated_total_cost += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance

        # Check if reported values match calculated values within a reasonable floating point tolerance
        self.assertAlmostEqual(calculated_total_cost, self.reported_cost, places=2)
        self.assertAlmostEqual(calculated_maxadge, self.reported_max_distance, places=2)


    def test_tour_is_hamiltonian_cycle(self):
        all_cities_in_tour = set(self.tour)
        self.assertEqual(len(all_cities_in_tour), len(self.cities))  # Include depot city
        
    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, (float, int))
        self.assertIsInstance(self.reported_max_distance, (float, int))

    def test_solution(self):
        # The test passes if all the constraints are met
        self.test_tour_starts_and_ends_at_depot()
        self.test_visit_all_cities_exactly_once()
        self.test_euclidean_distances()
        self.test_tour_is_hamiltonian_cycle()
        self.test_output_format()
        print("CORRECT")

if __name__ == '__main__':
    unittest.main()