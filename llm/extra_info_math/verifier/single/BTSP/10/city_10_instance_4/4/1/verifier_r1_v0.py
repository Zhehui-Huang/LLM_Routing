import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
        self.reported_total_cost = 337.17
        self.reported_max_distance = 61.68

    def test_starts_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        core_tour = self.tour[1:-1]  # ignore start and end depot visit
        self.assertEqual(len(set(core_tour)), len(core_tour))  # check no repetitions
        self.assertEqual(set(core_tour), set(range(1, 10)))  # check all cities are visited

    def test_total_and_maximum_travel_cost(self):
        real_costs = [euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
                      for i in range(len(self.tour) - 1)]
        total_cost = sum(real_costs)
        max_cost = max(real_costs)
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=2)
        self.assertAlmostEqual(max_cost, self.reported_max_distance, places=2)

# Running the unit test
if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTourSolution))
    result = unittest.TextTestRunner().run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")