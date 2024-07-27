import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
            5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
            10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
        }
        self.tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]
        self.reported_cost = 340.65

    def test_requirement_1(self):
        # Requirement 1: Start and end at city 0
        self.assertEqual(self.tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at city 0")
    
    def test_requirement_2(self):
        # Requirement 2: Visit each city exactly once, except depot which is visited twice
        unique_cities = set(self.tour)
        # Remove the depot city and check if remaining cities are exactly once
        unique_cities.remove(0)
        self.assertEqual(len(unique_cities), 14)
        self.assertEqual(sorted(unique_cities), list(range(1, 15)))

    def test_requirement_3(self):
        # Requirement 3: Total travel cost is correctly calculated
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i + 1]
            total_cost += calculate_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, 
                               msg=f"Actual cost {total_form_cost} does not match reported cost {self.reported_cost}")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTSPSolution('test_requirement_1'))
    suite.addTest(TestTSPSolution('test_requirement_2'))
    suite.addTest(TestTSPSolution('test_requirement_3'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")