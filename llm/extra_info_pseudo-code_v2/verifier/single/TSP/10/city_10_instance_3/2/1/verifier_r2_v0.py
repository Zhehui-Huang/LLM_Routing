import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 
            5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
        }
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.expected_cost = 315.56

    def test_tour_starts_and_ends_at_depot(self):
        """ Check if the tour starts and ends at the depot, city 0 """
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_all_cities_once(self):
        """ Ensure all cities are visited exactly once, except the depot """
        unique_cities = set(self.tour)
        self.assertEqual(unique_cities, set(self.cities.keys()))
        self.assertEqual(len(self.tour), len(self.cities) + 1)  # +1 because we return to depot

    def test_travel_distance_calculation(self):
        """ Calculate the total travel cost and compare with the expected value """
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        total_cost = 0
        for i in range(len(self.tour)-1):
            total_cost += euclidean_distance(self.cayities[self.tour[i]], self.cities[self.tour[i+1]])
        
        self.assertAlmostEqual(total_cost, self.expected_cost, places=2)

    def test_correct_output_format(self):
        """ Check the format of output: tour list starting and ending with depot and total cost """
        self.assertIsInstance(self.tour, list)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))
        self.assertIsInstance(self.expected_cost, float)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORERECT")
    else:
        print("FAIL")