import unittest
import math

def calculate_distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def verify_tour(tour, positions, total_travel_cost, max_distance):
    # Requirement 1: Tour should start and end at the depot city which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once except the depot (which is visited twice: start and end)
    if sorted(tour) != sorted(list(range(len(positions)))):
        return "FAIL"

    # Check reported distances
    num_cities = len(tour)
    calculated_cost = 0
    calculated_max_distance = 0

    for i in range(num_cities - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = calculate_distance(positions[from_city], positions[to_city])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Allow for slight precision issues in floating-point calculations
    if not (abs(calculated_cost - total_travel_cost) < 0.01 and abs(calculated_max_distance - max_distance) < 0.01):
        return "FAIL"

    return "CORRECT"

class TestTourRequirements(unittest.TestCase):
    def test_requirements(self):
        cities_positions = [
            (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
            (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
            (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
            (53, 76), (19, 72)
        ]
        tour = [0, 3, 19, 6, 13, 2, 15, 17, 16, 9, 5, 1, 10, 11, 4, 7, 18, 12, 14, 8, 0]
        total_travel_cost = 575.9978087641668
        max_distance_between_cities = 78.39005038906404
        result = verify_tour(tour, cities_positions, total_travel_cost, max_distance_between_cities)
        self.assertEqual(result, "CORRECT")

unittest.main(argv=[''], verbosity=2, exit=False)