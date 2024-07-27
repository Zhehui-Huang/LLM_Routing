import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

class TestTSPSolution(unittest.TestCase):
    
    def test_tsp_solution(self):
        cities = {
            0: (26, 60),
            1: (73, 84),
            2: (89, 36),
            3: (15, 0),
            4: (11, 10),
            5: (69, 22),
            6: (28, 11),
            7: (70, 2),
            8: (47, 50),
            9: (60, 29),
            10: (29, 26),
            11: (85, 68),
            12: (60, 1),
            13: (71, 73),
            14: (82, 47),
            15: (19, 25),
            16: (75, 9),
            17: (52, 54),
            18: (64, 72),
            19: (14, 89)
        }
        
        given_tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
        given_total_cost = 410.04
        given_max_distance = 89.01
        
        # Check if the tour starts and ends at the depot
        self.assertEqual(given_tour[0], 0)
        self.assertEqual(given_tour[-1], 0)
        
        # Check if each city is visited exactly once
        for city in range(20):
            self.assertEqual(given_tour.count(city), 1)
        
        # Calculate the total travel cost and max distance
        total_cost = 0
        max_distance_between_cities = 0
        for i in range(len(given_tour) - 1):
            current_city = given_tour[i]
            next_city = given_tour[i + 1]
            distance = euclidean_distance(cities[current_city], cities[next_city])
            total_cost += distance
            max_distance_between_cities = max(max_distance_between_cities, distance)
        
        # Check if the calculated total cost and max distance matches the solution provided
        self.assertAlmostEqual(total_cost, given_total_cost, places=2)
        self.assertAlmostEqual(max_distance_between_cities, given_max_distance, places=2)

if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")