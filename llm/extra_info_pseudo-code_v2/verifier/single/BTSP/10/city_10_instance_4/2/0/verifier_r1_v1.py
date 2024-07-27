import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.reported_total_distance = 320.8
        self.reported_max_distance = 61.7

    def test_tour_starts_and_ends_at_depot(self):
        """ Ensure the tour starts and ends at the depot city. """
        self.assertEqual(self.tour[0], 0, "Tour should start at the depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at the depot city 0")

    def test_visit_each_city_once(self):
        """ Check that each city is visited exactly once, excluding the depot at start and end. """
        self.assertEqual(sorted(self.tour[1:-1]), sorted(list(self.cities.keys())[1:]), "Each city must be visited exactly once")

    def test_minimize_longest_travel_distance(self):
        """ Validate that the longest single jump is minimized in the reported results. """
        calculated_max_distance = 0
        actual_total_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            distance = math.sqrt((self.cities[city1][0] - self.cities[city2][0]) ** 2 + (self.cities[city1][1] - self.cities[city2][1]) ** 2)
            actual_total_distance += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance
        
        self.assertAlmostEqual(calculated_max_distance, self.reported_max_distance, delta=0.1, msg="Calculated and reported maximum distance between consecutive cities should match")
        self.assertAlmostEqual(actual_total_distance, self.reported_total_distance, delta=0.1, msg="Calculated and reported total travel cost should match")

if __name__ == '__main__':
    # Load and run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)