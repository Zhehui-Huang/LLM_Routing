import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = {
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
        # Groups of cities
        self.groups = [
            [1, 3, 5, 11, 13, 14, 19],
            [2, 6, 7, 8, 12, 15],
            [4, 9, 10, 16, 17, 18]
        ]
        # Given output
        self.tour = [0, 1, 8, 4, 0]
        self.reported_cost = 110.08796524611944

    def test_tour_requirements(self):
        # Test start and end at the depot
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city 0.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city 0.")
        
        # Test visit exactly one city from each group 
        visited_cities = set(self.tour[1:-1])  # visited cities excluding the depot
        visited_groups = [any(city in group for city in visited_cities) for group in self.groups]
        self.assertTrue(all(visited_groups),
                        "Tour does not visit exactly one city from each group.")
        
        # Test cost calculation
        def calculate_distance(coord1, coord2):
            return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
        
        calculated_cost = sum(calculate_comp_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i+1]])
                               for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5,
                               msg="Calculated cost does not match reported cost.")

# Running the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTourSolution))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()