import unittest
import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_cost, max_distance):
    cities = [
        (3, 26),  # Depot city 0
        (85, 72),
        (67, 0),
        (50, 99),
        (61, 89),
        (91, 56),
        (2, 65),
        (38, 68),
        (3, 92),
        (59, 8),
        (30, 88),
        (30, 53),
        (11, 14),
        (52, 49),
        (18, 49),
        (64, 41),
        (28, 49),
        (91, 94),
        (51, 58),
        (30, 48)
    ]
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(set(tour)) != len(tour) - 1 or len(tour) != len(cities) + 1:
        return "FAIL"

    # [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify the travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i + 1]]
        distance = calculate_euclidean_distance(city_a, city_b)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # [Requirement 6]
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 7]
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
        total_travel_cost = 478.43
        max_distance_between_cities = 80.61
        result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
        self.assertEqual(result, "CORRECT")

if __name__ == '__main__':
    unittest.main()