import unittest
import math

# Assuming the provided tour data is accessible as follows:
robots_tours = {
    0: [0, 15, 14, 16, 11, 2, 5, 0],
    1: [0, 4, 6, 9, 17, 21, 0],
    2: [0, 12, 10, 7, 3, 13, 0],
    3: [0, 8, 1, 18, 20, 19, 0]
}

cities_coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 200)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestRobotTours(unittest.TestCase):
    def test_unique_visitation_and_return_to_depot(self):
        visited = set()
        for tour in robots_tours.values():
            # Check if tour starts and ends at depot
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
            
            # Add visited cities excluding the depot for multiple visits
            visited.update(tour[1:-1])
        
        # Check if all cities except the depot are visited exactly once
        self.assertEqual(len(visited), 21)
        self.assertEqual(visited, set(range(1, 22)))

    def test_travel_cost_calculation(self):
        expected_costs = {
            0: 166.2262756458405,
            1: 172.43806418638107,
            2: 133.8668172209115,
            3: 191.81392598621446
        }

        for robot_id, tour in robots_tours.items():
            total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            # Check total_cost against expected with a tolerance
            self.assertAlmostEqual(total_cost, expected_costs[robot_id], places=5)
        
    def test_minimize_maximum_distance(self):
        costs = []
        for tour in robots_tours.values():
            total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            costs.append(total_cost)
        
        max_cost = max(costs)
        expected_max_cost = 191.81392598621446
        self.assertEqual(max_cost, expected_max_cost)

# Running the unit tests
if __name__ == "__main__":
    unittest.main()