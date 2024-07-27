import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
                       (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
                       (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]
        
        # Provided tour
        self.tour = [7, 3, 12, 4, 1, 10, 9, 6, 2, 11, 8, 13, 5, 14, 0, 0]
        # Provided total cost
        self.provided_total_cost = 336.5878155857113
    
    def calculate_distance(self, city1, city2):
        # Euclidean distance calculation
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def test_tour_starts_and_ends_at_depot(self):
        # Check if the tour starts and ends at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_visit_each_city_exactly_once(self):
        # Check that all cities, except the depot city, are visited exactly once
        all_cities = list(range(1, 15))  # excluding city 0
        tour_without_depot = [city for city in self.tour if city != 0]
        self.assertCountEqual(all_cities, tour_without_depot)
    
    def test_total_travel_cost(self):
        # Calculate the total distance of the tour
        total_cost = sum(self.calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.provided_total_cost, places=5)
        
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the test
print(run_tests())