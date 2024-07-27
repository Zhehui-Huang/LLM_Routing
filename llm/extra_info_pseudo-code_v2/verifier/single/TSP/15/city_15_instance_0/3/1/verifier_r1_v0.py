import math
import unittest

# Provided City Coordinates
city_coordinates = [
    (9, 93),  # Depot City 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Provided solution
tour_solution = [0, 8, 10, 1, 11, 14, 12, 4, 9, 7, 3, 5, 6, 2, 13, 0]
total_cost_solution = 359.54

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, total_cost):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Verify all cities are visited exactly once except the depot city 0
    visited = set(tour)
    if len(visited) != 15 or tour.count(0) != 2:
        return False
    # Verify total cost
    calculated_cost = sum([calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)])
    if abs(calculated_cost - total_cost) > 0.01:  # Allow small floating point discrepancy
        return False
    return True

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Check if the provided solution meets all the requirements
        result = verify_tour(tour_solution, total_cost_solution)
        self.assertTrue(result)

if __name__ == "__main__":
    # Run unit tests
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")