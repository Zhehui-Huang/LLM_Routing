import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        total_cost += euclidean_distance(cities[city_index_1], cities[city_index_2])
    return total_cost

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        cities = [
            (9, 93),   # City 0
            (8, 51),   # City 1
            (74, 99),  # City 2
            (78, 50),  # City 3
            (21, 23),  # City 4
            (88, 59),  # City 5
            (79, 77),  # City 6
            (63, 23),  # City 7
            (19, 76),  # City 8
            (21, 38),  # City 9
            (19, 65),  # City 10
            (11, 40),  # City 11
            (3, 21),   # City 12
            (60, 55),  # City 13
            (4, 39)    # City 14
        ]
        
        tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
        expected_total_cost = 373.97393412233544
        
        # Check if the tour starts and ends at the depot (city 0)
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
        
        # Check if each city except depot is visited exactly once
        for city_index in range(1, 15):
            self.assertEqual(tour.count(city_index), 1)
        
        # Check if the total travel cost is calculated correctly
        total_cost_calculated = calculate_total_travel_cost(cities, tour)
        self.assertAlmostEqual(total_cost_calculated, expected_total_cost, places=6)

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution))
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")