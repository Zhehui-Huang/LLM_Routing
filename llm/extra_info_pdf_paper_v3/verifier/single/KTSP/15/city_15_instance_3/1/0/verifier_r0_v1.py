import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities' coordinates given in the problem description
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
            5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
            10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        self.tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 0]
        self.total_cost_given = 199.08346708108826

    def euclidean_distance(self, c1, c2):
        """ Calculate Euclidean distance between two points (x1, y1) and (x2, y2). """
        return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

    def test_tour_start_end_at_depot(self):
        """ Test if the tour starts and ends at the depot (city 0). """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_exactly_ten_cities(self):
        """ There should be 10 unique cities visited, including the depot. """
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 10)

    def test_travel_cost(self):
        """ Test if the calculated total distance matches the given distance approximately. """
        total_calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i + 1]]
            total_calculated_cost += self.euclidean_distance(city_a, city_b)
        
        self.assertAlmostEqual(total_calculated_cost, self.total_cost_given, places=5)

    def test_tour_output_format(self):
        """ Ensure that the output format adheres to the constraints. """
        self.assertEqual(len(self.tour), 11)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

if __name__ == "__main__":
    unittest.main()