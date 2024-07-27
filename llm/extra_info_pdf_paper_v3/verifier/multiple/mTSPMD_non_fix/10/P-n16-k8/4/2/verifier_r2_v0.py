import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Cities locations: id -> (x, y)
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
        }
        
        # List of robot's tours
        self.tours = [
            [0, 6, 0], [0, 2, 7, 0], [0, 4, 11, 0], 
            [0, 6, 7, 0], [0, 8, 3, 0], [0, 10, 1, 0], 
            [0, 12, 15, 0], [0, 14, 5, 0]
        ]
        
        # Calculating total travel costs
        self.robot_travel_costs = []
        for tour in self.tours:
            cost = 0
            for i in range(len(tour)-1):
                src_id = tour[i]
                dest_id = tour[i+1]
                cost += calculate_euclidean_distance(self.cities[src_id][0], self.cities[src_id][1], 
                                                     self.cities[dest_id][0], self.cities[dest_id][1])
            self.robot_travel_costs.append(cost)

        self.total_travel_cost = sum(self.robot_travel_costs)
        
        # All the cities need to be visited
        self.all_cities_visited = set()
        for tour in self.tours:
            self.all_cities_visited.update(set(tour[1:-1]))
            
    def test_each_robot_begins_at_depot_zero(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0, "Robot does not start at depot city 0")

    def test_all_cities_visited_once(self):
        self.assertEqual(len(self.all_cities_visited), 16, "Not all cities are visited exactly once")

    def test_total_travel_cost(self):
        self.assertAlmostEqual(self.total_travel_cost, 67.49, "Total travel cost does not match expected result")
        
    def test_each_city_visited_exactly_once(self):
        city_visitation_frequency = {i: 0 for i in range(16)}
        for tour in self.tours:
            for city in tour[1:-1]:
                city_visitation_frequency[city] += 1
        self.assertEqual(all(v == 1 for v in city_visitation_frequency.values()), True, 
                         "Some cities are visited more than once or not at all")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTours("test_each_robot_begins_at_depot_zero"))
    suite.addTest(TestRobotTours("test_all_cities_visited_once"))
    suite.addTest(TestRobotTours("test_total_travel_cost"))
    suite.addTest(TestRobotTours("test_each_city_visited_exactly_once"))
    
    # Running the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Call the test function and print result.
print(run_tests())