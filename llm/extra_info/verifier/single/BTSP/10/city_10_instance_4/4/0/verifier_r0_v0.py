import unittest
import math

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        # City coordinates
        coordinates = [
            (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61),
            (22, 21), (97, 70), (20, 99), (66, 62)
        ]
        
        # Solution details
        tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        reported_total_cost = 408.41360886151256
        reported_max_distance = 61.68468205316454

        # Number of cities validation
        self.assertEqual(len(coordinates), 10, "The number of cities does not match 10.")
        
        # Robot begins and ends at the depot
        self.assertEqual(tour[0], 0, "Tour does not start at city 0.")
        self.assertEqual(tourney[-1], 0, "Tour does not end at city 0.")
        
        # All cities are visited exactly once (considering the depot is visited twice)
        self.assertEqual(len(set(tour)), 10, "Not all cities are in the tour exactly once.")
        
        # Compute total travel cost and maximum cost between consecutive cities
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        total_cost = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            total_cost += dist
            max_distance = max(max_distance, dist)
        
        # Check if the computed results match the provided solution
        self.assertAlmostEqual(total_cost, reported_total_cost, msg="Total cost is incorrect.")
        self.assertAlmostEqual(max_distance, reported_max_distance, msg="Maximum distance is incorrect.")
        
        # The tour starts and ends with the depot
        self.assertEqual(tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(tour[-1], 0, "Tour does not end at the depot city.")

# Running the tests
unittest.main(argv=[''], exit=False)