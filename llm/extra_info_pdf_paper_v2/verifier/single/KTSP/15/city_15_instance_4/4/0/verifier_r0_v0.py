import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.solution_tour = [0, 10, 4, 12, 6, 3, 8, 14, 13, 9, 7, 5, 0]
        self.reported_cost = 348.73
        self.city_positions = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }

    def test_start_end_city(self):
        # Requirement 1
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_exact_cities_visited(self):
        # Requirement 2
        self.assertEqual(len(set(self.solution_tour)), 12)

    def test_total_cities(self):
        # Requirement 3
        self.assertEqual(len(self.city_positions), 15)

    def test_tour_is_valid(self):
        # Requirement 5
        start_at_depot = self.solution_tour[0] == 0
        end_at_depot = self.solution_tour[-1] == 0
        self.assertTrue(start_at_depot and end_at_depot)
    
    def test_total_travel_cost(self):
        # Requirement 6
        total_cost = 0
        for i in range(1, len(self.solution_tour)):
            city1 = self.solution_tour[i - 1]
            city2 = self.solution_tour[i]
            dx = self.city_positions[city2][0] - self.city_positions[city1][0]
            dy = self.city_positions[city2][1] - self.city_index[city1][1]
            total_cost += math.sqrt(dx**2 + dy**2)
        # Check within a reasonable precision delta
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

# Execute the test suite
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")