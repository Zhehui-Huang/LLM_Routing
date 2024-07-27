import unittest
import math

# Define the coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define the groups of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Function to calculate Euclidean distance between two cities given their indices
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTourSolution(unittest.TestCase):
    def test_tour(self):
        tour = [0, 5, 10, 4, 11, 0]
        provided_total_cost = 184.24

        # Check that the tour starts and ends at the depot
        self.assertEqual(tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city 0")
        
        # Check that exactly one city from each group is visited
        visited_groups = set()
        for city in tour[1:-1]:  # Skip the first and last city (depot)
            for group, group_cities in groups.items():
                if city in group_cities:
                    visited_groups.add(group)
                    break
        self.assertEqual(len(visited_groups), 4, "Should visit one city from each group")
        
        # Calculate the total travel cost and compare with the provided total cost
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(calculated_cost, provided_total_cost, places=2, msg="Calculated total cost does not match provided cost")
        
        # Check correctness of outputs
        if len(visited_groups) == 4 and tour[0] == 0 and tour[-1] == 0 and round(calculated_cost, 2) == provided_total_cost:
            print("CORRECT")
        else:
            print("FAIL")

# Run tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)