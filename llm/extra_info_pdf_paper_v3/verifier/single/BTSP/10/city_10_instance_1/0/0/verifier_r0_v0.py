import math
from unittest import TestCase, main

cities = [
    (53, 68),  # City 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestVRPSolution(TestCase):
    def test_tsp_solution(self):
        tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
        reported_total_cost = 291.41
        reported_max_distance = 56.61

        # Check start and end at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check that all cities are visited exactly once
        self.assertEqual(len(set(tour)), len(cities))

        total_distance = 0.0
        max_distance = 0.0

        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            total_distance += dist
            max_distance = max(max_distance, dist)

        # Check the total travel distance and maximum distance
        total_distance = round(total_distance, 2)
        max_distance = round(max_distance, 2)

        self.assertAlmostEqual(total_distance, reported_total_cost)
        self.assertAlmostEqual(max_distance, reported_max_distance)

        print("CORRECT")  # Prints correct if all assertions are passed.

if __name__ == '__main__':
    try:
        main(argv=['first-arg-is-ignored'], exit=False)
    except Exception as e:
        print("FAIL")