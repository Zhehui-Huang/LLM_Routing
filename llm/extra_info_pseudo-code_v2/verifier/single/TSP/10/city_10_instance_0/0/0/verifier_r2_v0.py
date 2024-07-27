import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost_claimed):
    if len(tour) != 11:  # Requirement 6
        return False
    if tour[0] != 0 or tour[-1] != 0:  # Requirement 3
        return False
    if len(set(tour)) != len(tour):  # Requirement 3
        return False
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(total_cost_claimed, total_cost_calculated, abs_tol=0.001):  # Requirement 7
        return False
    return True

class TestRobotTour(unittest.TestCase):
    def test_solution(self):
        # Definitions
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
        tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
        total_cost = 271.4716218753353
        
        # Conduct Test
        result = verify_tour(cities, tour, total_cost)
        
        # Evaluate Result
        if result:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)