import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
        self.total_travel_cost = 442.570870788815
        self.max_distance_between_cities = 85.21150157109074
        self.coordinates = [
            (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
            (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
            (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
        ]
    
    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_exactly_once(self):
        # Requirement 2
        visited = sorted(self.t,our[:-1])
        self.assertEqual(visited, list(range(1, 15)))
        
    def test_output_tour_format(self):
        # Requirement 4
        self.assertIsInstance(self.tour, list)

    def test_output_total_travel_cost(self):
        # Requirement 5
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.coordinates[self.tour[i]]
            city2 = self.coordinates[self.tour[i + 1]]
            calculated_cost += math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost, places=5)

    def test_output_maximum_distance(self):
        # Requirement 6
        max_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.coordinates[self.tour[i]]
            city2 = self.coordinates[self.tour[i + 1]]
            distance = math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)
            if distance > max_distance:
                max_distance = distance
        self.assertAlmostEqual(max_distance, self.max_distance_between_cities, places=5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
          print("FAIL")