import unittest
from math import sqrt

def calculate_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
            (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
            (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
        ]
        self.tour = [0, 8, 10, 11, 0]
        self.reported_total_cost = 110.01

    def test_tour_start_end_at_depot(self):
        # Verify the tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_length(self):
        # Verify exactly 4 unique cities are visited, including the depot
        unique_cities_count = len(set(self.tour))
        self.assertEqual(unique_cities_count, 4)

    def test_tour_distance(self):
        # Calculate the total travel cost from the tour
        tour_cost = sum(calculate_distance(self.coordinates[self.tour[i]], self.coordinates[self.tour[i + 1]])
                        for i in range(len(self.tour) - 1))
        # Test if the calculated distance matches the reported total cost, within a small error margin
        self.assertAlmostEqual(tour_cost, self.reported_total_cost, places=2)

    def test_solution(self):
        # Run all tests and print "CORRECT" if all tests pass, otherwise "FAIL"
        suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
        result = unittest.TextTestRunner().run(suite)

        if result.wasSuccessful():
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main()