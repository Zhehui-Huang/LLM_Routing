import unittest
import math

class TestKTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Provided tour and its cost
        self.tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.total_cost = 132.1185774560832
        # Coordinates of the cities
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")

    def test_tour_length_including_depot_twice(self):
        self.assertEqual(len(self.tour), 9, "Tour should include exactly 8 cities plus the return to the depot")

    def test_calculate_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            start = self.tour[i]
            end = self.tour[i + 1]
            calculated_cost += math.sqrt((self.cities[start][0] - self.cities[end][0])**2 + (self.cities[start][1] - self.cities[end][1])**2)
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5, msg="Calculated travel cost should match provided total cost")

    def test_complete_solution(self):
        results = (self.tour == [0, 2, 13, 3, 4, 12, 11, 6, 0] and
                   math.isclose(self.total_cost, 132.1185774560832, rel_tol=1e-5))
        self.assertTrue(results, "The solution tour and total cost must match the expected values")

if __name__ == "__main__":
    unittest.main()