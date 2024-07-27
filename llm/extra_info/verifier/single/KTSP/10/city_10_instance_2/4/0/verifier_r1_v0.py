import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, travel_distance, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour should start and end at depot city 0."
    
    if len(set(tour)) != 6:
        return False, "Tour should visit exactly 6 cities."
    
    if len(tour) != 7:
        return False, "Tour length should be 7 including start and end at depot."
  
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
    if abs(calculated_cost - travel_distance) > 1e-5:
        return False, f"Calculated travel cost {calculated_cost} does not match given {travel_distance}."
    
    return True, ""

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
        tour = [0, 8, 5, 2, 1, 9, 0]
        travel_distance = 183.85354044487238
        
        result, message = validate_solution(tour, travel_distance, cities)
        assert result, message
        
        print("CORRECT" if result else "FAIL")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)