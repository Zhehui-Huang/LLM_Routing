import unittest
from math import sqrt

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (16, 90),  # depot city 0
            (43, 99),
            (80, 21),
            (86, 92),
            (54, 93),
            (34, 73),
            (6, 61),
            (86, 69),
            (30, 50),
            (35, 73),
            (42, 64),
            (64, 30),
            (70, 95),
            (29, 64),
            (32, 79)
        ]
        self.solution_tour = [6, 8, 13, 14, 5, 9, 10, 11, 2, 7, 3, 12, 4, 1, 0, 6]
        self.reported_cost = 308.75733664843295

    def test_tour_visits_all_cities_once(self):
        cities_visited = set(self.solution_tour)
        all_cities = set(range(15))
        self.assertTrue(all(city in cities_visited for city in all_cities))

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_travel_costs(self):
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            from_city = self.solution_tour[i]
            to_city = self.solution_tour[i + 1]
            from_coord = self.coordinates[from_city]
            to_coord = self.coordinates[to_city]
            calculated_cost += sqrt((from_coord[0] - to_coord[0]) ** 2 + (from_coord[1] - to_coord[1]) ** 2)
        self.assertAlmostEqual(calculated_i_cost, self.reported_cost, places=5)

def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTravelingSalesmanSolution('test_tour_visits_all_cities_once'))
    test_suite.addTest(TestTravelingSalesmanSolution('test_tour_starts_and_ends_at_depot'))
    test_suite.addTest(TestTravelingSalesmanSolution('test_travel_costs'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()