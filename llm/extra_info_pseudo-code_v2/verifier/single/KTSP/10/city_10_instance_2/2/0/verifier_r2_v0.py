import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        self.tour = [0, 8, 9, 4, 7, 5, 0]
        self.reported_cost = 223.3175394997635

    def test_start_and_end_city(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_length(self):
        # Requirement 2
        self.assertEqual(len(self.tour), 7)  # Includes the depot twice

    def test_tour_exclusivity(self):
        # Ensuring no cities except depot are repeated
        non_depot_cities = self.tour[1:-1]
        self.assertEqual(len(non_depot_cities), len(set(non_depot_cities)))

    def test_travel_cost(self):
        # Requirement 4
        def calculate_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        calculated_cost = sum(calculate_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

    def test_output_format(self):
        # Requirement 5
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)
        # Validate indices within the range of available cities
        self.assertTrue(all(city in self.cities for city in self.tour))

def main():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestKTSPSolution))

    # run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()