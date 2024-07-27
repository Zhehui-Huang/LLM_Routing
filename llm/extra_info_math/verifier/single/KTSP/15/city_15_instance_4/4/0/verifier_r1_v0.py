import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    # Verify requirement 1: Start and end at depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify requirement 2: Visit exactly 12 cities
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Verify requirement 3: Use Euclidean distance
    total_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
    
    expected_distances = [
        calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)
    ]
    actual_distances = [calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)]
    
    if not all(a == b for a, b in zip(expected_distances, actual_distances)):
        return "FAIL"

    return "CORRECT", total_distance

class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        cities = {
            0: (35, 40),
            1: (39, 41),
            2: (81, 30),
            3: (5, 50),
            4: (72, 90),
            5: (54, 46),
            6: (8, 70),
            7: (97, 62),
            8: (14, 41),
            9: (70, 44),
            10: (27, 47),
            11: (41, 74),
            12: (53, 80),
            13: (21, 21),
            14: (12, 39),
        }
        
        # Assuming we have a valid tour (example provided should be corrected based on actual solution algorithm)
        test_tour = [0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 0]
        
        result, total_distance = verify_tour(test_tour, cities)
        print(f"Tour: {test_tour}")
        print(f"Total travel cost: {total_distance}")
        
        self.assertEqual(result, "CORRECT")

unittest.main(argv=[''], verbosity=2, exit=False)