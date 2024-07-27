import unittest
from math import sqrt

def calculate_distance(city_a, city_b):
    return sqrt((city_b[0] - city_a[0]) ** 2 + (city_b[1] - city_a[1]) ** 2)

def verify_solution(tour, distances, total_cost, max_distance):
    # Check if tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once except the depot
    city_visit_count = {i: 0 for i in range(len(distances))}
    for city in tour:
        city_visit_count[city] += 1

    if any(count != 1 for i, count in city_visit_count.items() if i != 0):
        return "FAIL"
    if city_visit_count[0] != 2:
        return "FAIL"

    # Compute and check total travel cost and max distance
    computed_total_cost = 0
    computed_max_distance = 0

    for i in range(1, len(tour)):
        distance = calculate_distance(distances[tour[i - 1]], distances[tour[i]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance

    if not (abs(computed_total_cost - total_cost) < 1e-2 and abs(computed_max_distance - max_distance) < 1e-2):
        return "FAIL"

    return "CORRECT"

class TestTSPVRPSolution(unittest.TestCase):
    def test_solution(self):
        tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
        total_cost = 373.97
        max_distance = 63.6

        # Assuming coordinates in order of city numbers from 0 to 14
        coordinates = [
            (9, 93),  # City 0
            (8, 51),  # City 1
            (74, 99),  # City 2
            (78, 50),  # City 3
            (21, 23),  # City 4
            (88, 59),  # City 5
            (79, 77),  # City 6
            (63, 23),  # City 7
            (19, 76),  # City 8
            (21, 38),  # City 9
            (19, 65),  # City 10
            (11, 40),  # City 11
            (3, 21),  # City 12
            (60, 55),  # City 13
            (4, 39)   # City 14
        ]

        result = verify_solution(tour, coordinates, total_cost, max_distance)
        self.assertEqual(result, "CORRECT")

if __name__ == "__main__":
    unittest.main()