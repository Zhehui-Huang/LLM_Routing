import unittest
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
            (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
            (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
            (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.n_cities = len(self.coordinates)

        # Simulate a solution - for example purposes
        self.solution_tour = [0, 3, 1, 2, 0]  # Example incorrect or correct tour
        self.solution_total_cost = 100
        self.solution_max_distance = 40

    def test_number_of_cities(self):
        self.assertEqual(self.n_cities, 20, "Should have 20 cities")

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at city 0")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at city 0")

    def test_visit_each_city_exactly_once_plus_return(self):
        tour_without_return = self.solution_tour[:-1]
        self.assertCountEqual(tour_without_return, list(range(1, self.n_cities)), 
                              "Each city must be visited exactly once and only depot city can appear twice (start and end)")

    def test_calculate_total_travel_cost(self):
        calculated_cost = sum(euclidean_distance(self.coordinates[self.solution_tour[i]], 
                                                 self.coordinates[self.solution_tour[i + 1]])
                               for i in range(len(self.solution_tour) - 1))
        self.assertAlmostEqual(self.solution_total_cost, calculated_cost, 
                               "Total travel cost should be correct as per euclidean distances")

    def test_max_distance_between_consecutive_cities(self):
        calculated_max_distance = max(euclidean_distance(self.coordinates[self.solution_tour[i]], 
                                                         self.coordinates[self.solution_tour[i + 1]])
                                      for i in range(len(self.solution_tour) - 1))
        self.assertEqual(self.solution_max_distance, calculated_max_distance, 
                         "Maximum distance between consecutive cities should match the given output")

if __name__ == '__main__':
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution))
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")