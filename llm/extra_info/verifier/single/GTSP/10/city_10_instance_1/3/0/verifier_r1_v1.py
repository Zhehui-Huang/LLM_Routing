import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.city_positions = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44),
                               (17, 69), (95, 89)]
        self.groups = [[5, 6, 7], [2, 3], [1, 9], [4, 8]]
        self.solution = [0, 5, 2, 9, 8, 0]
        self.reported_cost = 183.98559431675523

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution[0], 0)
        self.assertEqual(self.solution[-1], 0)

    def test_visits_one_from_each_group(self):
        visited_groups = []
        for city in self.solution[1:-1]:
            for i, group in enumerate(self.groups):
                if city in group:
                    visited_groups.append(i)
        self.assertEqual(len(set(visited_groups)), len(self.groups))

    def test_correct_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.solution) - 1):
            calculated_cost += euclidean_distance(
                self.city_positions[self.solution[i]],
                self.city_positions[self.solution[i + 1]]
            )
        self.assertAlmostEqual(calculated_cost, self.reported_cost)

    def test_tour_validity(self):
        self.test_starts_and_ends_at_depot()
        self.test_visits_one_from_each_group()
        self.test_correct_travel_cost()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_starts_and_ends_at_depot'))
    suite.addTest(TestTravelingSalesmanSolution('test_visits_one_from_each_group'))
    suite.addTest(TestTravelingSalesmanSolution('test_correct_travel_cost'))
    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")