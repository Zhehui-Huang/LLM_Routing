import unittest
import math

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities' coordinates
        self.cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        # Provided tour and its reported cost
        self.tour = [0, 8, 5, 9, 1, 2, 7, 4, 6, 3, 0]
        self.reported_cost = 354.91010610434057

    def test_starts_and_ends_at_depot(self):
        """ Ensure the tour starts and ends at the depot city 0. """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_all_cities_once(self):
        """ Tour must visit each of the other cities exactly once. """
        expected_cities = set(range(1, 10))
        visited_cities = set(self.tour[1:-1])
        self.assertEqual(visited_cities, expected_cities)

    def test_correct_travel_cost(self):
        """ Check if the computed total travel cost matches the reported cost with precision. """
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_from = self.tour[i]
            city_to = self.tour[i + 1]
            calculated_cost += euclidean_distance(self.cities[city_from], self.cities[city_to])
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

    def test_correct_output_format(self):
        """ Test if the tour output is in the correct list format. """
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

# To run the tests
if __name__ == '__main__':
    unittest.main()