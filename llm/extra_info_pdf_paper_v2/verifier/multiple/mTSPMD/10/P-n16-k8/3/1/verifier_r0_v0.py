import math
import unittest

# Data for tours and their costs
solution = {
    'robots': [
        {'tour': [0, 11, 15, 12, 10, 8, 13, 9, 14, 0], 'cost': 133.27370957078404},
        {'tour': [1, 1], 'cost': 0},
        {'tour': [2, 2], 'cost': 0},
        {'tour': [3, 3], 'cost': 0},
        {'tour': [4, 4], 'cost': 0},
        {'tour': [5, 5], 'cost': 0},
        {'tour': [6, 6], 'cost': 0},
        {'tour': [7, 7], 'cost': 0},
    ],
    'overall_cost': 133.27370957078404
}

# City coordinates
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities based on their coordinates."""
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_each_city_visited_once(self):
        all_cities = set(range(len(city_coordinates)))
        visited_cities = set()
        for robot in solution['robots']:
            # Exclude the repeating depot city at start and end
            visited_cities.update(robot['tour'][1:-1])
            
        self.assertEqual(all_cities, visited_cities, "Each city must be visited exactly once.")

    def test_correct_start_end_depot_for_each_robot(self):
        for i, robot in enumerate(solution['robots']):
            self.assertEqual(robot['tour'][0], robot['tour'][-1], f"Robot {i} must start and end at the same depot.")
            self.assertEqual(robot['tour'][0], i, f"Robot {i} must start and end at depot {i}.")

    def test_minimize_total_travel_cost(self):
        calculated_costs = []
        for robot in solution['robots']:
            tour = robot['tour']
            tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            calculated_costs.append(tour_cost)
            self.assertAlmostEqual(tour_cost, robot['cost'], delta=1e-5, msg=f"Cost mismatch for robot tour {tour}")
        total_cost = sum(calculated_costs)
        self.assertAlmostEqual(total_cost, solution['overall_cost'], delta=1e-5, msg="Overall cost mismatch.")

if __name__ == "__main__":
    test_result = unittest.TestResult()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTSPSolution)
    suite.run(test_result)
    
    # Output result based on if any tests failed or not
    print("CORRECT" if not test_result.failures and not test_result.errors else "FAIL")