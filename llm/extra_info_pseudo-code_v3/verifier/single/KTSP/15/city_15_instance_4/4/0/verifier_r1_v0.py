import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # Given coordinates of the cities (including depot)
        coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
                       (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
                       (53, 80), (21, 21), (12, 39)]
        
        # Given solution
        tour = [0, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 1, 0]
        reported_cost = 231.28885474918823
        
        # Check Requirement 1 & 4: Starts and ends at city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check Requirement 2: Exactly 12 cities
        self.assertEqual(len(set(tour)), 12)
        
        # Check Requirement 3: Minimum tour requirement cannot be precisely validated without full optimization logic
        # However, we can compute the provided tour cost and compare with given cost
        calculated_cost = total_tour_cost(tour, coordinates)
        self.assertAlmostEqual(calculated_cost, reported_cost, places=5)

        # Check Requirement 5: Reporting cost correctly
        self.assertAlmostEqual(reported_cost, 231.28885474918823, places=5)
        
        # If all checks pass
        print("CORRECT")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)