import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour_solution(cities_coordinates, tour, total_cost_calculated):
    try:
        # Requirement 1 and 4 - Starts and ends at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return False
        
        # Requirement 2 - Visits other cities exactly once
        cities_visited = set(tour[1:-1])
        if len(cities_visited) != len(cities_coordinates) - 1 or len(tour[1:-1]) != len(cities_coordinates) - 1:
            return False
        
        # Requirement 5 - Check total travel cost
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_dataistance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
        if not math.isclose(total_cost, total_cost_calculated, rel_tol=1e-5):
            return False
        
        # If all checks passed
        return True
    except Exception as e:
        return False

class TestTSPSolution(unittest.TestCase):
    def test_tour_validation(self):
        cities_coordinates = [
            (53, 68),  # depot city 0
            (75, 11),  # city 1
            (91, 95),  # city 2
            (22, 80),  # city 3
            (18, 63),  # city 4
            (54, 91),  # city 5
            (70, 14),  # city 6
            (97, 44),  # city 7
            (17, 69),  # city 8
            (95, 89)   # city 9
        ]
        # Mimic a tour and total cost as potentially outputted by a solution
        tour = [0, 1, 6, 7, 2, 9, 5, 3, 4, 8, 0]
        total_cost = sum([
            euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
            for i in range(len(tour)-1)
        ])
        
        # Check output correctness
        result = validate_tour_solution(cities_coordinates, tour, total_cost)
        if result:
            print("CORRECT")
        else:
            print("FAIL")

unittest.main(argv=[''], verbosity=2, exit=False)