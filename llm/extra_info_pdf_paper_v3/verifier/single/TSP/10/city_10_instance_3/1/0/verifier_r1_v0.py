import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    cities = {
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

    def compute_distance(self, start, end):
        return sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

    def test_tour(self):
        tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        calculated_cost = 0

        # Check starting and ending at depot city 0
        self.assertEqual(tour[0], 0, "Tour must start at city 0")
        self.assertEqual(tour[-1], 0, "Tour must end at city 0")
        
        # Check if all cities except the depot are visited exactly once
        all_cities_visited_once = all(tour.count(x) == 1 for x in range(1, 10))
        self.assertTrue(all_cities_visited_once, "All cities must be visited exactly once except the depot")
        
        # Calculate and validate the travel cost using Euclidean distance
        for i in range(len(tour)-1):
            start_city = tour[i]
            end_city = tour[i+1]
            calculated_cost += self.compute_distance(self.cities[start_city], self.cities[end_city])

        expected_cost = 315.56
        # Check if the calculated cost matches the expected (within a small margin for floating point precision)
        self.assertAlmostEqual(calculated_cost, expected_cost, places=2, msg="Total travel cost should be approximately 315.56")

if __name__ == '__main__':
    unittest.main()