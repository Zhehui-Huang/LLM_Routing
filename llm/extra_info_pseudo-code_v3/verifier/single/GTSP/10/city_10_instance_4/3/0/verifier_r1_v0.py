import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        
        city_groups = [
            [1, 4],
            [2, 6],
            [7],
            [5],
            [9],
            [8],
            [3]
        ]
        
        proposed_tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]

        # Requirement 1: Check start and end at Depot
        self.assertEqual(proposed_tour[0], 0)
        self.assertEqual(proposed_tour[-1], 0)

        # Requirement 2: Check visiting exactly one city from each group
        visited_groups = [[] for _ in city_groups]
        for i, group in enumerate(city_groups):
            for city in group:
                if city in proposed_tour:
                    visited_groups[i].append(city)
        all_visited = all(len(visited) == 1 for visited in visited_groups)
        self.assertTrue(all_visited)

        # Requirement 3: Check calculated total distance
        calculated_dist = sum(euclidean_distance(
            cities[proposed_tour[i]][0],
            cities[proposed_tour[i]][1],
            cities[proposed_tour[i+1]][0],
            cities[proposed_tour[i+1]][1]) for i in range(len(proposed_tour) - 1))
        
        provided_distance = 279.02
        # Using small tolerance since float calculations can be slightly different depending on system and method
        self.assertAlmostEqual(calculated_dist, provided_distance, places=2)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_robot_tour'))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")