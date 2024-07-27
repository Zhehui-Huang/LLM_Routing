import unittest
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                   coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
    return cost

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        # Provided coordinates
        coordinates = [
            (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
            (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
            (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
        ]
        
        # City groups
        group_0 = [1, 3, 5, 11, 13, 14, 19]
        group_1 = [2, 6, 7, 8, 12, 15]
        group_2 = [4, 9, 10, 16, 17, 18]
        
        # Solution given
        tour = [0, 1, 8, 4, 0]
        reported_cost = 110.08796524611944
        
        # Test depot start and end
        self.assertEqual(tour[0], 0, "Tour should start at the depot")
        self.assertEqual(tour[-1], 0, "Tour should end at the depot")

        # Test exactly one city from each group
        self.assertIn(tour[1], group_0, "Should visit exactly one city from group 0")
        self.assertIn(tour[2], group_1, "Should visit exactly one city from group 1")
        self.assertIn(tour[3], group_2, "Should visit exactly one city from group 2")
        
        # Correct cities and index range
        self.assertTrue(all(city in range(20) for city in tour), "Tour should only include valid city indices")
        
        # Test cost calculation
        calculated_cost = calculate_total_travel_cost(tour, coordinates)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5, msg="Calculated cost does not match reported cost")
        
        # If all tests pass, print "CORRECT"
        print("CORRECT")

# Run the tests
unittest.main(argv=[''], exit=False)