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
    def test_solution_correctness(self):
        try:
            # Check total city count
            self.assertEqual(len(cities), 10)
            # Check tour starts and ends at the depot city 0
            self.assertEqual(solution_tour[0], 0)
            self.assertEqual(solution_tour[-1], 0)
            # Check only 4 unique cities including depot are visited
            self.assertEqual(len(set(solution_tour)), 4)
            # Check the travel cost calculation
            total_distance = 0
            for i in range(len(solution_tour) - 1):
                from_city, to_city = solution_tour[i], solution_tour[i + 1]
                total_distance += calculate_distance(cities[from_city], cities[to_city])
            self.assertAlmostEqual(total_distance, solution_cost, places=5)
            print("CORRECT")
        except AssertionError:
            print("FAIL")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)