import unittest
from math import sqrt

# Defines the cities coordinates as tuples, where each tuple represents (x, y)
cities = [
    (30, 56),  # City 0 (Depot)
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_tour_validity(self):
        solution_tour = [0, 1, 15, 17, 16, 9, 5, 3, 11, 10, 4, 7, 8, 14, 18, 12, 2, 13, 6, 19, 0]
        correct_flag = True

        # Check if the tour starts and ends at depot city 0
        if solution_tour[0] != 0 or solution_tour[-1] != 0:
            correct_flag = False
        # Check if all cities except depot are visited exactly once
        visited_cities = set(solution_tour[1:-1])
        if len(visited_cities) != 19 or not all(city in visited_cities for city in range(1, 20)):
            correct_flag = False
        # Verify the reported total travel cost
        reported_cost = 577.4603341121659
        calculated_cost = sum(calculate_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
                               for i in range(len(solution_tour) - 1))
        if not abs(calculated_cost - reported_cost) < 0.01:
            correct_flag = False

        if correct_flag:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)