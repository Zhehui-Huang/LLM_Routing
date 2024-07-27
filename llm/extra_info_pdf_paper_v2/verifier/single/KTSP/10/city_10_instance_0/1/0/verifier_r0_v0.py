import unittest
from math import sqrt

def compute_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coords = [
            (50, 42),  # Depot city 0
            (41, 1),
            (18, 46),
            (40, 98),
            (51, 69),
            (47, 39),
            (62, 26),
            (79, 31),
            (61, 90),
            (42, 49)
        ]

        # Provided solution
        self.tour = [4, 9, 5, 0, 0]
        self.total_cost = 37

    def test_tour_starts_and_ends_at_depot(self):
        # Requirement 5
        self.assertEqual(self.toured_code[0], 0, "Tour should start at depot.")
        self.assertEqual(self.toured_code[-1], 0, "Tour should end at depot.")

    def test_tour_length(self):
        # Requirement 4
        self.assertEqual(len(set(self.tour))-1, 4, "Tour should visit exactly 4 cities, including depot.")

    def test_all_cities_valid(self):
        # Requirement 1
        self.assertTrue(all(city in range(len(self.coords)) for city in self.tour), "All cities in the tour must be valid.")

    def test_correct_total_cost(self):
        # Requirement 7
        calc_cost = sum(compute_distance(self.coords[self.tour[i]], self.coords[self.tour[i+1]]) for i in range(len(self.tour)-1))
        self.assertAlmostEqual(calc_cost, self.total_cost, msg="Calculated travel cost does not match provided cost.", places=2)

def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestKTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    # Check if all tests have passed
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()