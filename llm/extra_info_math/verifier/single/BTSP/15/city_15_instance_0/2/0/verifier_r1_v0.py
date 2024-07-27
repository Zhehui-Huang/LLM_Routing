import unittest
from math import sqrt

def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tour(tour, distances, total_cost, max_distance):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check each city is visited exactly once, excluding starting/ending depot city
    cities_visited = set(tour[1:-1])
    if len(cities_visited) != 14:
        return "FAIL"
    
    # Check tour is listed correctly
    if len(tour) < 2 or tour[0] != tour[-1]:
        return "FAIL"
    
    # Compute and check the total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        distance = distances[tour[i]][tour[i+1]]
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    if not (abs(calculated_cost - total_cost) < 1e-5 and abs(calculated_max_distance - max_distance) < 1e-5):
        return "FAIL"
    
    return "CORRECT"

class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        # Coordinates of the cities including the depot city 0
        coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
                       (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]
        
        # Calculate distances between each pair of cities
        distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]
        
        # Provided solution details
        tour = [0, 10, 1, 8, 0, 10, 1, 8, 0, 10, 1, 8, 0, 10, 1, 0]
        total_travel_cost = 373.26667878524154
        max_distance = 42.01190307520001
        
        # Verify the tour
        result = verify_tour(tour, distances, total_travel_cost, max_distance)
        self.assertEqual(result, "CORRECT")

unittest.main(argv=[''], verbosity=2, exit=False)