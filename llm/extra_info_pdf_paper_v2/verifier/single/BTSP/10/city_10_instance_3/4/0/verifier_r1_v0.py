import unittest
import math

class TestBTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities in the format city_index: (x, y)
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        # Provided tour output
        self.tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
        self.reported_total_cost = 345.92
        self.reported_max_distance = 68.26

    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 1 & 4
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")
    
    def test_visit_each_city_once(self):
        # Requirement 2
        visited = set(self.tour)
        self.assertEqual(len(visited), 10, "Should visit each city exactly once excluding the return")
    
    def test_total_travel_cost(self):
        # Requirement 5
        total_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            total_cost += distance
        
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2, msg="Total travel cost should match the reported value")
    
    def test_max_distance_between_cities(self):
        # Requirement 3 & 6
        max_distance = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance > max_distance:
                max_distance = distance
        
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=2, msg="Maximum distance between consecutive cities should match the reported value")

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBTSPSolution))
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")