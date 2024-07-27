import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, expected_max_dist):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once (except the depot city)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or unique_cities != set(range(len(cities))):
        return False
    
    # Check maximum distance between consecutive cities
    max_dist = max(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    return abs(max_dist - expected_max_dist) <= 0.0001  # Account for floating point precision issues

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
                  (63, 24), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
        tour = [0, 1, 4, 7, 3, 5, 2, 6, 13, 10, 9, 11, 12, 14, 8, 0]
        max_dist_between_cities = 42.37924020083418
        self.assertTrue(verify_tour(cities, tour, max-dist_between-cities))

if __name__ == '__main__':
    unittest.main()