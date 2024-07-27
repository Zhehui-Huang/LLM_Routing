import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # Provided solution
        tour = [0, 8, 5, 2, 6, 3, 0]
        total_travel_cost = 314.1864038066482
        
        # City coordinates
        coordinates = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        
        # Check if the tour starts and ends at the depot city
        self.assertEqual(tour[0], 0, "Tour should start at city 0.")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0.")
        
        # Check if exactly 6 cities are visited
        unique_cities = set(tour)
        self.assertEqual(len(unique_cities), 6, "Exactly 6 unique cities should be visited.")
        
        # Check if first and last city is the depot city
        self.assertEqual(tour[0], tour[-1], "Tour should start and end at the depot city.")
        
        # Calculate the total travel cost and compare
        calculated_cost = sum(sqrt((coordinates[tour[i]][0] - coordinates[tour[i+1]][0])**2 + 
                          (coordinates[tour[i]][1] - coordinates[tour[i+1]][1])**2) for i in range(len(tour) - 1))
        
        # Floating-point comparison might need a margin of error
        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=5, 
                               msg="Calculated travel cost should match provided total travel cost.")
        
        # Assert final output, if all tests pass
        if (len(unique_cities) == 6 and tour[0] == 0 and tour[-1] == 0 and
            abs(calculated_cost - total_travel_cost) < 1e-5):
            print("CORRECT")
        else:
            print("FAIL")

# Running the test suite
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)