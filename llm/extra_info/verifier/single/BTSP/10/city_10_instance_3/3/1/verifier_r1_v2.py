import unittest
import math

def euclidean_distance(p1: tuple, p2: tuple) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def validate_solution(tour: list, cities: list) -> str:
    # [Requirement 1] Start and end at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once
    if sorted(tour[:-1]) != list(range(len(cities))):
        return "FAIL"
    
    # [Requirement 3] Check distances between consecutive cities
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        if i > 0 and dist > max_distance:
            max_distance = dist

    return "CORRECT"

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        tour = [0, 1, 2, 7, 3, 8, 4, 6, 9, 5, 0]
        cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
        
        result = validate_solution(tour, cities)
        # Directly print "CORRECT" or "FAIL" based on validation.
        print(result)

# Running the unit tests
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)