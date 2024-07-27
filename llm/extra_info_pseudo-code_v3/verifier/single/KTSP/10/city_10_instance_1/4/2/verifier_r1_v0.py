import unittest
from math import sqrt

class TestKTravelingSalesman(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 9, 2, 5, 3, 0]
        self.reported_cost = 158.46
        self.coordinates = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city.")

    def test_tour_length(self):
        self.assertEqual(len(self.tour), 6, "Tour should include exactly 6 cities (including repeat of depot).")

    def test_tour_distance(self):
        def euclidean_distance(c1, c2):
            return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

        calculated_cost = 0
        for i in range(1, len(self.tour)):
            city1, city2 = self.tour[i-1], self.tour[i]
            calculated_cost += euclidean_distance(self.coordinates[city1], self.coordinates[city2])
        
        # Verify distance with some tolerance
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=1, msg="Reported travel cost should be close to calculated cost based on Euclidean distances.")

    def test_tour_contains_total_of_five_cities_visited(self):
        unique_cities = set(self.tour)
        self.assertTrue(len(unique_cities) == 5, "Tour should consist of exactly 5 unique cities.")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestKTravelingSalesman("test_tour_starts_and_ends_at_depot"))
    suite.addTest(TestKTravelingSalesman("test_tour_length"))
    suite.addTest(TestKTravelingSalesman("test_tour_distance"))
    suite.addTest(TestKTravelingSalesman("test_tour_contains_total_of_five_cities_visited"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")