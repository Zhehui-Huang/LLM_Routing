import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56),
            1: (53, 42),
            2: (1, 95),
            3: (25, 61),
            4: (69, 57),
            5: (6, 58),
            6: (12, 84),
            7: (72, 77),
            8: (98, 95),
            9: (11, 0),
            10: (61, 25),
            11: (52, 0),
            12: (60, 95),
            13: (10, 94),
            14: (96, 73),
            15: (14, 47),
            16: (18, 16),
            17: (4, 43),
            18: (53, 76),
            19: (19, 72)
        }
        self.tour = [0, 1, 4, 7, 18, 12, 14, 8, 2, 13, 6, 19, 3, 15, 5, 17, 16, 9, 11, 10, 0]
        self.reported_cost = 521.1406925345192
    
    def test_tour_start_end_depot(self):
        # Requirement 2
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_all_cities_visited_once(self):
        # Requirement 3
        for city in range(1, 20):  # No need to check depot city, as it is start and end
            self.assertEqual(self.tour.count(city), 1)
    
    def test_correct_tour_length(self):
        # Requirement 1
        self.assertEqual(len(set(self.tour)), 20)  # Including depot city
        self.assertEqual(len(self.tour), 21)  # Additional one for return

    def test_total_travel_cost(self):
        # Requirement 4 and 8
        cost = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i + 1]]
            cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.assertAlmostEqual(cost, self.reported_cost)

unittest.TextTestResult.stream = open("test_output.txt", "w")
tests = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
test_result = unittest.TextTestRunner(verbosity=2).run(tests)

if test_result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")