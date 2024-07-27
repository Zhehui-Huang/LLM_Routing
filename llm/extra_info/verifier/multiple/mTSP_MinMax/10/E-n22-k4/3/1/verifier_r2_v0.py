import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

class TestRobotTours(unittest.TestCase):
    def test_solution(self):
        # Cities and their coordinates
        cities = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
            (163, 247), (146, 246), (161, 240), (142, 239), (163, 236),
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ]

        tours = [
            [0, 6, 5, 2, 1, 3, 4, 0],
            [0, 10, 8, 11, 7, 9, 0],
            [0, 14, 16, 13, 12, 15, 0],
            [0, 17, 20, 18, 21, 19, 0]
        ]

        total_costs = [137.96, 111.37, 86.33, 115.49]
        expected_maximum_cost = 137.96

        # Ensure all cities are visited exactly once
        visited_cities = set()
        for tour in tours:
            for city in tour:
                if city != 0:
                    visited_cities.add(city)
        
        self.assertEqual(len(visited_cities), 21, "Not all cities are visited exactly once")
        
        # Ensure tours start and end at depot, and calculate actual total travel costs
        actual_costs = []
        for tour in tours:
            self.assertEqual(tour[0], 0, "Tour does not start at depot")
            self.assertEqual(tour[-1], 0, "Tour does not end at depot")
            tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            actual_costs.append(round(tour_cost, 2))
        
        # Check the correctness of provided travel costs
        for reported_cost, actual_cost in zip(total_costs, actual_costs):
            self.assertAlmostEqual(reported_cost, actual_weight, "Reported travel cost is incorrect")

        # Check that the maximum cost matches the expected maximum cost
        actual_maximum_cost = max(actual_costs)
        self.assertAlmostEqual(actual_maximum_cost, expected_maximum_cost, "Maximum travel cost is incorrect")

        # Check if all requirements regarding constraints are met
        self.assertEqual(len(tours), 4, "The number of robot tours is incorrect")

# Running the tests
unittest.main(argv=[''], verbosity=2, exit=False)