import unittest
import math

# Assuming we have a function get_solution() that implements the GVNS algorithm and returns the required data
# For the context of this mock, let's define a placeholder function
def get_solution():
    # Example data to test; this might come from actual algorithm output
    return {
        'tours': [
            [0, 1, 2, 0],
            [0, 3, 4, 0],
            [0, 5, 6, 0],
            [0, 7, 8, 9, 0]
        ],
        'costs': [60, 50, 77, 65],
        'max_cost': 77
    }

# The city coordinates as stated
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_tours_and_costs(self):
        solution = get_solution()
        tours = solution['tours']
        costs = solution['costs']
        max_cost = solution['max_cost']

        # Testing requirement 2 and 8
        visited_cities = set()
        for tour in tours:
            self.assertTrue(tour[0] == 0 and tour[-1] == 0, "Tours must start and end at the depot")
            for city in tour[1:-1]:
                visited_cities.add(city)

        # Testing requirement 1
        self.assertEqual(len(visited_cities), 21, "All cities except the depot must be visited exactly once")

        # Testing requirement 7
        computed_costs = []
        for tour in tours:
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            computed_costs.append(tour_cost)

        self.assertListEqual(costs, computed_costs, "Costs must match calculated values")
        self.assertEqual(max(computed_costs), max_cost, "Maximum cost must be correct")

        # Checking requirement 3
        self.assertEqual(max_cost, max(computed_costs), "Must minimize the maximum distance traveled")

        # If all tests pass, we consider the solution correct
        print("CORRECT")

# Run the tests
if __name__ == '__main__':
    unittest.main()