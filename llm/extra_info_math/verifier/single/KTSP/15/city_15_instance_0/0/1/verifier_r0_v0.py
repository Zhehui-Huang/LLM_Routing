import unittest
import math

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_distance

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Cities coordinates
        self.cities = [
            (9, 93),  # City 0 - Depot
            (8, 51),  # City 1
            (74, 99), # City 2
            (78, 50), # City 3
            (21, 23), # City 4
            (88, 59), # City 5
            (79, 77), # City 6
            (63, 23), # City 7
            (19, 76), # City 8
            (21, 38), # City 9
            (19, 65), # City 10
            (11, 40), # City 11
            (3, 21),  # City 12
            (60, 55), # City 13
            (4, 39)   # City 14
        ]
        self.tour = [0, 1, 10, 8, 0]
        self.expected_distance = 90.53947981328088
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_tour_total_distance(self):
        calculated_distance = calculate_total_distance(self.tour, self.cities)
        self.assertAlmostEqual(calculated_distance, self.expected_distance, places=5,
                               msg="Calculated distance does not match expected distance")

    def test_tour_includes_exactly_four_cities(self):
        self.assertEqual(len(set(self.tour)), 4, "Tour does not include exactly four cities")

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
         print("FAIL")