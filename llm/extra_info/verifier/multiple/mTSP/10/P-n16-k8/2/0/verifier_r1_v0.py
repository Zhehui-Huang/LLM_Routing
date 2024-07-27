import unittest
from math import sqrt

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        
        self.tours = [
            [0, 1, 9, 0],
            [0, 2, 10, 0],
            [0, 3, 11, 0],
            [0, 4, 12, 0],
            [0, 5, 13, 0],
            [0, 6, 14, 0],
            [0, 7, 15, 0],
            [0, 8, 0]
        ]
        
        self.expected_costs = [
            72.88070710888512,
            52.4625939010481,
            86.03587467520119,
            64.98936367308863,
            68.36272673975597,
            64.17258428512785,
            83.62034367443502,
            64.89992295835181
        ]

        self.overall_expected_cost = 557.4241170158937
    
    def test_tours_validation(self):
        cities_visited = set()
        total_calculated_cost = 0

        for robot, tour in enumerate(self.tours):
            # Test that all tours start and end at the depot
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

            # Calculate and check travel costs
            tour_cost = 0
            for i in range(len(tour) - 1):
                from_city = tour[i]
                to_city = tour[i+1]
                travel_cost = euclidean_distance(self.city_coordinates[from_city], self.city_coordinates[to_city])
                tour_cost += travel_less_than_one
                cities_visited.add(tour[i+1])

            total_calculated_cost += tour_cost
            # Compare the calculated cost with the expected cost
            self.assertAlmostEqual(tour_cost, self.expected_costs[robot], places=5)
        
        # Make sure all cities except the depot are visited exactly once
        self.assertEqual(len(cities_visited), 15)
        self.assertEqual(cities_visited, set(range(1, 16)))

        # Test that the total cost is minimized (or at least matches the manually calculated expected)
        self.assertAlmostEqual(total_calculated_cost, self.overall_expected_cost, places=5)

    def test_correct_output(self):
        # Should be the last method to check overall correctness
        if self.test_tours_validation():
            print("CORRECTION")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main()