import unittest
import math

class TestTourSolution(unittest.TestCase):
    def test_tour_requirements(self):
        # Provided solution details
        tour = [0, 8, 14, 4, 1, 10, 11, 16, 15, 5, 2, 13, 19, 0]
        calculated_cost = 371.17
        
        # Known city coordinates
        coordinates = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
            4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
            8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
            12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
            16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }

        # Requirement 1: 13 cities including the depot
        self.assertEqual(len(set(tour)), 13)

        # Requirement 2: Start and end at the depot city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Requirement 4: Each city visited once
        self.assertEqual(len(tour), len(set(tour))+1)  # +1 because the depot appears twice

        # Compute the travel cost
        def euclidean_distance(c1, c2):
            return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
        
        actual_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
        
        # Requirement 3: actual cost should be approximately equal to calculated cost
        self.assertAlmostEqual(actual_cost, calculated_cost, places=2, msg="Cost does not match. Expected ~{}".format(calculated_cost))
        
        # Assert the cities do not exceed the total count of 20
        # Requirement 5
        self.assertTrue(max(tour) < 20)

test_suite = unittest.TestSuite()
test_suite.addTest(TestTourSolution("test_tour_requirements"))

runner = unittest.TextTestRunner()
result = runner.run(test_suite)

# If all tests pass, print CORRECT else FAIL
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")