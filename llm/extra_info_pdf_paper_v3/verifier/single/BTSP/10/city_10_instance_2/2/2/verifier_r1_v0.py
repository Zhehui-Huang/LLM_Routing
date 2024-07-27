import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
                       (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
        self.claimed_tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
        self.claimed_total_cost = 418.32
        self.claimed_max_distance = 69.43
    
    def euclidean_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.claimed_tour[0], 0)
        self.assertEqual(self.claimed_tour[-1], 0)

    def test_visit_each_city_exactly_once(self):
        cities_visited = set(self.claimed_tour)
        all_cities = set(range(len(self.cities)))
        self.assertEqual(cities_visited, all_cities)

    def test_correct_total_and_maximum_travel_cost(self):
        calculated_distances = []
        for i in range(len(self.claimed_tour) - 1):
            dist = self.euclidean_distance(
                self.cities[self.claimed_tour[i]], self.cities[self.claimed_tour[i + 1]])
            calculated_distances.append(dist)
        calculated_total_cost = sum(calculated_distances)
        calculated_max_distance = max(calculated_distances)
        self.assertAlmostEqual(calculated_total_cost, self.claimed_total_cost, places=2)
        self.assertAlmostEqual(calculated_max_distance, self.claimed_max_distance, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTravelingSalesmanSolution)
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")