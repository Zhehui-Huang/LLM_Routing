import unittest
from math import sqrt

# City coordinates (indexed from 0 to 15)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Tours provided in the solution
tours = [
    [0, 9, 13, 0], [0, 12, 15, 0], [0, 6, 0], [0, 4, 11, 0], [0, 5, 14, 0], 
    [0, 8, 3, 0], [0, 10, 1, 0], [0, 2, 7, 0]
]

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Given travel costs for validation
given_costs = [68.39, 66.12, 24.08, 57.39, 62.44, 72.82, 41.77, 51.59]

class TestMTSPSolution(unittest.TestCase):
    def test_unique_city_visits(self):
        "Test that all cities, except the depot, are visited exactly once."
        all_visited_cities = [city for tour in tours for city in tour if city != 0]
        self.assertEqual(len(set(all_visited_cities)), 15)  # There are 15 other cities

    def test_tour_start_end(self):
        "Test that each tour starts and ends at the depot."
        for tour in tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_travel_costs(self):
        "Test the correctness of the reported travel costs for each tour."
        for i, tour in enumerate(tours):
            total_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour) - 1))
            self.assertAlmostEqual(total_cost, given_costs[i], places=2)

    def test_minimize_maximum_distance(self):
        "Test that the maximum travel cost is minimized (based on provided data)."
        calculated_max_cost = max(given_costs)
        self.assertEqual(calculated99tr

    def test_all_cities_served(self):
        "Test that every city is included in some tour."
        combined_tours = sum(tours, [])
        self.assertTrue(all(city in combined_tours for city in range(1, 16)))

# Entry point for unittest
if __name__ == '__main__':
    unittest.main()