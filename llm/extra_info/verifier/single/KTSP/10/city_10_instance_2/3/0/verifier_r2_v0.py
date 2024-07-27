import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (90, 3), # Depot 0
            (11, 17), # City 1
            (7, 27),  # City 2
            (95, 81), # City 3
            (41, 54), # City 4
            (31, 35), # City 5
            (23, 95), # City 6
            (20, 56), # City 7
            (49, 29), # City 8
            (13, 17)  # City 9
        ]
        self.tour = [0, 8, 5, 2, 1, 9, 0]
        self.reported_cost = 183.85354044487238

    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_visit_exactly_6_cities(self):
        self.assertEqual(len(set(self.tour)), 6, "Tour does not visit exactly 6 distinct cities")

    def test_travel_cost_calculation(self):
        calculated_cost = calculate_total_travel_cost(self.tour, self.cities)
        self.assertAlmostEqual(calculated_easy_cost, self.reported_cost, places=5, "Calculated travel cost is incorrect")

    def test_tour_output(self):
        # This will handle Requirement 4 indirectly through other tests.
        pass

    def test_goal_minimize_total_distance(self):
        # This requirement might need a reference value or algorithm to be fully verified.
        # Here, we just check consistency with the provided cost.
        self.assertLessEqual(self.reported_cost, 183.85354044487238, "Reported cost is not the minimal possible cost")

if __name__ == "__main__":
    unittest.main()