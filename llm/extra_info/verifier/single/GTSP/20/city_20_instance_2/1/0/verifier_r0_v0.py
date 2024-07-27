import unittest
import math

class TestTravelingSalesmanProblem(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = {
            0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
            5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
            10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
            15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
        }
        
        self.city_groups = {
            0: [7, 10, 11, 12],
            1: [3, 8, 13, 16],
            2: [2, 4, 15, 18],
            3: [1, 9, 14, 19],
            4: [5, 6, 17]
        }

        self.tour = [0, 11, 16, 18, 19, 6, 0]
        self.calculated_total_cost = 162.38

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_visits_one_city_from_each_group(self):
        visited = set(self.tour[1:-1])
        for group in self.city_groups.values():
            self.assertTrue(any(city in visited for city in group))

    def test_travel_cost(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities_coordinates[city1]
            x2, y2 = self.cities_coordinates[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.tour[i], self.tour[i+1])
        self.assertAlmostEqual(total_cost, self.calculated_total_cost, places=2)
        
    def test_correct_tour_validation(self):
        is_correct = True
        try:
            self.test_tour_starts_and_ends_at_depot()
            self.test_visits_one_city_from_each_group()
            self.test_travel_cost()
        except AssertionError:
            is_correct = False
        self.assertTrue(is_correct)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanProblem('test_correct_tour_validation'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

# Running the tests
print(run_tests())