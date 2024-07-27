import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
            (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
            (28, 49), (91, 94), (51, 58), (30, 48)
        ]
        self.tour = [0, 14, 16, 19, 11, 7, 10, 3, 4, 1, 17, 5, 2, 9, 15, 13, 18, 8, 6, 12, 0]
        self.reported_cost = 492.29
        
    def calculate_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    def calculate_total_cost(self, tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += self.calculate_distance(self.cities[tour[i]], self.cities[tour[i+1]])
        return total_cost
        
    def test_tour_start_and_end_at_depot(self):
        # [Requirement 3] & [Requirement 4]
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_all_cities_visited_once(self):
        # [Requirement 1]
        city_visits = set(self.tour[1:-1])
        self.assertEqual(len(city_visits), 19)  # Exclude start/end city, checking all other unique cities
        
    def test_correct_total_travel_cost(self):
        # [Requirement 2] & [Requirement 5]
        calculated_cost = self.calculate_total_cost(self.tour)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=1)

unittest.main(argv=[''], exit=False)