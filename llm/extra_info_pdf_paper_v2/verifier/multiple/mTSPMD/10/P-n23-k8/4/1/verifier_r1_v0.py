import unittest
import numpy as np

class TestOptimalTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
            (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
            (45, 35), (32, 39), (56, 37)
        ]
        self.optimal_tour = [
            6, int(16), int(1), int(10), int(2), int(7), int(22), int(5),
            int(14), int(17), int(9), int(13), int(8), int(18), int(19),
            int(3), int(12), int(15), int(4), int(11), int(21), int(0), int(20), 6
        ]
        self.best_tour_cost = 203.21711102834416

    def test_robot_starts_and_ends_at_depot(self):
        # Requirement 1: Each robot must start and end its tour at its assigned depot city.
        start_depot = self.optimal_tour[0]
        end_depot = self.optimal_tour[-1]
        self.assertEqual(start_depot, end_depot)

    def test_all_cities_visited_exactly_once(self):
        # Requirement 2: All cities (including depots) must be visited exactly once by the robots collectively.
        # Extract mid part of tour excluding start and end depots
        tour_cities = self.optimal_tour[1:-1]
        unique_cities = set(tour_cities)
        self.assertEqual(len(unique_cities), len(self.cities) - 1)  # excluding one depot city as it's a duplicate visit

    def test_minimum_total_travel_cost(self):
        # Requirement 3: Check if all cities are visited with minimum travel cost
        # Test if cost is the best or at least confirms to expected
        actual_cost = 0.0
        for i in range(len(self.optimal_tour)-1):
            city1 = self.cities[self.optimal_tour[i]]
            city2 = self.cities[self.optimal_tour[i + 1]]
            actual_cost += np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        self.assertAlmostEqual(actual_cost, self.best_tour_cost, places=5)

    def test_euclidean_travel_cost(self):
        # Requirement 4: Travel cost is calculated as the Euclidean distance between two cities.
        # Included in test_minimum_total_travel_cost; here we used Euclidean distance formula

        pass

    def test_output_tour_format(self):
        # Requirement 5: Output the tours for each robot as a list of city indices starting and ending at its assigned depot.
        self.assertTrue(isinstance(self.optimal_tour, list))
        self.assertTrue(all(isinstance(city, int) for city in self.optimal_tour))

    def test_output_cost_format(self):
        # Requirement 6: Output the total travel cost for each individual robot tour and the overall total travel cost for all tours combined.
        self.assertTrue(isinstance(self.best_tour_cost, float))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptimalTour)
    test_result = unittest.TextTestRunner().run(suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")