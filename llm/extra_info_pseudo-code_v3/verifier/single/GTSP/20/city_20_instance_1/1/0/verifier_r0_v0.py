import unittest
import math

# Define the provided tour and its cost
solution_tour = [0, 6, 13, 2, 9, 0]
solution_cost = 114.65928837582914

# Environment details
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Group details
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_is_correct_length(self):
        self.assertEqual(len(solution_tour), 6)

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0)
        self.assertEqual(solution_tour[-1], 0)

    def test_visits_each_group_exactly_once(self):
        groups_visited = []
        for city in solution_tour:
            for group_idx, group in city_groups.items():
                if city in group:
                    groups_visited.append(group_idx)
        self.assertEqual(sorted(set(groups_visited)), [0, 1, 2, 3])

    def test_correct_calculation_of_travel_cost(self):
        calculated_cost = 0
        for i in range(len(solution_tour)-1):
            city_a = solution_tour[i]
            city_b = solution_tour[i + 1]
            calculated_cost += calculate_distance(city_coordinates[city_a], city_coordinates[city_b])
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5)

# Test Execution
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
result = unittest.TextTestRunner(verbosity=2).run(suite)
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")