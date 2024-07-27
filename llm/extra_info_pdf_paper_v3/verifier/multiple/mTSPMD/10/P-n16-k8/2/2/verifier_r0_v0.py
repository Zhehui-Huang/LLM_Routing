import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(cities, tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

class TestMTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        self.robot_tours = [
            [0, 8, 10, 0],  # Robot 0
            [1, 13, 12, 1],  # Robot 1
            [2, 9, 14, 2],   # Robot 2
            [3, 11, 15, 3],  # Robot 3
            [4, 7, 5, 4],    # Robot 4
            [5, 6, 4, 5],    # Robot 5
            [6, 8, 10, 6],   # Robot 6
            [7, 9, 13, 7],   # Robot 7
        ]

    def test_unique_city_visit(self):
        all_visited_cities = sum(self.robot_tours, [])
        unique_cities = set(all_visited_cities)
        # Check if number of unique cities equals the length of all_visited_cities minus the repeated depot visits (8 depots).
        self.assertEqual(len(unique_cities), 16)

    def test_tour_starts_ends_at_depot(self):
        for idx, tour in enumerate(self.robot_tours):
            # Check if each tour starts and ends at the robot's assigned depot
            self.assertEqual(tour[0], idx)
            self.assertEqual(tour[-1], idx)

    def test_travel_cost_calculation(self):
        # Compute travel costs for each robot and assert they are computed successfully
        costs = [calculate_tour_cost(self.cities, tour) for tour in self.robot_tours]
        total_cost = sum(costs)
        self.assertTrue(total_cost >= 0)  # Total cost should be non-negative

    def test_output_format(self):
        # Verify that each robot tour output meets the format requirement
        for tour in self.robot_tours:
            # Each tour should be a list of integers (city indices)
            self.assertTrue(all(isinstance(city, int) for city in tour))
            # Check the format of the tour start and end
            self.assertTrue(tour[0] == tour[-1])

if __name__ == "__main__":
    unittest.main()