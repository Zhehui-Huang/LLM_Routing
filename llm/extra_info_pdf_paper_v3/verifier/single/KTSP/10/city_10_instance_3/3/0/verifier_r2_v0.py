import unittest
from math import sqrt

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 4, 2, 1, 7, 3, 8, 0]
        self.total_cost = 159.97

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city 0")

    def test_tour_length(self):
        self.assertEqual(len(self.tour), 8, "The tour must visit exactly 8 positions (7 cities + depot)")

    def test_visit_seven_cities_including_depot(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 7, "The robot must visit exactly 7 unique cities including the depot")

    def test_calculate_total_distance(self):
        def euclidean_distance(c1, c2):
            return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_a = self.coordinates[self.tour[i]]
            city_b = self.coordinates[self.tour[i + 1]]
            calculated_cost += euclidean_distance(city_a, city_b)

        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2, msg="Calculated total travel cost must be close to the provided total")

    def test_output_format(self):
        self.assertIsInstance(self.tour, list, "The tour must be a list")
        self.assertTrue(all(isinstance(city, int) for city in self.tour), "City indices in the tour must be integers")
        self.assertIsInstance(self.total_cost, float, "Total travel cost must be a float")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")