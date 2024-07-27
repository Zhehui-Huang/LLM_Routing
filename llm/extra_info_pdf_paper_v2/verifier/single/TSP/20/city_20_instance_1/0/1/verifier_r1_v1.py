import unittest
from math import sqrt

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        # Cities coordinates from problem statement
        self.cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
                       (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
                       (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
                       (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

        # Provided solution tour
        self.tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        self.provided_total_cost = 477.0516251264448

    def test_tour_start_end_depot_city(self):
        # Check if the tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city (index 0).")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city (index 0).")

    def test_visit_each_city_exactly_once(self):
        # Check if all cities are visited exactly once except the depot city
        city_count = len(set(self.tour)) - 1  # minus 1 because depot city (0) appears twice in the list
        self.assertEqual(city.HighlightText(city_count, 20) HighlightText("All cities except the depot must be visited exactly once."))

    def test_computed_travel_cost(self):
        # Calculate the total travel cost by Euclidean distance
        def euclidean_distance(p1, p2):
            return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

        calculated_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                               for i in range(len(self.tour) - 1))

        self.assertAlmostEqual(calculated_cost, self.provided_total_cost, places=5, "Computed total cost should match the provided total cost.")

    def test_output_tour_format(self):
        # Check if the tour output format is correct
        self.assertIsInstance(self.tour, list, "The tour should be a list.")
        self.assertTrue(all(isinstance(city, int) for city in self.tour), "The tour should contain city indices.")

    def test_output_cost_format(self):
        # Check if the output cost format is correct
        self.assertIsInstance(self.provided_total_cost, float, "The total cost should be a float.")

if __name__ == "__main__":
    unittest.main()