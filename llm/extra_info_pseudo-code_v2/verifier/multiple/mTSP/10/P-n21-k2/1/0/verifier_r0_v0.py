import unittest
from math import sqrt

# Provided cities data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculating the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Validate the solution
class TestTSPSolution(unittest.TestCase):
    def test_unique_visitation_and_return_to_depot(self):
        # Robot tours from the described solution
        tours = [
            [0, 1, 4, 10, 2, 3, 8, 9, 7, 5, 6, 0],
            [0, 16, 11, 15, 12, 19, 18, 13, 17, 14, 20, 0]
        ]
        all_visited = set()
        for tour in tours:
            self.assertEqual(tour[0], tour[-1])  # Checks start and end at depot
            for city in tour[1:-1]:
                all_visited.add(city)
        
        # Check if all cities are visited exactly once
        self.assertEqual(len(all_visited), 20)
        self.assertEqual(all_visited, set(range(1, 21)))  # cities 1 to 20

    def test_correct_total_costs(self):
        # Robot tours and reported costs from solution
        tours = [
            [0, 1, 4, 10, 2, 3, 8, 9, 7, 5, 6, 0],
            [0, 16, 11, 15, 12, 19, 18, 13, 17, 14, 20, 0]
        ]
        reported_costs = [131.03562107117372, 145.75885545934872]
        calculated_costs = [0, 0]
        
        for i, tour in enumerate(tours):
            tour_cost = 0
            for j in range(len(tour) - 1):
                tour_cost += calculate_distance(tour[j], tour[j + 1])
            calculated_costs[i] = tour_cost

        # Compare calculated costs with reported costs
        for i in range(2):
            self.assertAlmostEqual(calculated_costs[i], reported_costs[i], places=5)

        # Check total cost
        self.assertAlmostEqual(sum(calculated_costs), 276.79447653052245, places=5)

if __name__ == '__main__':
    # Run unittest to test the correctness of the solution
    unittest.main(argv=[''], exit=False)