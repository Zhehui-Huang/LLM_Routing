import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
            0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28), 
            5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
        }
        
        # Provided solution
        self.tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
        self.total_travel_cost = 345.92
        self.max_distance = 68.26
    
    def test_tour_validity(self):
        # Requirement 1: Starts and ends at depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
        # Requirement 2: Each city visited exactly once
        visited_cities = self.tour[1:-1]
        unique_cities = set(visited_cities)
        self.assertEqual(len(visited_cities), len(unique_cities))
        self.assertEqual(set(range(10)), unique_cities.union({0}))

    def test_distance_optimization(self):
        # Requirement 3: Minimize the longest distance between consecutive cities
        distances = []
        for i in range(len(self.tour) - 1):
            dist = euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
            distances.append(dist)
        
        # Check the maximum distance
        calculated_max_distance = max(distances)
        calculated_total_cost = sum(distances)
        
        # Test if the distance and cost values meet given ones (floating-point comparison tolerance)
        self.assertAlmostEqual(calculated_max_distance, self.max_distance, places=2)
        self.assertAlmostEqual(calculated_total_cost, self.total_travel_cost, places=2)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTour('test_tour_validity'))
    suite.addTest(TestRobotTour('test_distance_optimization'))
    
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()