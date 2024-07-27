import unittest
import math

# Provided city coordinates and demands
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
city_demand = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28,
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}
robots_tours = [
    [0, 6, 0], [0, 2, 0], [0, 1, 0], [0, 4, 15, 0], [0, 8, 0],
    [0, 7, 5, 0], [0, 14, 9, 13, 0], [0, 3, 12, 0], [0, 10, 11, 0]
]
robots_capacity = 35

# Helper function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    coord1, coord2 = city_coords[city1], city_coords[city2]
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Test class for verifying the robot routes
class TestRobotRoutes(unittest.TestCase):
    def test_demand_meet_conditions(self):
        """Test that all city demands are met without exceeding robot capacities."""
        city_delivered = {key: 0 for key in city_demand}
        for tour in robots_tours:
            remaining_capacity = robots_capacity
            for i in range(1, len(tour) - 1):
                city = tour[i]
                city_delivered[city] += city_demand[city]
                remaining_capacity -= city_demand[city]
                self.assertGreaterEqual(remaining_capacity, 0, "Robot capacity exceeded!")
        self.assertDictEqual(city_delivered, city_demand, "Not all demands are met correctly.")

    def test_return_to_depot(self):
        """Ensure each robot tour starts and ends at the depot."""
        for tour in robots_tours:
            self.assertEqual(tour[0], 0, "Tour does not start at the depot.")
            self.assertEqual(tour[-1], 0, "Tour does not end at the depot.")

    def test_total_travel_cost(self):
        """Check the correctness of the total travel cost."""
        actual_costs = [24.08, 42.05, 27.78, 61.08, 64.9, 53.11, 82.73, 72.01, 67.57]
        calculated_costs = []
        for tour in robots_tours:
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += calculate_distance(tour[i], tour[i + 1])
            calculated_costs.append(round(tour_cost, 2))
        for index, (actual, calculated) in enumerate(zip(actual_costs, calculated_costs)):
            self.assertAlmostEqual(actual, calculated, places=2, msg=f"Cost does not match for Robot {index}")

if __name__ == '__main__':
    unittest.main()