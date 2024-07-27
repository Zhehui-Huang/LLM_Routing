import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(coordinates, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclideanDistance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (29, 51),  # Depot 0
            (49, 20),  # City 1 Group 0
            (79, 69),  # City 2 Group 0
            (17, 20),  # City 3 Group 2
            (18, 61),  # City 4 Group 2
            (40, 57),  # City 5 Group 0
            (57, 30),  # City 6 Group 0
            (36, 12),  # City 7 Group 2
            (93, 43),  # City 8 Group 1
            (17, 36),  # City 9 Group 1
            (4, 60),   # City 10 Group 1
            (78, 82),  # City 11 Group 3
            (83, 96),  # City 12 Group 3
            (60, 50),  # City 13 Group 1
            (98, 1)    # City 14 Group 3
        ]
        self.groups = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.provided_tour = [0, 1, 13, 7, 14, 0]
        self.provided_cost = 261.96898175403817

    def test_tour_validity(self):
        # Start and end at depot
        self.assertEqual(self.provided_tour[0], 0)
        self.assertEqual(self.provided_tour[-1], 0)
        
        # Only one city from each group
        visited_groups = [False] * len(self.groups)
        for city in self.provided_tour[1:-1]:  # ignoring the depot at start and end
            for i, group in enumerate(self.groups):
                if city in group:
                    self.assertFalse(visited_groups[i])
                    visited_groups[i] = True
        self.assertTrue(all(visited_groups))
        
        # Calculate travel cost and compare
        calculated_cost = calculate_total_travel_cost(self.coordinates, self.provided_tour)
        self.assertAlmostEqual(calculated_cost, self.provided_cost, places=5)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTravelingSalesmanSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()