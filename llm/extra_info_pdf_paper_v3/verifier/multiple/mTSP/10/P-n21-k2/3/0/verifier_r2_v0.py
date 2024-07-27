import unittest
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Provided tours and costs
robot_tours = {
    0: [0, 6, 7, 5, 9, 2, 10, 1, 4, 3, 8, 0],
    1: [0, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 0]
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour_starts_and_ends_at_depot(tour):
    """ Check if the tour starts and ends at the depot """
    return tour[0] == tour[-1] == 0

def validate_unique_cities_visit(tours):
    """ Validate that each city, except the depot, is visited exactly once collectively """
    visited = set()
    for tour in tours.values():
        for city in tour[1:-1]:  # ignore first and last city because they are depot
            if city in visited:
                return False
            visited.add(city)
    return len(visited) == 20  # Since 21 cities include the depot

def calculate_total_tour_cost(tour):
    """ Calculate the total tour cost for a given tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    
    def test_tour_start_and_end_points(self):
        for tour in robot_tours.values():
            self.assertTrue(check_tour_starts_and_ends_at_depot(tour))
    
    def test_all_cities_visited_exactly_once(self):
        self.assertTrue(validate_unique_cities_visit(robot_tours))
    
    def test_correct_travel_cost_calculation(self):
        calculated_costs = {0: 148.98, 1: 146.55}  # Provided costs rounded to two decimal places
        for robot_id, tour in robot_tours.items():
            self.assertAlmostEqual(calculate_total_tour_cost(tour), calculated_costs[robot_id], places=2)
    
    def test_overall_cost(self):
        expected_total_cost = sum(calculate_total_tour_cost(tour) for tour in robot_tours.values())
        self.assertAlmostEqual(expected_total_cost, 295.53, places=2)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")