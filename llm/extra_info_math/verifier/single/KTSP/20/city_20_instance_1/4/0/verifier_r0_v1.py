import unittest
import math

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Test class
class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (14, 77),
            6: (4, 56),
            2: (19, 38),
            13: (26, 29),
            8: (37, 28),
            9: (27, 45),
            14: (21, 79),
        }
        # Provided solution tour
        self.tour = [0, 6, 2, 13, 8, 9, 14, 0]
        # Provided total travel cost
        self.provided_cost = 130.67

    def test_tour_requirements(self):
        # Check if the tour starts and ends at the depot and if exactly 7 cities are in the tour
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        self.assertEqual(len(set(self.tour)), 7, "Tour should include exactly 7 distinct cities including the depot.")

    def test_travel_cost(self):
        # Calculate the total travel cost
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            total_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        
        # Compare calculated cost with provided cost
        self.assertAlmostEqual(total_cost, self.provided_cost, delta=0.01, msg="Calculated travel cost does not match the provided cost.")

# Running the tests
if __name__ == '__main__':
    unittest.main()