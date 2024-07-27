import unittest
import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

# Tours provided by the user
tours = [
    [0, 21, 16, 1, 10, 0],
    [0, 6, 20, 0],
    [0, 2, 0],
    [0, 4, 11, 0],
    [0, 7, 22, 5, 0],
    [0, 13, 9, 17, 0],
    [0, 15, 12, 0],
    [0, 14, 0]
]

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

class TestTours(unittest.TestCase):
    def test_capacity(self):
        """ Test each robot's carrying capacity is not exceeded. """
        for tour in tours:
            total_demand = sum(demands[city] for city in tour if city != 0)
            self.assertLessEqual(total_demand, robot_capacity, "Capacity exceeded in one of the tours")

    def test_no_city_left_behind(self):
        """ Check if all cities are visited exactly once by one robot. """
        visited = set()
        for tour in tours:
            for city in tour:
                if city != 0:  # Exclude depot city
                    self.assertNotIn(city, visited, "A city is visited more than once")
                    visited.add(city)
        self.assertEqual(len(visited), len(coordinates) - 1, "Not all cities were visited")

    def test_tours_start_end_at_depot(self):
        """ Ensure all tours start and end at the depot. """
        for tour in tours:
            self.assertEqual(tour[0], 0, "Tour does not start at the depot")
            self.assertEqual(tour[-1], 0, "Tour does not end at the depot")

    def test_distance_calculation(self):
        """ Check the correctness of distance calculations for given tours."""
        actual_costs = [
            45.418094823641184, 34.56118681213356, 42.04759208325728, 57.394073777130664,
            56.42321680576039, 77.16742441032888, 66.12407122823275, 61.741396161732524
        ]
        for i, tour in enumerate(tours):
            calculated_cost = sum(calculate_distance(coordinates[tour[j]], coordinates[tour[j+1]]) for j in range(len(tour) - 1))
            self.assertAlmostEqual(calculated_cost, actual_costs[i], places=5, msg="Mismatch in calculated travel cost")

if __name__ == "__main__":
    unittest.main()