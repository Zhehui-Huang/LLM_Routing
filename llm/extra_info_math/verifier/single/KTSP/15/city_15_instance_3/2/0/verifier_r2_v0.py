import unittest
from math import sqrt

# Define the cities' coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Provided solution
solution_tour = [0, 14, 1, 4, 9, 5, 10, 13, 8, 6, 0]
solution_cost = 179.51184908603798

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_tour_start_end(self):
        # Requirement 1: Starts and ends at city 0
        self.assertEqual(solution_tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(solution_tour[-1], 0, "Tour does not end at city 0")
    
    def test_tour_length(self):
        # Requirement 2: Exactly 10 cities visited
        self.assertEqual(len(set(solution_tour)), 10, "Tour does not visit exactly 10 unique cities")
    
    def test_tour_cost(self):
        # Calculate the travel cost based on the solution tour
        tour_cost = 0
        for i in range(len(solution_tour) - 1):
            tour_cost += calculate_distance(solution_tour[i], solution_tour[i+1])
        
        # Requirement 3: Check if the calculated cost matches the provided cost
        self.assertAlmostEqual(tour_cost, solution_cost, places=5, msg="Calculated tour cost does not match the reported cost")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)