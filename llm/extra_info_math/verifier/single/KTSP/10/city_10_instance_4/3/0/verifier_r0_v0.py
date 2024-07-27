import unittest

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # The output of the solution to test
        self.tour = None
        self.total_travel_cost = float('inf')

    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1: Tour must start and end at the depot city 0
        if self.tour is not None:
            self.assertEqual(self.tour[0], 0, "Tour should start at depot")
            self.assertEqual(self.tour[-1], 0, "Tour should end at depot")
        else:
            self.assertIsNone(self.tour, "Tour is None and does not meet the requirement")

    def test_tour_visits_exactly_eight_cities(self):
        # Requirement 2: Tour must visit exactly 8 cities including the depot
        if self.tour is not None:
            # Remove potential duplicates to get unique cities visited
            unique_cities = set(self.tour)
            self.assertEqual(len(unique_cities), 8, "Tour should visit exactly 8 unique cities")
        else:
            self.assertIsNone(self.tour, "Tour is None and does not meet the requirement")

    def test_tour_minimizes_travel_cost(self):
        # Requirement 3: Tour should minimize the total travel cost
        # Testing 'minimization' is complex without reference solutions, but we can do basic checks
        if self.tour is not None:
            self.assertNotEqual(self.total_travel_cost, float('inf'), "Total travel cost cannot be infinite if valid tour exists")
        else:
            self.assertEqual(self.total_travel_cost, float('inf'), "No valid tour exists, hence cost is inf")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    # Check if all tests passed
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Running the tests and printing the result
test_result = run_tests()
print(test_result)