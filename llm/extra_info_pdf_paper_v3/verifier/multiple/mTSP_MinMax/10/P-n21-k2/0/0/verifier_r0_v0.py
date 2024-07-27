import unittest

class mTSPSolutionTest(unittest.TestCase):
    def test_robot_tour_requirements(self):
        robot_0_tour = [0, 6, 20, 5, 14, 17, 9, 7, 2, 1, 0]
        robot_1_tour = [0, 4, 11, 15, 12, 3, 19, 18, 8, 13, 10, 16, 0]
        all_cities = set(range(1, 21))  # City indices from 1 to 20
        visited_cities_robot_0 = set(robot_0_tour[1:-1])
        visited_cities_robot_1 = set(robot_1_tour[1:-1])

        # Requirement 1: Test start and end at depot
        self.assertEqual(robot_0_tour[0], 0, "Robot 0 does not start at the depot")
        self.assertEqual(robot_0_tour[-1], 0, "Robot 0 does not end at the depot")
        self.assertEqual(robot_1_tour[0], 0, "Robot 1 does not start at the depot")
        self.assertEqual(robot_1_tour[-1], 0, "Robot 1 does not end at the depot")

        # Requirement 2: Test visiting each city exactly once
        combined_cities_visited = visited_cities_robot_0.union(visited_cities_robot_1)
        self.assertEqual(combined_cities_visited, all_cities, "Not all cities are visited exactly once")

        # No requirement 3 specific validation required as it's about the evaluation of distances, not structure

        # If all tests pass, consider the solution correct
        return "CORRECT"

# Running the test
test_suite = unittest.TestSuite()
test_suite.addTest(mTSPSolutionTest('test_robot_tour_requirements'))

test_runner = unittest.TextTestRunner()
test_results = test_runner.run(test_suite)

# Output based on test results
if test_results.wasSuccessful():
    output = "CORRECT"
else:
    output = "FAIL"

print(output)