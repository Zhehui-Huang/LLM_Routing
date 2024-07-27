import unittest
import math

class TestKTSPSolution(unittest.TestCase):
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
        self.tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
        self.reported_cost = 235.38

    def calculate_total_distance(self, tour):
        total_distance = 0
        for i in range(len(tour) - 1):
            x1, y1 = self.cities[tour[i]]
            x2, y2 = self.cities[tour[i+1]]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            total_distance += distance
        return total_distance

    def test_tour_start_end(self):
        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_8_cities(self):
        # Check if exactly 8 cities are visited including the depot city
        self.assertEqual(len(set(self.tour)), 8)

    def test_distance_calculation(self):
        # Check if the total travel cost is calculated correctly
        calculated_cost = self.calculate_total_distance(self.tour)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2)

    def test_all_cities_exist(self):
        # Check if all cities in the tour exist in the defined city coordinates
        all_exist = all(city in self.cities for city in self.tour)
        self.assertTrue(all_exist)

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTSPSolution('test_tour_start_end'))
    test_suite.addTest(TestKTSPSolution('test_visit_8_cities'))
    test_suite.addTest(TestKTSPSolution('test_distance_calculation'))
    test_suite.addTest(TestKTSPSolution('test_all_cities_exist'))

    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
    if len(results.failures) == 0 and len(results.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")

run_tests()