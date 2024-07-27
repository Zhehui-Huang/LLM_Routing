import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour_and_cost(tour, cities, groups, stated_cost):
    # Check if the tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
    if len(visited_groups) != len(groups):
        return False

    # Calculate and compare the tour travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(total_cost - stated_cost) > 1e-5:
        return False
    
    return True

class TestRobotTour(unittest.TestCase):
    def test_correct_solution(self):
        cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        groups = [
            [3, 6], 
            [5, 8], 
            [4, 9], 
            [1, 7], 
            [2]
        ]
        tour = [0, 3, 5, 2, 1, 9, 0]
        stated_cost = 273.3072642077373
        self.assertTrue(check_tour_and_cost(tour, cities, groups, stated_cost))
        
if __name__ == '__main__':    
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")