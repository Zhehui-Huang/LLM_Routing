import unittest
import math

# Provided city coordinates and tours data
cities_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 200)
}

robots_tours = {
    0: [0, 15, 14, 16, 11, 2, 5, 0],
    1: [0, 4, 6, 9, 17, 21, 0],
    2: [0, 12, 10, 7, 3, 13, 0],
    3: [0, 8, 1, 18, 20, 19, 0]
}

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestRobotTours(unittest.TestCase):
    def test_unique_visitation_and_return_to_depot(self):
        visited = set()
        all_tours = sum(robots_tours.values(), [])
        for city in all_tours[1:-1]:  # Ignore the depot city at start/end
            visited.add(city)
        self.assertEqual(len(visited), 21)
        self.assertTrue(all(city in range(1, 22) for city in visited))

    def test_travel_cost_calculation(self):
        recalculated_costs = {}
        for robot_id, tour in robots_tours.items():
            total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            recalculated_costs[robot_id] = total_cost
            print(f"Robot {robot_id} recalculated travel cost: {total_cost}")
        
        # Display for manual verification with expected values if available
        expected_costs = {  # Original expected costs (if correctly provided)
            0: 166.2262756458405,
            1: 172.43806418638107,
            2: 133.8668172209115,
            3: 191.81392598621446
        }

        for robot_id in robots_tours:
            with self.subTest(robot_id=robot_id):
                self.assertAlmostEqual(recalculated_costs[robot_id], expected_costs[robot_id], places=5)

    def test_minimize_maximum_distance(self):
        costs = [sum(euclidean					     .distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) \
                 for tour in robots_tours.values()]
        max_cost = max(costs)
        # The expected maximum cost from the task
        expected_max_cost = 191.81392598621446
        self.assertEqual(max_cost, expected_max


_cost)

# Running tests
if __name__ == "__main__":
    unittest.main()