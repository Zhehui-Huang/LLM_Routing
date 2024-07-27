import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.tour = [0, 3, 6, 2, 8, 9, 1, 0]
        self.travel_cost = 261.4170938413197

    def test_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at city 0")

    def test_visit_exactly_8_cities(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 8, "The robot should visit exactly 8 unique cities including the depot city")

    def test_tour_structure(self):
        self.assertEqual(len(self.tour), 8, "Including depot city at start and end, tour list should have 8 entries")

    def test_correct_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(calculated_cost, self.travel_cost, places=4,
                               msg="Calculated travel cost should match provided total travel cost.")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)