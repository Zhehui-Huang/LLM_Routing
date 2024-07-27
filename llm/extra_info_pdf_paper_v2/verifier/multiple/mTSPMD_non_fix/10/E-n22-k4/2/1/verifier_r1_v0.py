import unittest
import math

# Define the class for the unit tests
class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
            4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
            8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
            12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
            16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
            20: (155, 185), 21: (139, 182)
        }
        
        self.tours = {
            0: [0, 4, 3, 1, 2, 5],
            1: [0, 9, 7, 6, 8, 10],
            2: [0, 11, 13, 14, 12, 15],
            3: [0, 16, 18, 20, 17, 19, 21]
        }

        self.costs = {
            0: 89.91,
            1: 66.79,
            2: 83.90,
            3: 90.27
        }

        self.expected_overall_cost = 330.87
    
    def test_tour_starts_with_depot(self):
        for robot, tour in self.tours.items():
            self.assertEqual(tour[0], 0, "Tours should start at depot city 0")
    
    def test_tour_unique_visit(self):
        all_visited = set()
        for tour in self.tours.values():
            all_visited.update(tour)
            self.assertEqual(len(set(tour)), len(tour), "Each city in a tour must be visited only once")
        self.assertEqual(len(all_visited), len(self.cities), "Each city must be visited exactly once")
    
    def test_tour_cost_calculation(self):
        def calculate_euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
        
        for robot, tour in self.tours.items():
            computed_cost = 0
            for i in range(len(tour) - 1):
                computed_cost += calculate_euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            self.assertAlmostEqual(computed_cost, self.costs[robot], delta=0.01, msg=f"Cost for Robot {robot} mismatch")
    
    def test_total_cost(self):
        total_cost = sum(self.costs.values())
        self.assertAlmostEqual(total_cost, self.expected_overall_cost, delta=0.01, msg="Overall cost mismatch")

# Execute the test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
result = unittest.TextTestRunner(verbosity=2).run(suite)

# Check if the tests have passed
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")