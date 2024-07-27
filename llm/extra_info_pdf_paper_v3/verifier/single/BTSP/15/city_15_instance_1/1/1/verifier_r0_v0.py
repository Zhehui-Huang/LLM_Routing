import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, cities):
    visited = set(tour)
    # Check if all cities are visited exactly once and starts/ends at 0
    condition_1 = len(visited) == len(cities) and all(i in visited for i in range(len(cities)))
    condition_2 = tour[0] == 0 and tour[-1] == 0
    
    # Check maximum distance to minimize in the tour
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    return condition_1 and condition_2, total_cost, max_distance

class TestTourSolution(unittest.TestCase):
    def test_tour_solution(self):
        # Provided tour solution
        solution_tour = [0, 5, 0, 4, 10, 4, 0, 9, 3, 7, 1, 6, 13, 2, 11, 12, 11, 2, 8, 14, 8, 2, 13, 6, 1, 7, 3, 9, 0]
        cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), (4, 60),
                  (78, 82), (83, 96), (60, 50), (98, 1)]
        
        # Check if the robot visits each city exactly once and starts/ends at the depot city
        is_valid, total_cost, max_distance = validate_tour(solution_tour, cities)

        # Assert all conditions
        self.assertTrue(is_valid)
        self.assertAlmostEqual(total_cost, 544.3, places=1)
        self.assertAlmostEqual(max_distance, 42.3, places=1)

if __name__ == '__main__':
    unittest.main()