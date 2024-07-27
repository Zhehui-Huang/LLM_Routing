import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        # City coordinates
        cities = [
            (84, 67),  # Depot city 0
            (74, 40),  # City 1
            (71, 13),  # City 2
            (74, 82),  # City 3
            (97, 28),  # City 4
            (0, 31),   # City 5
            (8, 62),   # City 6
            (74, 56),  # City 7
            (85, 71),  # City 8
            (6, 76)    # City 9
        ]

        # Provided tour
        tour = [0, 7, 6, 5, 9, 1, 2, 4, 8, 3, 0]
        # Provided total travel cost
        total_travel_cost = 370.90358172409935

        # [Requirement 1] Start and end at city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # [Requirement 2] Visit all cities exactly once
        cities_visited = set(tour)
        self.assertEqual(len(cities_visited), 10)
        self.assertSetEqual(cities_visited, set(range(len(cities))))

        # [Requirement 3 & 5] Validate the computed travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

        self.assertAlmostEqual(calculated_cost, total_travel_cost, places=5)

        # [Requirement 4] Ensure tour is a correct format
        expected_number_of_cities = len(cities)
        self.assertEqual(len(tour), expected_number_of_cities + 1)  # Includes return to depot

        # If the requirements above are met, we will print CORRECT, otherwise FAIL
        print("CORRECT")


# Running the test
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # Adjustments for Jupyter Notebooks