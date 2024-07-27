import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
            4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
            8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
            12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
            16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        self.solution_tour = [0, 16, 13, 5, 8, 10, 2, 18, 12, 7, 9, 15, 3, 11, 14, 4, 17, 6, 1, 19, 1, 0]
        self.reported_total_cost = 819.59
        self.reported_max_distance = 62.65

    def test_all_cities_visited_exactly_once(self):
        # Check the presence of each city exactly once (except depot 0 twice)
        visited = set(self.solution_tour[1:-1])  # ignore first and last
        self.assertEqual(len(visited), 19, "All cities except depot should appear exactly once.")

    def test_tour_begins_and_ends_at_depot(self):
        # Check tour starts and ends at depot
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at the depot.")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at the depot.")

    def test_total_cost_and_max_distance(self):
        cumulated_cost = 0
        max_distance = 0
        for i in range(len(self.solution_tour) - 1):
            city_a_id = self.solution_tour[i]
            city_b_id = self.solution_tour[i + 1]
            distance = calculate_distance(self.cities[city_a_id], self.cities[city_b_id])
            cumulated_cost += distance
            max_distance = max(max_distance, distance)

        # Round results to compare with reported values due to floating point arithmetic considerations
        rounded_cumulated_cost = round(cumulated_cost, 2)
        rounded_max_distance = round(max_distance, 2)

        self.assertEqual(rounded_cumulated_tour, self.report__assertAlmostEqual(self.reported_total_cost, rounded_cumulated_cost, places=2, "Total cost is not as reported.")
        self.assertAlmostEqual(self.reported_max_distance, rounded_max_distance, places=2, "Maximum distance is not as reported.")

if __name__ == '__main__':
    # run unittest in verbose mode
    unittest.main(argv=[''], verbosity=2, exit=False)