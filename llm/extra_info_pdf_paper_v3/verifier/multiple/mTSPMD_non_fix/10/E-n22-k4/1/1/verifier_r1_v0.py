import unittest
import math

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided tours and costs
robot_tours = [
    [0, 21, 12, 5, 8, 0],
    [0, 15, 20, 16, 13, 0],
    [0, 9, 7, 4, 10, 0],
    [0, 6, 11, 19, 14, 0],
    [0, 18, 17, 0]
]
provided_costs = [149.92, 100.64, 114.01, 129.02, 68.16]

# Expected total cost
expected_total_cost = 561.75

class TestRobotTour(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        for tour in robot_tours:
            self.assertEqual(tour[0], 0)  # Start at depot city 0
            self.assertEqual(tour[-1], 0)  # End at a valid city (depot city 0)

    def test_all_cities_visited_exactly_once(self):
        all_visited = set()
        for tour in robot_tours:
            all_visited.update(tour[1:-1])  # Skip the depot city at start and end in counting
        self.assertEqual(len(all_visited), 21)  # 21 cities visited, excluding the extra start/end city
        
    def test_total_travel_costs(self):
        total_cost_calculated = 0
        for tour, provided_cost in zip(robot_tours, provided_costs):
            tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]])
                            for i in range(len(tour) - 1))
            total_cost_calculated += tour_cost
            self.assertAlmostEqual(tour_cost, provided_cost, places=2)
        
        self.assertAlmostEqual(total_cost_calculated, expected_total_cost, places=2)

if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestRobotTour))
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")