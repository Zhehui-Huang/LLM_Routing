import unittest
import math

class TestTourSolution(unittest.TestCase):
    def test_start_end_at_depot(self):
        tour = [0, 6, 9, 19, 10, 4, 0]
        self.assertEqual(tour[0], 0)  # start at depot
        self.assertEqual(tour[-1], 0)  # end at depot

    def test_tour_length(self):
        tour = [0, 6, 9, 19, 10, 4, 0]
        self.assertEqual(len(set(tour[1:-1])), 6)  # 6 unique cities plus the depot city

    def test_tour_format(self):
        tour = [0, 6, 9, 19, 10, 4, 0]
        self.assertIsInstance(tour, list)  # tour format as list
        self.assertTrue(all(isinstance(city, int) for city in tour))  # city indices are integers

    def test_correct_total_travel_cost(self):
        tour = [0, 6, 9, 19, 10, 4, 0]
        positions = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
            (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
            (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        calculated_cost = 0
        for i in range(1, len(tour)):
            x1, y1 = positions[tour[i - 1]]
            x2, y2 = positions[tour[i]]
            calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        rounded_calculated_cost = round(calculated_symbolic_cost, 2)
        self.assertEqual(rounded_calculated_cost, 266.41)  # provided total travel cost

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTourSolution("test_start_end_at_depot"))
    suite.addTest(TestTourSolution("test_tour_length"))
    suite.addTest(TestTourSolution("test_tour_format"))
    suite.addTest(TestTourElementWiseDerived("test_correct_total_travel_cost"))

    result = unittest.TextTestRunner().run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")