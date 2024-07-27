import unittest
import math

cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

tour_solution = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost_solution = 322.5037276986899

def calculate_tour_cost(tour):
    return sum(euclidean_lookup(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

class TestTourSolution(unittest.TestCase):
    
    def test_tour_start_end_at_depot(self):
        self.assertEqual(tour_solution[0], 0)  # Start at depot
        self.assertEqual(tour_solution[-1], 0)  # End at depot

    def test_tour_visits_all_cities_once(self):
        # Check only cities 1 to 14 are visited once and depot city 0 is visited twice.
        visits = {x: tour_solution.count(x) for x in range(15)}
        self.assertEqual(visits[0], 2)  # Depot city revisited only once at the end
        for city in range(1, 15):
            self.assertEqual(visits[city], 1)

    def test_travel_cost_calculation(self):
        calculated_cost = calculate_tour_cost(tour_solution)
        self.assertAlmostEqual(calculated_cost, total_cost_solution, places=5)
    
    def test_output_format(self):
        self.assertIsInstance(tour_solution, list)
        self.assertIsInstance(total_cost_solution, float)

if __name__ == '__main__':
    unittest.main()