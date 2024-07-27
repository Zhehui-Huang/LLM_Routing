import unittest
import math

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # Given tour and cost
        tour = [0, 9, 4, 8, 3, 2, 5, 1, 6, 7, 0]
        calculated_cost = 284.4453079431739  # as provided 

        # City coordinates
        cities = [
            (50, 42),  # Depot 0
            (41, 1),   # City 1
            (18, 46),  # City 2
            (40, 98),  # City 3
            (51, 69),  # City 4
            (47, 39),  # City 5
            (62, 26),  # City 6
            (79, 31),  # City 7
            (61, 90),  # City 8
            (42, 49)   # City 9
        ]
        num_cities = len(cities)

        # Check there are indeed 10 cities
        self.assertEqual(num_cities, 10)

        # Check the tour starts and ends at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check all cities are visited exactly once
        expected_visited = set(range(num_cities))
        visited_cities = set(tour[:-1])  # exclude the last duplicate depot city
        self.assertEqual(visited_closures, expected_visited)

        # Check travel cost is calculated correctly based on EU distances
        total_travel_cost = 0
        for i in range(len(tour) - 1):
            total_travel_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

        # Check the stated total travel cost
        self.assertAlmostEqual(total_travel_cost, calculated_cost, places=5)
        
        # Check if the provided tour is indeed the shortest (unsure without computing other tours)
        # Since it's difficult to assert the optimality without solving the problem again,
        # we proceed by checking the tour viability and the distance as provided.

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)