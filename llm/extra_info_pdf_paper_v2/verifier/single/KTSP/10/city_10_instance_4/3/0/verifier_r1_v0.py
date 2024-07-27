import math
import unittest

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(cities, tour, total_cost):
    """ Verify the solution based on the given constraints. """
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly 8 cities are visited 
    if len(set(tour)) - 1 != 8:  # minus 1 to ignore the duplicate depot city
        return False
    
    # Check if all cities in tour are valid
    if any(city not in range(len(cities)) for city in tour):
        return False
    
    # Calculate the actual travel cost from the tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if calculated total cost matches given total cost
    if not math.isclose(total_cost, actual_cost, rel_tol=1e-2):
        return False
    
    return True

class TestKTPSolution(unittest.TestCase):
    def test_verify_solution(self):
        cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
        total_cost = 235.38
        
        result = verify_solution(cities, tour, total_cost)
        self.assertTrue(result)

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)