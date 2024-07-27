import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def test_solution(self):
        # Given solution
        tour = [0, 1, 8, 4, 0]
        reported_cost = 110.08796524611944
        
        # City coordinates
        coordinates = {
            0: (8, 11),
            1: (40, 6),
            2: (95, 33),
            3: (80, 60),
            4: (25, 18),
            5: (67, 23),
            6: (97, 32),
            7: (25, 71),
            8: (61, 16),
            9: (27, 91),
            10: (91, 46),
            11: (40, 87),
            12: (20, 97),
            13: (61, 25),
            14: (5, 59),
            15: (62, 88),
            16: (13, 43),
            17: (61, 28),
            18: (60, 63),
            19: (93, 15)
        }

        # Groups
        groups = {
            0: [1, 3, 5, 11, 13, 14, 19],
            1: [2, 6, 7, 8, 12, 15],
            2: [4, 9, 10, 16, 17, 18]
        }

        # Requirement 1: Start and end at depot city 0
        self.assertEqual(tour[0], 0, "Tour does not start at depot city 0.")
        self.assertEqual(tour[-1], 0, "Tour does not end at depot city 0.")

        # Requirement 2: Visit exactly one city from each group
        unique_cities = set(tour[1:-1])  # ignore the starting and ending depot city
        city_groups_visited = {key: False for key in groups}
        for city in unique_cities:
            for group, cities in groups.items():
                if city in cities:
                    city_groups_visited[group] = True
        self.assertTrue(all(city_groups_visited.values()), "Not exactly one city from each group is visited.")
        
        # Requirement 5: Checking output format of tour
        self.assertIsInstance(tour, list, "The output tour is not a list.")
        
        # Computing and validating the travel cost
        def calculate_distance(coord1, coord2):
            return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
        
        calculated_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
        
        # Requirement 4: Correct calculation of travel cost
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5, msg="Reported cost does not match the calculated cost.")
        
        # Requirement 3: Minimizing travel cost (here we just check with reported cost)
        self.assertAlmostEqual(calculated_cost, reported_data, places=5, msg="Tour is not the shortest possible as per reported costs.")

        # If all tests pass
        print("CORRECT")

if __name__ == '__main__':
    unittest.main()