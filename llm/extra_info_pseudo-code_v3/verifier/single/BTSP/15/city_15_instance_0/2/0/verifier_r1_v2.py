import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, expected_max_dist):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once (except the depot city)
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return False
    
    # Calculate maximum distance between consecutive cities in the tour
    max_dist = max(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Check if the maximum distance is approximately equal to the expected maximum distance
    return abs(max_dist - expected_max_path) < 0.0001

class TestBTSPTour(unittest.TestCase):
    def test_tour_verification(self):
        cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
                  (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
        tour = [0, 1, 4, 7, 3, 5, 2, 6, 13, 10, 9, 11, 12, 14, 8, 0]
        expected_max_path = 42.37924020083418
        result = verify_tour(cities, tour, expected_max_path)
        self.assertTrue(result)

if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False)
    if result.result.errors or result.result.failures:
        print("FAIL")
    else:
        print("CORRECT")