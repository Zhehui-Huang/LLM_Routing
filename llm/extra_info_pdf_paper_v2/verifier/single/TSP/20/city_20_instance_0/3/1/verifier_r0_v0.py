import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
            5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
            10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 
            14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 
            19: (93, 15)
        }
        self.tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
        self.reported_cost = 349.1974047195548
        
    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 19)  # There should be 19 unique cities visited

    def test_calculate_travel_cost(self):
        total_calculated_cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total_calculated_cost += distance
        self.assertAlmostEqual(total_calculated_cost, self.reported_cost, places=5)
     
    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        self.assertGreater(len(self.tour), 1)
        all_are_integers = all(isinstance(city, int) for city in self.tour)
        self.assertTrue(all_are_integers)
        
    def runTest(self):
        self.test_start_end_at_depot()
        self.test_visit_each_city_once()
        self.test_calculate_travel_cost()
        self.test_output_format()

# Running the test
test = TestTSPSolution()
result = unittest.TextTestRunner().run(test)
failure_count = len(result.failures) + len(result.errors)
if failure_count == 0:
    print("CORRECT")
else:
    print("FAIL")