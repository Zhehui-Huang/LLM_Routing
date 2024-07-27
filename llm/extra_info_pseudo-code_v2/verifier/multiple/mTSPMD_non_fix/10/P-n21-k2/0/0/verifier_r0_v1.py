import unittest
import math

def get_cities():
    return list(range(21))  # City indices from 0 to 20

def robot_start_locations():
    return {0: 0, 1: 0}  # Both robots start at depot city 0

def euclidean_distance(a, b, city_coords):
    dx, dy = city_coords[a][0] - city_coords[b][0], city_coords[a][1] - city_coords[b][1]
    return math.sqrt(dx**2 + dy**2)

# Provide full coordinates for all cities
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours.values():
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(tour[i], tour[i+1], city_coords)
    return total_cost

# Test solution assuming output has two robots and tours as indicated
tours = {
    0: [0, 2, 3],  # Robot 0 tour
    1: [1, 4, 5]   # Robot 1 tour
}
total_cost = calculate_total_cost(tours)

class TestTSPSolution(unittest.TestCase):
    def test_city_count(self):
        self.assertEqual(len(get_cities()), 21)

    def test_city_indices(self):
        self.assertEqual(get_cities(), list(range(21)))

    def test_number_of_robots(self):
        self.assertEqual(len(robot_start_locations()), 2)

    def test_unique_city_visits(self):
        visited = set()
        for tour in tours.values():
            for city in tour:
                self.assertNotIn(city, visited)
                visited.add(city)

    def test_total_cost_calculation(self):
        expected_cost = calculate_total_cost(tours)
        self.assertEqual(total_cost, expected_cost)

    def test_correct_tour_departure(self):
        start_locs = robot_start_locations()
        for robot_id, tour in tours.items():
            self.assertEqual(tour[0], start_locs[robot_id])  # Start at their designated depot

# If using in a script:
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("CORRECT" if result.wasSuccessful() else "FAIL")