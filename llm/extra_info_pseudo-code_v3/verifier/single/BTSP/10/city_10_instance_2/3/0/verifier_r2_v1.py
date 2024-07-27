import unittest
from typing import List, Tuple
from math import sqrt

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    """
    Calculate the Euclidean distance between two cities.
    """
    return sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour: List[int], cities: List[Tuple[int, int]], total_cost: float, max_dist: float) -> bool:
    """
    Validate the tour against the provided requirements.
    """
    # Check if tour starts and ends at the depot city and visits each city exactly once
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != len(cities):
        return False
    
    # Calculate the total cost and maximum distance
    calculated_total_cost = 0.0
    calculated_max_dist = 0.0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        calculated_total_cost += distance
        if distance > calculated_max_dist:
            calculated_max_dist = distance
    
    # Check if provided total cost and maximum distance match calculated values
    if not (abs(calculated_total_cost - total_cost) < 1e-5 and abs(calculated_max_dist - max_dist) < 1e-5):
        return False
    
    return True

class TestBottleneckTSP(unittest.TestCase):
    def test_solution(self):
        cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), 
                  (23, 95), (20, 56), (49, 29), (13, 17)]
        
        tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
        total_travel_cost = 418.32344417340323
        maximum_distance = 69.42621983083913
        
        # Verify the solution
        valid_tour = verify_tour(tour, cities, total_travel_cost, maximum_distance)
        
        if valid_tour:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)