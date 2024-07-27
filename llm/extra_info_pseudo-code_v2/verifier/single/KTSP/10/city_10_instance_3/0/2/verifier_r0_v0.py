import math
from unittest import TestCase, main

class TestTSPSolution(TestCase):
    def setUp(self):
        self.cities = {
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
        self.tour = [0, 8, 3, 7, 1, 4, 0]
        self.total_cost = 128.73130793605634
    
    def test_starts_and_ends_with_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visits_exactly_seven_cities(self):
        unique_cities = len(set(self.tour))
        self.assertEqual(unique_cities, 7)

    def test_total_travel_cost(self):
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            city1 = self.tour[i - 1]
            city2 = self.tour[i]
            calculated_cost += math.sqrt((self.cities[city1][0] - self.cities[city2][0]) ** 2 + (self.cities[city1][1] - self.cities[city2][1]) ** 2)
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)
    
    def test_output_format(self):
        self.assertIsInstance(self.tour, list)
        for city in self.tour:
            self.assertIsInstance(city, int)

if __name__ == "__main__":
    test_suite = main(exit=False)
    if test_suite.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")