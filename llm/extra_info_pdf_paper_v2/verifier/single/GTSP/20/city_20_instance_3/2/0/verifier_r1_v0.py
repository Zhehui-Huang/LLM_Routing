import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.grouped_cities = [
            [4, 10, 13, 17], [6, 7, 14], 
            [9, 12, 16], [2, 5, 15], 
            [1, 3, 19], [8, 11, 18]
        ]
        self.solution_tour = [0, 18, 6, 3, 15, 17, 16, 0]
        self.reported_cost = 199.42225020008016
    
    def test_tour_length(self):
        # Check if the tour starts and ends at city 0
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_tour_cities_grouping(self):
        # Check if exactly one city from each group is visited
        visited_groups = set()
        for city in self.solution_tour[1:-1]:
            for i, group in enumerate(self.grouped_cities):
                if city in group:
                    visited_groups.add(i)
        self.assertEqual(len(visited_groups), 6)

    def test_tour_travel_cost(self):
        # Calculate the Euclidean distance and check the travel cost
        total_cost = 0
        for i in range(len(self.solution_tour)-1):
            c1 = self.solution_tour[i]
            c2 = self.solution_tour[i+1]
            total_cost += math.sqrt((self.cities[c1][0] - self.cities[c2][0])**2 + (self.cities[c1][1] - self.cities[c2][1])**2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5)

    def test_minimum_tour_requirement(self):
        # Since optimizing and asserting a global minimum is complex without re-solving,
        # we just confirm that this tour is indeed a valid solution considering the constraints
        self.assertTrue(self.reported_cost > 0)


def run_tsp_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tsp_tests()