import unittest
import math

# Data setup
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Solution details
solution_tours = {
    0: [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0],
    1: [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0]
}

solution_costs = {
    0: 115.60,
    1: 149.77
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += calculate_euclidean_distance(tour[i], tour[i+1])
    return round(cost, 2)

class TestRobotTours(unittest.TestCase):
    def test_solution(self):
        result = True
        visited_cities = set()

        for robot_id, tour in solution_tours.items():
            # Check if the tour starts and ends at the depot
            self.assertTrue(tour[0] == tour[-1] == 0, "Tour does not start and end at the depot.")
            # Calculate and compare the tour cost
            cost_calculated = calculate_total_tour_cost(tour)
            self.assertAlmostEqual(cost_calculated, solution_costs[robot_id], places=2, msg="Cost does not match.")
            # Check for each city visited once
            visited_cities.update(tour[1:-1])

        # Check all cities visited exactly once
        self.assertEqual(len(visited_cities), 18, "Not all non-depot cities are visited exactly once.")
        
        if result:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)