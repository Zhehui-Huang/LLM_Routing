import unittest
import math

# Given solution
solution_tour = [0, 9, 5, 6, 0]
solution_cost = 61.65991894151281

# Provided coordinates of cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_city_count(self):
        self.assertEqual(len(cities), 10, "The number of cities should be 10.")

    def test_robot_start_end_depot(self):
        self.assertEqual(solution_tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(solution_tour[-1], 0, "Tour should end at depot city 0.")

    def test_visit_four_cities(self):
        self.assertEqual(len(set(solution_tour)), 4, "Robot should visit exactly 4 unique cities including the depot.")

    def test_travel_cost(self):
        total_distance = 0
        for i in range(len(solution_tour) - 1):
            city_from = solution_tour[i]
            city_to = solution_tour[i + 1]
            total_distance += calculate_distance(cities[city_from], cities[city_to])
        
        self.assertAlmostEqual(total_distance, solution_cost, places=5, msg="The calculated travel cost should match the given solution cost.")

unittest.main(argv=[''], verbosity=2, exit=False)