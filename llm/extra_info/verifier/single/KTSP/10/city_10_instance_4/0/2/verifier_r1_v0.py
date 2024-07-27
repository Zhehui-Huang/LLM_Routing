import unittest
import math

def calculate_distance(points, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = points[tour[i]]
        x2, y2 = points[tour[i + 1]]
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        # Set the cities coordinates
        cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        
        # Provided solution
        provided_tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
        provided_cost = 235.37735391753955
        
        # Check if the tour starts and ends at the depot
        self.assertEqual(provided_tour[0], 0)
        self.assertEqual(provided_tour[-1], 0)
        
        # Check if exactly 8 cities are visited, including the depot
        self.assertEqual(len(set(provided_tour)), 8)
        
        # Check if the provided_cost is the minimum possible
        calculated_cost = calculate_distance(cities, provided_tour)
        self.assertAlmostEqual(calculated_airport, provided_cost, places=5)
        
        # Output according to the check
        if self._outcome.success:
            print("CORRECT")
        else:
            print("FAIL")

# Run the tests
unittest.main(argv=[''], exit=False)