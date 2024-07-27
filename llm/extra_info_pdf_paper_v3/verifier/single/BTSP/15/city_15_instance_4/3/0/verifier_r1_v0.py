import unittest
from math import sqrt

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # The cities coordinates
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        
        # Provided tour including the depot at start and end
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.reported_total_cost = 337.8447016788252
        self.reported_max_leg_distance = 60.67124524847005

    def test_start_and_end_at_depot(self):
        # Check the starting and ending location is the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Check every city visited exactly once apart from the depot which should be visited twice
        tour_set = set(self.tour)
        self.assertEqual(len(tour_set), 15)  # Should be 15 unique items including depot
        self.assertEqual(self.tour.count(0), 2)  # Depo must appear twice

    def test_correct_travel_cost_and_max_leg_distance(self):
        total_cost = 0
        max_leg_distance = 0
        
        def euclidean_distance(p1, p2):
            return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        for i in range(1, len(self.tour)):
            city1 = self.tour[i - 1]
            city2 = self.tour[i]
            dist = euclidean_distance(self.cities[city1], self.cities[city2])
            total_cost += dist
            max_leg_distance = max(max_leg_distance, dist)
            
        self.assertAlmostEqual(total_cost, self.reported_total_cost)
        self.assertAlmostEqual(max_leg_distance, self.reported_max_leg_distance)

if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    # Output appropriate result based on unit test pass or fail
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
    	print("FAIL")