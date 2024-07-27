import unittest
import math

# Define the cities coordinates
cities = [
    (79, 15),  # Depot
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Solution Output
tour_solution = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
total_cost_solution = 320.7939094250147

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_cities_visited_once(self):
        # Verify all cities except the depot are visited exactly once
        self.assertEqual(len(set(tour_solution) - {0}), 9)
        
    def test_start_end_at_depot(self):
        # Check tour starts and ends at depot
        self.assertEqual(tour_solution[0], 0)
        self.assertEqual(tour_solution[-1], 0)
        
    def test_complete_tour(self):
        # Check all cities are visited
        self.assertCountEqual(tour_solution, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    
    def test_travel_cost(self):
        # Recompute the tour cost based on the given solution and verify the cost
        total_cost = sum(calculate_euclidean_distance(tour_solution[i], tour_solution[i + 1]) for i in range(len(tour_solution) - 1))
        self.assertAlmostEqual(total_cost, total_cost_solution)
        
    def test_output_format(self):
        # Check that the output tour and cost are in correct format
        self.assertIsInstance(tour_solution, list)
        self.assertIsInstance(total_cost_solution, float)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
unittest.TextTestRunner().run(suite)