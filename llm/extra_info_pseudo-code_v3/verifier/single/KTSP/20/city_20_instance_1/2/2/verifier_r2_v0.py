import unittest
import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTourSolution(unittest.TestCase):
    def test_tour_constraints(self):
        cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 
            4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82), 
            8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 
            12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 
            16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        
        tour = [0, 6, 9, 7, 5, 14, 0]
        reported_cost = 135.57
        
        # Verify the tour starts and ends at the depot city 0
        self.assertEqual(tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city 0")
        
        # Verify that exactly 7 cities are visited including depot
        self.assertEqual(len(tour), 7, "Tour should visit exactly 7 cities")
        
        # Calculate the total travel cost and check it
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

        # Check if calculated total cost matches the reported cost within reasonable floating point precision
        self.assertAlmostEqual(total_cost, reported_cost, places=2, msg="Calculated travel cost should match reported cost")
        
        # Output result based on test outcomes
        if len(tour) == 7 and tour[0] == tour[-1] and math.isclose(total_cost, reported_cost, rel_tol=1e-2):
            print("CORRECT")
        else:
            print("FAIL")

# Running the test
unittest.main(argv=[''], verbosity=2, exit=False)