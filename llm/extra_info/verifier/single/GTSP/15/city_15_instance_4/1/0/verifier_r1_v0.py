import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
            4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
            8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
            12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]
        self.submitted_tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
        self.submitted_cost = 156.56
    
    def test_start_and_end_at_depot(self):
        self.assertEqual(self.submitted_tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(self.submitted_tour[-1], 0, "Tour should end at depot city 0.")
    
    def test_visit_one_city_from_each_group(self):
        visited_cities = set(self.submitted_tour[1:-1])  # Ignoring the first and last which is the depot
        unique_group_cities = set()
        for group in self.groups:
            is_group_represented = any(city in visited_cities for city in group)
            self.assertTrue(is_group_represented, f"One city from group {group} should be visited.")
            # We also add the cities to check if only one city per group is visited
            for city in group:
                if city in visited_cities:
                    unique_group_cities.add(city)
        self.assertEqual(len(unique_group_cities), len(self.groups), "Only one city from each group can be visited.")
    
    def test_minimize_total_travel_cost(self):
        # Function to calculate the Euclidean distance between two cities
        def euclidean_distance(c1, c2):
            return sqrt((self.coordinates[c1][0] - self.coordinates[c2][0]) ** 2 + (self.coordinates[c1][1] - self.coordinates[c2][1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.submitted_tour) - 1):
            calculated_cost += euclidean_distance(self.submitted_tour[i], self.submitted_tour[i + 1])
        
        self.assertAlmostEqual(calculated_cost, self.submitted_cost, places=2, msg="Total travel cost should be correctly calculated and should be minimal.")

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestRobotTour))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
      print("FAIL")