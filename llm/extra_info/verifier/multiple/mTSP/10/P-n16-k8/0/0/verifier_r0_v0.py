import math
import unittest

# Coordinates of the cities including the depot city
coordinates = {
    0: (30, 40),   # Depot
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def calculate_travel_cost(tour):
    """
    Calculate the travel cost based on the Euclidean distance between cities in the tour.
    """
    total_cost = 0.0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(total_cost, 2)

class TestTravelingSalesmanProblem(unittest.TestCase):
    
    def test_tours(self):
        # Robot tours and their calculated costs as given in the query
        robot_tours = [
            [0, 7, 11, 0],
            [0, 15, 12, 0],
            [0, 10, 8, 0],
            [0, 4, 13, 0],
            [0, 3, 9, 0],
            [0, 6, 1, 0],
            [0, 5, 2, 0],
            [0, 14, 0]
        ]
        robot_costs = [86.98, 66.12, 68.29, 81.56, 88.79, 38.02, 60.39, 61.74]
        
        # Check each tour to ensure it satisfies [Requirement 3] and [Requirement 7]
        # and that the total costs match [Requirement 6] and [Requirement 7]
        visited_cities = set()
        calculated_total_cost = 0
        provided_total_cost = 551.89

        for tour, provided_cost in zip(robot_tours, robot_costs):
            self.assertEqual(tour[0], 0)  # Tour must start at depot
            self.assertEqual(tour[-1], 0)  # Tour must end at depot
            visited_cities.update(tour[1:-1])  # Exclude the depot city

            # Test calculated tour cost
            calculated_cost = calculate_travel_cost(tour)
            self.assertAlmostEqual(calculated_cost, provided_cost, delta=0.1)
            calculated_total_cost += calculated_cost

        # Check if all cities have been visited exactly once excluding the depot
        self.assertEqual(len(visited_cities), 15)  # [Requirement 4] and [Requirement 7]
        self.assertNotIn(0, visited_cities)  # Depot should not be counted here

        # Test the total cost
        self.assertAlmostEqual(calculated_total_cost, provided_total_cost, delta=0.1)

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTravelingSalesmanProblem)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")