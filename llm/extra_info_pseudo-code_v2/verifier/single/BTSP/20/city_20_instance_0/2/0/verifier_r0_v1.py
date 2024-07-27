import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for each city indexed by their IDs
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
            4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
            8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
            12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
            16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        # Provided tour results
        self.solution_tour = [0, 16, 13, 5, 8, 10, 2, 18, 12, 7, 9, 15, 3, 11, 14, 4, 17, 6, 1, 19, 1, 0]
        self.reported_total_cost = 819.59
        self.reported_max_distance = 62.65

    def test_all_cities_visited_exactly_once(self):
        # Check the presence of each city exactly once (except depot city 0 which should appear twice)
        unique_cities = set(self.solution_tour)
        for city in unique_cities:
            count = self.solution_tour.count(city)
            if city == 0:
                self.assertEqual(count, 2, f"Depot city 0 should appear twice but appeared {count} times.")
            else:
                self.assertEqual(count, 1, f"City {city} appears {count} times; expected exactly once.")

    def test_tour_begins_and_ends_at_depot(self):
        # Check tour starts and ends at depot city 0
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at the depot city.")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at the depot city.")

    def test_total_cost_and_max_distance(self):
        cumulative_cost = 0
        max_distance = 0
        for i in range(len(self.solution_tour) - 1):
            distance = calculate_distance(self.cities[self.solution_tour[i]], self.cities[self.solution_tour[i + 1]])
            cumulative_cost += distance
            max_distance = max(max_distance, distance)

        # Check if reported values are consistent
        self.assertAlmostEqual(cumulative_cost, self.reported_total_cost, places=2, msg="Calculated total cost does not match reported value.")
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2, msg="Calculated maximum distance does not match reported value.")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)