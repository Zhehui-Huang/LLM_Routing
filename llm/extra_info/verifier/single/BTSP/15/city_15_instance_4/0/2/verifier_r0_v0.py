import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        cities = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]
        tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        calculated_total_cost = 0
        calculated_max_distance = 0
        
        # Check if starts and ends at the depot
        self.assertEqual(tour[0], 0, "Robot should start at depot.")
        self.assertEqual(tour[-1], 0, "Robot should end at depot.")
        
        # Check if all cities are visited exactly once, apart from the depot
        from collections import Counter
        city_counter = Counter(tour)
        self.assertEqual(city_counter[0], 2, "Depot city should be visited twice.")
        for i in range(1, 15):
            self.assertEqual(city_counter[i], 1, "Each city needs to be visited exactly once.")
        
        # Calculate total cost and maximum distance between consecutive cities
        for i in range(len(tour) - 1):
            distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            calculated_total_cost += distance
            if distance > calculated_max_distance:
                calculated_max_distance = distance
        
        # Check total travel cost and maximum consecutive distance
        self.assertAlmostEqual(calculated_total_cost, 337.84, places=2, msg="Total travel cost should match.")
        self.assertAlmostEqual(calculated_max_distance, 60.67, places=2, msg="Maximum distance between consecutive cities should match.")

# Run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
unittest.TextTestRunner().run(suite)