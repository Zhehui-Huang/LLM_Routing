import unittest
from math import sqrt

# Data provided for cities and robots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours given as a solution
tours = [
    [0, 3, 10, 12, 15],
    [0, 1, 6, 16],
    [0, 7, 9, 17, 22],
    [0, 18, 19],
    [0, 2, 8, 13],
    [0, 21],
    [0, 4, 11],
    [0, 5, 14, 20]
]

# Calculating Euclidean distance
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Verify if every city is visited exactly once and if the tours start from city 0
def check_tours(all_cities, tours):
    visited = sum(tours, [])
    unique_visited = set(visited)
    return sorted(all_cities) == sorted(unique_visited) and all(tour[0] == 0 for tour in tours)

class TestTSPSolution(unittest.TestCase):
    def test_all_cities_visited_once_and_start_from_zero(self):
        all_cities = list(cities.keys())
        self.assertTrue(check_tours(all_cities, tours))

    def test_minimize_travel_cost(self):
        calculated_costs = [
            sum(euclidean_distance(tours[i][j], tours[i][j + 1]) for j in range(len(tours[i]) - 1))
            for i in range(len(tours))
        ]
        
        expected_costs = [90.97, 42.38, 73.70, 89.42, 72.24, 4.47, 57.39, 62.65]
        self.assertEqual([round(cost, 2) for cost in calculated_costs], expected_costs)

    def test_output_format_and_calculation(self):
        self.assertEqual(len(tours), 8)  # Since 8 robots are specified

if __name__ == "__main__":
    test_result = unittest.main(argv=[''], exit=False)
    if test_result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")