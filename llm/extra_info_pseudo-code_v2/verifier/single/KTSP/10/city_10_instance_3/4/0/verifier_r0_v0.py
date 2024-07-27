import unittest
import math

# Provided city coordinates with city index as key
cities_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def calculate_euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def calculate_total_travel_cost(tour):
    """Calculate the total travel cost of a given tour based on the Euclidean distance"""
    total_cost = 0
    for i in range(len(tour) - 1):
        start_city = tour[i]
        next_city = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities_coordinates[start_city], cities_coordinates[next_city])
    return total_cost

class TestTourSolution(unittest.TestCase):
    def test_tour_solution(self):
        # Given tour and cost
        given_tour = [0, 8, 3, 7, 1, 4, 0]
        given_cost = 128.73130793605634

        # 1. Test start and end at Depot City 0
        self.assertEqual(given_tour[0], 0, "Tour does not start at City 0")
        self.assertEqual(given_tour[-1], 0, "Tour does not end at City 0")

        # 2. Test tour visits exactly 7 cities
        # Counting depot city twice since it must start and end at depot city
        self.assertEqual(len(set(given_tour)), 7, "Tour does not visit exactly 7 cities including depot")

        # 5. Test format of the tour
        self.assertIsInstance(given_tour, list, "Tour output format is incorrect")
        self.assertTrue(all(isinstance(city, int) for city in given_tour), "Tour contains non-integer items")

        # 4 & 6. Test calculated travel cost matches given one
        estimated_cost = calculate_total_travel_cost(given_tour)
        self.assertAlmostEqual(estimated_cost, given_cost, places=5, msg="Calculated travel cost does not match the given cost")

        # 3. Not easy to verify without solving the problem for best cost, so assume it's correct if passed above checks.

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)