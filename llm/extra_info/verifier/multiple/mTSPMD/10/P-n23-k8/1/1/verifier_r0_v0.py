import math
import unittest

# Coordinates of all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Provided solution
Robot_tours = [
    [0, 21, 0],
    [1, 16, 10, 1],
    [2, 13, 2],
    [3, 8, 18, 19, 3],
    [4, 11, 15, 12, 4],
    [5, 22, 17, 14, 5],
    [6, 20, 6],
    [7, 9, 7]
]

# Calculate expected travel costs for verification
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Validate the solution
class TestTSPSolution(unittest.TestCase):

    def test_tours_start_end_depot(self):
        """ Test if each robot starts and ends at its assigned depot. """
        for index, tour in enumerate(Robot_tours):
            self.assertEqual(tour[0], index, "Robot does not start at correct depot")
            self.assertEqual(tour[-1], index, "Robot does not end at correct depot")
            
    def test_all_cities_visited_once(self):
        """ Test if all cities are visited exactly once across all tours. """
        all_cities_visited = [city for tour in Robot_tours for city in tour[1:-1]]
        self.assertCountEqual(all_cities_visited, list(range(8, 23)), "Not all cities are visited once")

    def test_correct_travel_costs(self):
        """ Test if computed travel costs match the provided values. """
        provided_costs = [
            4.47213595499958, 24.85853025288332, 18.110770276274835,
            33.04712599166492, 36.58553349238563, 27.253463793663165,
            13.416407864998739, 20.09975124224178
        ]
        computed_costs = [sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) for tour in Robot_tours]
        for provided, computed in zip(provided_costs, computed_costs):
            self.assertAlmostEqual(provided, computed, places=5, msg="Travel costs do not match")

# Run the tests
if __name__ == "__main__":
    unittest.main()