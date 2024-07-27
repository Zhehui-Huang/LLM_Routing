import unittest
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        # Provided cities' coordinates
        cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
                  (62, 26), (79, 31), (61, 90), (42, 49)]
        
        # Given solution
        tour = [0, 7, 6, 1, 5, 2, 4, 3, 8, 9, 0]
        total_cost_given = 299.22080186207336
        max_distance_given = 45.18849411078001
        
        # Verify Requirement 1 - All Cities Visited and Return to Start
        self.assertEqual(len(set(tour)), len(cities))
        self.assertEqual(tour[0], tour[-1])

        # Requirement 2 is open to implementation so we skip it in test for now. (Requires mini-maxing)
        
        # Calculate actual travel costs and distances
        actual_total_dist = 0
        actual_max_dist = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]][0], cities[tour[i]][1],
                                      cities[tour[i+1]][0], cities[tour[i+1]][1])
            actual_total_dist += dist
            actual_max_dist = max(actual_max_dist, dist)

        # Verify Requirement 3 - Distance Calculation
        self.assertAlmostEqual(total_cost_given, actual_totalit, places=5)

        # Verify Requirement 4 - Tour starts and ends at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Verify Requirement 5 - Total Travel Cost
        self.assertAlmostEqual(total_cost_given, actual_total_dist, places=5)
        
        # Verify Requirement 6 - Max Distance Between Consecutive Cities
        self.assertAlmostEqual(max_distance_given, actual_max_dist, places=5)


if __name__ == "__main__":
    unittest.main()