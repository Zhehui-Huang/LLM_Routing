import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities):
        return "FAIL"
    actual_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        actual_cost += calculate_euclidean_distance(cities[city_a][0], cities[city_a][1], cities[city_b][0], cities[city_b][1])
    if abs(total_travel_cost - actual_cost) > 1e-9:
        return "FAIL"
    return "CORRECT"

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # given tour and total travel cost
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        total_travel_cost = 345.23  # hypothetical value, replace with actual computed cost if required

        # cities coordinates from the description
        cities = [
            (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
            (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
            (60, 63), (93, 15)
        ]
        
        # invoke verification method
        result = verify_tour(tour, total_travel_cost, cities)
        
        # assert correct solution
        self.assertEqual(result, "CORRECT")

# Run tests
unittest.main(argv=[''], exit=False)