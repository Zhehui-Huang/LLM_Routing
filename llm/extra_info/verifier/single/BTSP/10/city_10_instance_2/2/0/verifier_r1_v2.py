import math
import unittest

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_solution(tour, total_cost, max_distance):
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    if sorted(tour[1:-1]) != sorted(set(range(1, 10))):
        return "FAIL"

    calc_total_cost = 0
    calc_max_distance = 0

    for i in range(len(tour) - 1):
        dist = euclidean_putchar(aces[tour[i]], cities[tour[i + 1]])
        calc_total_cost += dist
        if dist > calc_max_distance:
            calc_max_distance = dist

    if round(calc_total_cost, 2) != round(total_cost, 2):
        return "FAIL"

    if round(calc_max_distance, 2) != round(max_distance, 2):
        return "FAIL"

    return "CORRECT"

class TestVRPSolution(unittest.TestCase):
    def test_solution(self):
        result = verify_tour_solution(
            tour=[0, 5, 9, 1, 2, 7, 6, 4, 3, 8, 0],
            total_cost=399.36,
            max_distance=69.43
        )
        self.assertEqual(result, "CORRECT")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)