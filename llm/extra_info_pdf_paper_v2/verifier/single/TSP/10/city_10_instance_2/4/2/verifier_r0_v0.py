import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (90, 3),  # City 0: Depot
            (11, 17), # City 1
            (7, 27),  # City 2
            (95, 81), # City 3
            (41, 54), # City 4
            (31, 35), # City 5
            (23, 95), # City 6
            (20, 56), # City 7
            (49, 29), # City 8
            (13, 17)  # City 9
        ]
        self.solution_tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
        self.calculated_cost = 384.7863591860825
        
    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour does not start at the depot")
        self.assertEqual(self.solution_tour[-1], 0, "Tour does not end at the depot")
        
    def test_visit_each_city_once(self):
        tour_without_depot = self.solution_tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 9, "Not all cities are visited exactly once")
        self.assertEqual(set(range(1, 10)), unique_cities, "Cities other than 1 to 9 are visited or some are missed")
        
    def test_calculate_total_travel_cost(self):
        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i + 1]
            total_cost += calculate_distance(self.coordinates[city1], self.coordinates[city2])
        self.assertAlmostEqual(total_cost, self.calculated_cost, places=5, msg="Total cost calculation error")
        
    def test_correct_output_format(self):
        self.assertIsInstance(self.solution_tour, list, "Tour should be in list format")
        self.assertTrue(all(isinstance(x, int) for x in self.solution_tour), "Tour should be a list of integers")
        self.assertIsInstance(self.calculated_cost, float, "Total travel cost should be a float")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")