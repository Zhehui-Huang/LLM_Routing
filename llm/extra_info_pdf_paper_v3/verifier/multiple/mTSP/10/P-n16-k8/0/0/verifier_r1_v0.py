import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Provided city coordinates
        self.cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
                       (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
                       (43, 67), (58, 48), (58, 27), (37, 69)]
        
        # Provided solution
        self.robot_tours = [
            [0, 1, 9, 0], 
            [0, 2, 10, 0],
            [0, 3, 11, 0],
            [0, 4, 12, 0],
            [0, 5, 13, 0],
            [0, 6, 14, 0],
            [0, 7, 15, 0],
            [0, 8, 0]
        ]
        
        # Provided costs
        self.robot_costs = [72.88, 52.46, 86.04, 64.99, 68.36, 64.17, 83.62, 64.90]
        self.total_cost_reported = 557.42
        
    def test_tours_start_end_at_depot(self):
        # Requirement 1
        for tour in self.robot_tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
    
    def test_unique_city_visit(self):
        # Requirement 2
        visited = set()
        for tour in self.robot_tours:
            for city in tour[1:-1]:  # Exclude the depot city at start and end
                self.assertNotIn(city, visited)
                visited.add(city)
        self.assertEqual(len(visited), 15)  # 15 cities to visit, excluding depot city
    
    def test_calculate_travel_costs(self):
        # Requirement 5
        for tour, reported_cost in zip(self.robot_tours, self.robot_costs):
            calculated_cost = 0
            for i in range(len(tour) - 1):
                calculated_cost += calculate_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            self.assertAlmostEqual(calculated_cost, reported_company, places=2)
    
    def test_total_travel_cost(self):
        # Requirement 6
        calculated_total_cost = sum(self.robot_costs)
        self.assertAlmostEqual(calculated_total_cost, self.total_cost_reported, places=2)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
unittest.TextTestRunner().run(suite)