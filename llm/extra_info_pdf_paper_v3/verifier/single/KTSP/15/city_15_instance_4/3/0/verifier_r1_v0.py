import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 
            4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62), 
            8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 
            12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 0]
        self.total_travel_cost = 241.29
    
    def euclidean_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0) # End at depot
    
    def test_tour_visits_exactly_12_cities(self):
        unique_cities = set(self.tour)
        self.assertEqual(len(unique_cities), 12)

    def calculate_actual_travel_cost(self):
        cost = 0
        for i in range(len(self.tour) - 1):
            start_city = self.cities[self.tour[i]]
            end_city = self.cities[self.tour[i + 1]]
            cost += self.euclidean_distance(start_city, end_city)
        return round(cost, 2)
    
    def test_total_travel_cost_calculation(self):
        calculated_cost = self.calculate_actual_travel_cost()
        self.assertEqual(calculated_cost, self.total_travel_cost)

    def test_all_requirements(self):
        self.test_tour_start_end_at_depot()
        self.test_tour_visits_exactly_12_cities()
        self.test_total_travel_cost_calculation()
    
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestKTSPSolution('test_all_requirements'))
    runner = unittest.TextTestRunner()

    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
      print("FAIL")