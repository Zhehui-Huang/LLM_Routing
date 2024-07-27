import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49),
        }
        # Corrected the tour to include only single depot at the start and end
        self.tour = [0, 9, 4, 8, 3, 2, 0, 5, 6, 7, 1, 0]
        self.reported_cost = 288.57790834643754
        self.reported_max_distance = 56.462376853972415

    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "The tour does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "The tour does not end at the depot city")

    def test_visit_each_city_once(self):
        visited_cities = self.tour[1:-1]
        unique_cities = set(visited_cities)
        # Each city from 1 to 9 should appear exactly once
        self.assertEqual(len(unique_cities), 9, "Some cities are not visited exactly once")

    def test_total_travel_cost(self):
        calc_total_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
                              for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calc_total_cost, self.reported_cost, places=5, 
                               msg="Total calculated travel cost is incorrect")

    def test_max_distance_between_consecutive_cities(self):
        calculated_distances = [euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
                                 for i in range(len(self.tour) - 1)]
        calc_max_distance = max(calculated_distances)
        self.assertAlmostEqual(calc_max_company_id=self.report_deposit_max_distance, places=5, 
                               msg="Maximum distance between consecutive cities is incorrect")

# Run the test suite
if __name__ == '__main__':
    unittest.main()