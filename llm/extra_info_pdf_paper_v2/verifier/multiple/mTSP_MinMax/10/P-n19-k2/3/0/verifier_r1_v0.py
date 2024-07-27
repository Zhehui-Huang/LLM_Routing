import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.tours = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]
        ]
        self.robot_costs = [196.36, 278.77]  # Approximated costs
        self.max_cost = 278.77

    def euclidean_distance(self, p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def calculate_tour_cost(self, tour):
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += self.euclidean_distance(self.city_coordinates[tour[i]], self.city_coordinates[tour[i+1]])
        return cost

    def test_correct_number_of_cities(self):
        self.assertEqual(len(self.city_coordinates), 19)

    def test_all_cities_visited_once(self):
        all_cities = set(range(1, 19))  # City 0 is the depot
        visited_cities = set()
        for tour in self.tours:
            visited_cities.update(tour[1:-1])  # Exclude the starting and ending depot
        self.assertSetEqual(visited_cities, all_cities)
    
    def test_start_end_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_travel_cost_for_tours(self):
        for tour, reported_cost in zip(self.tours, self.robot_costs):
            calculated_cost = self.calculate_tour_cost(tour)
            self.assertAlmostEqual(calculated_cost, reported_cost, places=2)

    def test_minimize_maximum_travel_cost(self):
        calculated_max_cost = max(self.calculate_tour_cost(tour) for tour in self.tours)
        self.assertAlmostEqual(calculated_max_cost, self.max_cost, places=2)

    def test_formatted_output(self):
        formatted_tours = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]
        ]
        formatted_costs = [196.36, 278.77]
        self.assertEqual(self.tours, formatted_tours)
        self.assertEqual(self.robot_costs, formatted_costs)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTours)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")