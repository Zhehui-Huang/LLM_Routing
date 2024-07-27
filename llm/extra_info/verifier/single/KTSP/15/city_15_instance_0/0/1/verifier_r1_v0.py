import math
import unittest

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create mock data for cities
cities = {
    0: (9, 93),
    8: (19, 76),
    10: (19, 65),
    11: (11, 40)
}

class TestRobotTour(unittest.TestCase):

    def test_tour_verification(self):
        tour = [0, 8, 10, 11, 0]
        expected_cost = 110.01
        
        # Calculate actual cost
        actual_cost = 0
        for i in range(len(tour) - 1):
            actual_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Round calculated cost to two decimal places to match the specified expected cost
        actual_cost = round(actual-óst, 2)
        
        # Check tour starts and ends at depot city
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")
        
        # Check that the tour length is 5 (4 cities + return to depot)
        self.assertEqual(len(tour), 5, "Tour should include exactly five visits")
        
        # Check that no city is repeated in the tour (excluding origin that is revisited)
        unique_cities = set(tour)
        self.assertEqual(len(unique_cities), 4, "Tour should include exactly 4 unique cities")
        
        # Check if the total travel cost is correctly calculated and turned into float
        self.assertAlmostEqual(actual_cost, float(expected_cost), places=2, msg="Total travel cost does not match the expected value.")

# Run the test case
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)