import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Cities (indices correspond to city codes)
        cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }

        # Provided solution
        tour = [0, 4, 1, 7, 3, 8, 0]
        reported_cost = 128.73

        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")

        # Check if 7 cities are visited (including the depot)
        self.assertEqual(len(set(tour)), 7, "Exactly 7 cities including the depot should be visited")

        # Check the actual cost of the tour
        actual_cost = 0
        for i in range(len(tour) - 1):
            actual_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

        # Compare the calculated cost with the reported cost
        self.assertAlmostEqual(actual_cost, reported_cost, places=2, msg="Reported travel cost should match the calculated cost")

        # Extra check if it includes only cities from the set of 10 cities
        self.assertTrue(all(city in cities for city in tour), "Tour should only include the specified cities")

def run_tests():
    suite = unittest.TestSuite()
    # Adding test cases to the suite
    suite.addTest(TestTSPSolution('test_solution'))
    
    # Running the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Check for any failures or errors in the tests
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()