import unittest
from math import sqrt

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_distance += sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance

class TestRobotTour(unittest.TestCase):
    
    def setUp(self):
        self.cities = {
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
        self.groups = [
            [3, 6],
            [5, 8],
            [4, 9],
            [1, 7],
            [2]
        ]
        self.solution_tour = [0, 3, 8, 4, 7, 2, 0]
        self.reported_cost = 313.11087320137085
    
    def test_requirement1(self):
        # Checking if the tour starts and ends at the depot city 0.
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
    
    def test_requirement2(self):
        # Checking if exactly one city from each group is visited.
        visited = {}
        for city in self.solution_tour[1:-1]:
            for idx, group in enumerate(self.groups):
                if city in group:
                    visited[idx] = visited.get(idx, 0) + 1
                    break
        
        # Verifying one city from each group has been visited
        for group_count in visited.values():
            self.assertEqual(group_count, 1)
        self.assertEqual(len(visited), len(self.groups))
    
    def test_requirement3(self):
        # All cities are unique, Ensuring connectivity is whatever route is given
        for i in range(len(self.solution_tour) - 1):
            self.assertIn(self.solution_tour[i], self.cities)
            self.assertIn(self.solution_tour[i + 1], self.cities)

    def test_requirement4(self):
        # Tour matches exactly as per requirement format including start and end at city 0
        self.assertListEqual(self.solution_tour, [0, 3, 8, 4, 7, 2, 0])
  
    def test_requirement5(self):
        # Calculate total travel distance
        calculated_distance = calculate_total_distance(self.solution_tour, self.cities)
        self.assertAlmostEqual(calculated_distance, self.reported_cost)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRobotTour))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")