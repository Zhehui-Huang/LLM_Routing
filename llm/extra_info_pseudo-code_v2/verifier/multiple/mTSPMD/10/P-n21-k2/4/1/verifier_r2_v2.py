import unittest
import math

# Function to calculate Euclidean distance
def calculate_distance(city1, check_city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Simulated function outputs based on the function we're testing
def get_robots_tours_and_costs():
    # Example solution based on task description (mocked)
    return {
        "Robot 0": {
            "Tour": [0, 2, 3, 0],
            "Total Travel Cost": calculate_tour_cost([(30, 40), (49, 49), (52, 64), (30, 40)])
        },
        "Robot 1": {
            "Tour": [1, 4, 5, 1],
            "Total Travel Cost": calculate_tour_cost([(37, 52), (31, 62), (52, 33), (37, 52)])
        }
    }

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # Get results from the simulated function
        self.results = get_robots_tours_and_costs()
        self.robot_0_tour = self.results["Robot 0"]["Tour"]
        self.robot_1_tour = self.results["Robot 1"]["Tour"]

    def test_tour_requirements(self):
        all_tour_cities = set(self.robot_0_tour[:-1] + self.robot_1_tour[:-1])
        all_cities = set(range(21))
        # Each city is visited exactly once
        self.assertEqual(all_tour_cities, all_cities)

    def test_travel_cost_calculation(self):
        # Verify calculated costs are coherent with the distance function
        expected_robot_0_cost = calculate_tour_cost([(30, 40), (49, 49), (52, 64), (30, 40)])
        expected_robot_1_cost = calculate_tour_cost([(37, 52), (31, 62), (52, 33), (37, 52)])

        self.assertAlmostEqual(self.results["Robot 0"]["Total Travel Cost"], expected_robot_0_cost)
        self.assertAlmostEqual(self.results["Robot 1"]["Total Travel Cost"], expected_robot_1_cost)

    def test_overall_cost(self):
        # Verify the overall cost
        overall_cost = self.results["Robot 0"]["Total Travel Cost"] + self.results["Robot 1"]["Total Travel Cost"]
        expected_overall_cost = calculate_tour_cost([(30, 40), (49, 49), (52, 64), (30, 40)]) + calculate_tour_cost([(37, 52), (31, 62), (52, 33), (37, 52)])
        self.assertAlmostEqual(overall_cost, expected_overall_cost)

if __name__ == "__main__":
    unittest.main()