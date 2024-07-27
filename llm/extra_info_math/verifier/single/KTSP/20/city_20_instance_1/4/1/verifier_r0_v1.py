import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):

    def test_solution(self):
        cities = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
            (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
            (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
            (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        tour = [0, 14, 9, 2, 13, 8, 1, 0]
        reported_total_cost = 143.83

        # Check Requirement 1: Start and end at depot city (city index 0)
        self.assertEqual(tour[0], 0, "The tour does not start at the depot city.")
        self.assertEqual(tour[-1], 0, "The tour does not end at the depot city.")

        # Check Requirement 2: Exactly 7 cities visited, including the depot
        self.assertEqual(len(set(tour)), 7, "The number of unique cities visited is not 7.")

        # Check Requirement 3: Verify the travel cost
        calculated_total_cost = 0
        for i in range(len(tour) - 1):
            calculated_total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost = round(calculated_total_cost, 2)
        
        self.assertAlmostEqual(calculated_total_cost, reported_total_cost, places=2, 
                               msg="Calculated cost does not match the reported total cost.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)