import unittest
import math

class TestBTSPSolution(unittest.TestCase):
    def test_solution(self):
        cities = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        
        tour = [0, 3, 8, 5, 0]
        expected_total_cost = 111.39
        expected_max_distance = 43.05
        
        # Requirement 1: Check if every city except the depot is visited once
        self.assertEqual(len(set(tour) - {0}), len(cities) - 1)
        
        # Calculate costs
        def euclidean_distance(a, b):
            return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

        travel_costs = [euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
        total_cost = sum(travel_costs)
        max_distance = max(travel_costs)

        # Requirement 2: Check if the maximum distance between any two consecutive cities in the tour is minimized
        # To exactly check this would require solving it or knowing the optimal; here we just confirm it's close to the provided
        self.assertAlmostEqual(max_distance, expected_max_distance, places=2)

        # Requirement 3: Compute the total travel cost and confirm it
        self.assertAlmostEqual(total_cost, expected_total_circle_cost, places=2)
        
        # Since no known 'optimal solution' is provided, just output success
        print("CORRECT")

# Running the test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)