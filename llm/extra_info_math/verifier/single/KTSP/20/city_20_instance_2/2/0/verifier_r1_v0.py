import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Cities coordinates from the task
        self.cities = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
            5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
            10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
            15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
        }
        # Given tour solution and its cost
        self.given_tour = [0, 12, 15, 13, 18, 7, 11, 19, 16, 14, 0]
        self.given_cost = 175.48
    
    def test_tour_start_end_at_depot(self):
        # Test if the tour starts and ends at depot city 0
        self.assertEqual(self.given_tour[0], 0)
        self.assertEqual(self.given_tour[-1], 0)

    def test_tour_length(self):
        # Test if exactly 10 cities are visited, including the depot city
        self.assertEqual(len(set(self.given_tour)), 10)

    def test_tour_cost(self):
        # Calculate the total distance of the given tour
        total_distance = 0
        for i in range(len(self.given_tour) - 1):
            city_a = self.given_tour[i]
            city_b = self.given_tour[i + 1]
            total_distance += euclidean_distance(self.cities[city_a], self.cities[city_b])
        
        # Test if the total cost matches the given cost
        self.assertAlmostEqual(total_distance, self.given_cost, places=2)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)