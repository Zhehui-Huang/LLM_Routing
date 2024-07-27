import unittest
from math import sqrt

# Data for cities coordinates: (city_index: (x, y))
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

class TestKTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Provided solution
        tour = [0, 1, 10, 8, 0]
        reported_cost = 90.54

        # Verify the tour starts and ends at city 0
        self.assertEqual(tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(tour[-1], 0, "Tour does not end at the depot")
        
        # Verify exactly 4 cities are visited
        self.assertEqual(len(set(tour)), 4, "Tour does not visit exactly 4 distinct cities")
        
        # Verify calculation of total travel distance and compare with reported
        calculated_cost = sum(euclidean _distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Allowing for a small margin of error in floating point calculations
        self.assertAlmostEqual(calculated_cost, reported_cost, places=2, msg="Calculated travel cost does not match reported")

        # Since all tests pass, output "CORRECT"
        print("CORRECT")

# Run the unit test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)