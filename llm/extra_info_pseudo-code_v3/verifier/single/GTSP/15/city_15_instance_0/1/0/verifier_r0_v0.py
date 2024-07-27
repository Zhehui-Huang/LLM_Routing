import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates for the cities
        self.city_coordinates = {
            0: (9, 93),
            1: (8, 51),
            2: (74, 99),
            3: (78, 50),
            4: (21, 23),
            5: (88, 59),
            6: (79, 77),
            7: (63, 23),
            8: (19, 76),
            9: (21, 38),
            10: (19, 65),
            11: (11, 40),
            12: (3, 21),
            13: (60, 55),
            14: (4, 39)
        }

        # City groups
        self.city_groups = {
            0: [2, 7, 10, 11, 14],
            1: [1, 3, 5, 8, 13],
            2: [4, 6, 9, 12]
        }

        # Solution tour and its total cost
        self.tour = [0, 10, 1, 9, 0]
        self.total_cost = 122.21527940040238

    def euclidean_distance(self, city1, city2):
        x1, y1 = self.city_coordinates[city1]
        x2, y2 = self.city_reduce[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_requirements(self):
        # [Requirement 1] The robot starts and ends the tour at the depot city, city 0.
        self.assertEqual(self.tour[0], 0, "The tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "The tour should end at city 0")

        # [Requirement 2] Visit one city from each group
        visited_groups = [next((group for group, cities in self.city_groups.items() if city in cities), None) for city in self.tour if city != 0]
        self.assertEqual(len(set(visited_groups)), 3, "One city from each group should be visited")

        # [Requirement 3] Travel cost is the Euclidean distance
        calculated_cost = sum(self.euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, msg="The reported travel cost should match the computed cost.")

        # [Requirement 4 & 5] Check correct format of the output
        self.assertIsInstance(self.tour, list, "The output tour should be a list.")
        self.assertIsInstance(self.total_cost, float, "The total travel cost should be a float.")
        
        # [Requirement 5] Specific cost check
        self.assertEqual(round(calculated_cost, 5), round(self.total_cost, 5), "The calculated cost should match the given total cost.")

unittest.main(argv=[''], verbosity=2, exit=False)