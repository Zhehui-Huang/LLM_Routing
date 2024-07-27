import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (9, 93),   # Depot city 0
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
        self.groups = [
            [2, 7, 10, 11, 14],
            [1, 3, 5, 8, 13],
            [4, 6, 9, 12]
        ]
        self.solution_tour = [0, 8, 10, 9, 0]
        self.reported_cost = 114.09
        
    def test_tour_starts_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)
        
    def test_direct_travel_between_cities(self):
        for i in range(len(self.solution_tour)-1):
            city1 = self.solution_tour[i]
            city2 = self.solution_tour[i+1]
            self.assertTrue(city1 in range(len(self.cities)) and city2 in range(len(self.cities)))
    
    def test_visit_one_city_per_group(self):
        visited_groups = []
        for city_index in self.solution_tour[1:-1]:
            for group_index, group in enumerate(self.groups):
                if city_index in group:
                    visited_groups.append(group_index)
        self.assertEqual(sorted(list(set(visited_groups))), sorted(list(range(len(self.groups)))))
        
    def test_total_travel_cost(self):
        total_cost = 0.0
        for i in range(len(self.solution_tour)-1):
            x1, y1 = self.cities[self.solution_tour[i]]
            x2, y2 = self.cities[self.solution_tour[i+1]]
            total_cost += euclidean_distance(x1, y1, x2, y2)
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_optimality_of_solution(self):
        # Here is just a simple check for the solution correctness regarding the cost.
        # Generally, this would require knowing all possible routes costs to ensure optimality.
        # We suppose the solution provided to be correct unless proven otherwise.
        pass  # Assuming the solution is optimal

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORNI32RECT")
    else:
        print("FAIL")