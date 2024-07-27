import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Cities coordinates as given
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
        # Provided solution tour
        self.tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        # Provided total cost and max distance
        self.total_travel_cost = 637.815708196756
        self.max_distance = 61.68468205316454

    def test_starts_and_ends_at_depot(self):
        # Check if tour starts and ends at the depot (city 0)
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_each_city_once(self):
        # Check if each city is visited exactly once, consider 0 twice (start/end)
        cities_visited = list(sorted(self.tour[:-1]))
        self.assertListEqual(cities_visited, list(range(10)))

    def test_euclidean_distance_calculation(self):
        # Function to calculate Euclidean distance between two cities
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # Calculate the total travel cost and maximum distance between consecutive cities
        total_cost = 0
        max_dist = 0
        for i in range(len(self.tour) - 1):
            dist = euclidean_distance(self.tour[i], self.tour[i + 1])
            total_cost += dist
            max_dist = max(max_dist, dist)
        
        # Check if calculated and provided total cost and max distances match
        self.assertAlmostEqual(total_cost, self.total_travel_cost, places=2)
        self.assertAlmostEqual(max_dist, self.max_discounted_ROMPT, places=2)

if __name__ == "__main__":
    unittest.main()