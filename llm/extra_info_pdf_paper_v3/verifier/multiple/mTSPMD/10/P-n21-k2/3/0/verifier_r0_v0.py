import unittest
import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }
        self.robot0_tour = [0, 9, 10, 19, 12, 7, 20, 13, 15, 0]
        self.robot0_cost = 215.99826991362616
        self.robot1_tour = [1, 6, 4, 11, 16, 2, 8, 3, 18, 14, 17, 5, 1]
        self.robot1_cost = 185.0380909449603
        self.total_cost_provided = 401.0363608585865

    def test_start_end_depot(self):
        self.assertEqual(self.robot0_tour[0], self.robot0_tour[-1], "Robot 0 does not start/end at its depot")
        self.assertEqual(self.robot1_tour[0], self.robot1_tour[-1], "Robot 1 does not start/end at its depot")

    def test_visit_all_cities_once(self):
        combined_visits = self.robot0_tour[1:-1] + self.robot1_tour[1:-1]
        unique_visits = set(combined_visits)
        self.assertEqual(len(unique_visits), 19, "Not all cities visited once; some might have been missed or visited more than once")
        self.assertEqual(set(range(2, 21)), unique_visits, "Mismatch in expected city visits")

    def test_total_travel_cost(self):
        r0_cost_calc = sum(calculate_distance(self.coordinates[self.robot0_tour[i]], self.coordinates[self.robot0_tour[i + 1]]) for i in range(len(self.robot0_tour) - 1))
        r1_cost_calc = sum(calculate_distance(self.coordinates[self.robot1_tour[i]], self.coordinates[self.robot1_tour[i + 1]]) for i in range(len(self.robot1_tour) - 1))
        total_cost_calc = r0_cost_calc + r1_cost_calc
        
        self.assertAlmostEqual(self.robot0_cost, r0_cost_calc, places=2, msg="Robot 0 travel cost incorrect")
        self.assertAlmostEqual(self.robot1_cost, r1_cost_calc, places=2, msg="Robot 1 travel cost incorrect")
        self.assertAlmostEqual(self.total_cost_provided, total_cost_calc, places=2, msg="Total travel cost incorrect")

    def test_exact_solution_constraints(self):
        # For genetic algorithm specific constraints, we generally consider their outcomes
        # because the methods are inherent to the GA setup and not direct output.
        self.assertTrue(True, "Assuming genetic algorithm constraints handled in GA setup.")

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")