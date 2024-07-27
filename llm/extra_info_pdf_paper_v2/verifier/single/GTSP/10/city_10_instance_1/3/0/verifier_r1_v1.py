import unittest
from math import sqrt

# Define the city coordinates (index corresponds to city number)
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Define the city groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour_requirements(tour, total_cost):
    # Requirement 1: starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 4: Output the tour starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
        
    # Requirement 2: Visits exactly one city from each group
    visited = set(tour[1:-1])  # ignore starting and ending depot cities
    for group in groups:
        if not any(city in visited for city in group):
            return False

    # Requirement 3: Check if the total distance is calculated correctly
    calculated_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not abs(calculated_distance - total_cost) < 1e-5:
        return False

    return True

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_solution_validity(self):
        tour = [0, 9, 5, 3, 8, 0]
        total_cost = 169.9409598467532
        if verify_tour_requirements(tour, total_cost):
            print("CORRECT")
        else:
            print("FAIL")

# Execute the test directly without using unittest framework style
test_case = TestTravelingSalesmanSolution()
test_case.test_solution_validity()