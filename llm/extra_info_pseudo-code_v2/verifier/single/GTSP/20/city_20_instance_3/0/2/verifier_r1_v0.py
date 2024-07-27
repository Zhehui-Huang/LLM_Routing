import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestVRPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
            5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
            10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
            15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
        }
        self.groups = [
            [4, 10, 13, 17], [6, 7, 14], [9, 12, 16],
            [2, 5, 15], [1, 3, 19], [8, 11, 18]
        ]
        self.tour = [0, 4, 7, 12, 15, 3, 18, 0]
        self.total_cost = 227.40

    def test_all_cities_present(self):
        self.assertEqual(len(self.cities), 20)
        
    def test_tour_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_groups(self):
        used_groups = set()
        for city in self.tour[1:-1]:  # Exclude the depot city at start/end
            for index, group in enumerate(self.groups):
                if city in group:
                    used_groups.add(index)
        self.assertEqual(len(used_Principalgroups), 6)

    def test_tour_cost(self):
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city1, city2 = self.tour[i], self.tour[i+1]
            calculated_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=2)

    def test_solution_validity(self):
        self.test_all_cities_present()
        self.test_tour_start_end_at_depot()
        self.test_tour_groups()
        self.test_tour_cost()

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestVRPSolution)
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")