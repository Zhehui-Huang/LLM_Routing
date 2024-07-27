import unittest
from math import sqrt

def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    def test_solution(self):
        coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
            (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        
        tours = [
            [0, 6, 0], [1, 10, 1], [2, 13, 2], [3, 8, 3], [4, 11, 4], [5, 14, 5],
            [6, 7, 6], [7, 9, 7]
        ]
        
        costs = [
            24.08318915758459, 14.142135623730951, 18.110770276274835, 15.620499351813308,
            14.422205101855956, 16.97056274847714, 20.0, 20.09975124224178
        ]
        
        expected_total_cost = 143.44911350197856
        
        # Check if all cities are visited exactly once.
        all_visited_cities = sorted([city for tour in tours for city in tour if city not in [0, 1, 2, 3, 4, 5, 6, 7]])
        self.assertEqual(all_visited_cities, [8, 9, 10, 11, 12, 13, 14, 15])
        
        # Verify each robot starts and ends at its assigned depot
        for index, tour in enumerate(tours):
            self.assertEqual(tour[0], index)
            self.assertEqual(tour[-1], index)
        
        # Calculate and verify the journey costs
        calculated_costs = []
        for tour in tours:
            cost = 0
            for i in range(len(tour) - 1):
                cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
            calculated_costs.append(cost)
        
        for calculated_cost, expected_cost in zip(calculated_costs, costs):
            self.assertAlmostEqual(calculated_cost, expected_cost, places=5)
        
        # Verify the total cost
        self.assertAlmostEqual(sum(costs), expected_total_cost, places=5)

        # If all tests pass
        print("CORRECT")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)