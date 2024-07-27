import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (84, 67),  # Depot city 0
            (74, 40),  # City 1
            (71, 13),  # City 2
            (74, 82),  # City 3
            (97, 28),  # City 4
            (0, 31),   # City 5
            (8, 62),   # City 6
            (74, 56),  # City 7
            (85, 71),  # City 8
            (6, 76)    # City 9
        ]
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.reported_total_cost = 315.56
        self.reported_max_dist = 78.52

    def test_visitation_completion(self):
        # Checking if every city except depot is visited exactly once
        tour_set = set(self.tour)
        self.assertEqual(tour_set, set(range(10)))  # Check set equality with all cities including the depot

    def test_tour_ends_at_depot(self):
        # Check if tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_distances(self):
        total_cost = 0
        max_distance = 0
        for i in range(len(self.tour) - 1):
            dist = euclidean_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i+1]])
            total_cost += dist
            max_distance = max(max_distance, dist)

        # Check if the computed total cost and max distance match the reported values
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2)
        self.assertAlmostEqual(max_distance, self.reported_max_dist, places=2)

    def test_correctness_of_solution(self):
        self.test_visitation_completion()
        self.test_tour_ends_at_depot()
        self.test_distances()
        print("CORRECT")
        
def run_TSP_tests():
    test_suite = unittest.TestSuite()
    # Adding each test
    test_suite.addTest(TestTSPSolution('test_visitation_completion'))
    test_suite.addTest(TestTSPSolution('test_tour_ends_at_depot'))
    test_suite.addTest(TestTSPSolution('test_distances'))

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    # Evaluate the test results
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

# Run test to validate solution
run_TSP_tests()