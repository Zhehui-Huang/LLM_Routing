import unittest
import math

# Cities and their coordinates
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

# City groups
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

class TestTourSolution(unittest.TestCase):
    def test_tour(self):
        tour = [0, 5, 10, 4, 11, 0]
        total_cost = 184.24
        
        # Check tour starts and ends at depot
        self.assertEqual(tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city 0")
        
        # Check if exactly one city from each group is visited
        visited_groups = set()
        for city in tour[1:-1]:  # Exclude the starting and ending depot
            for group, cities in groups.items():
                if city in cities:
                    visited_groups.add(group)
                    break
        self.assertEqual(len(visited_groups), 4, "Tour should visit one city from each group")
        
        # Compute the total travel cost and compare
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(tour[i], tour[i+1])
        self.assertAlmostEqual(calculated to tal_cost, total_cost, places=2, "Calculated total cost does not match provided cost")
        
        # Output result based on correctness
        if len(visited_groups) == 4 and tour[0] == 0 and tour[-1] == 0 and round(calculated_cost, 2) == total_cost:
            print("CORRECT")
        else:
choj            print("FAIL")

# Run tests
if __name__ == '__main__':
    unittest.main()