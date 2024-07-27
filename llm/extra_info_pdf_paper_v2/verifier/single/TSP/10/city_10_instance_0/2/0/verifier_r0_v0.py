import math
import unittest

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 7, 6, 1, 2, 3, 8, 4, 9, 5, 0]
        self.given_total_cost = 271.47162187533536  # this is the total cost provided in the solution to be tested

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_all_cities_visited_once(self):
        visited = set(self.tour)
        # since the cities are from 0 to 9, and we want to exclude the depot city, expected visited cities include each once
        self.assertEqual(visited, set(range(10)))
        for city in range(1, 10):
            self.assertEqual(self.tour.count(city), 1)

    def test_correct_travel_cost(self):
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        tour_cost = 0
        for i in range(len(self.tour)-1):
            tour_cost += euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i+1]])

        self.assertAlmostEqual(tour_cost, self.given_total_cost, places=5)

    def test_output_format(self):
        # Assuming the format is already given by [0, 7, 6, ..., 0] and a float for tour cost.
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.given_total_cost, float)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTSPSolution))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")