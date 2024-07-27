import unittest
from math import sqrt

def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, total_cost_calculated):
    # Coordinates of all cities
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    if len(coordinates) != 20:
        return False
    
    if tour[0] != 0 or tour[-1] != 0:
        return False

    if sorted(tour[1:-1]) != list(range(1, 20)):
        return False

    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    return abs(total_cost_calculated - total_distance) < 1e-5

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        tour = [0, 19, 8, 10, 6, 3, 4, 15, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
        total_cost = 417.6330718348164
        
        result = verify_tour(tour, total_cost)
        self.assertTrue(result, "The tour or total travel cost is incorrect.")

# Running the test
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
result = unittest.TextTestRunner().run(suite)

# Output result based on test outcomes
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")