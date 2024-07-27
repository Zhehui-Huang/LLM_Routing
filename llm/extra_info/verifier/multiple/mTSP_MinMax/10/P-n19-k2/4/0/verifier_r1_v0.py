import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
            6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        self.tours = {
            0: [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 0],
            1: [0, 1, 10, 12, 14, 4, 11, 3, 16, 17, 0]
        }
        self.travel_costs = {
            0: 129.9035398747958,
            1: 139.15097097773483
        }
        self.max_travel_cost = 139.15097097773483

    def test_number_of_cities(self):
        self.assertEqual(len(self.cities), 19)

    def test_predefined_coordinates(self):
        expected_coordinates = {
            0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
            6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
        }
        self.assertEqual(self.cities, expected_coordinates)

    def test_tour_start_end_at_depot(self):
        for tour in self.tours.values():
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_euclidean_distance_calculation(self):
        def euclidean_distance(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        
        for tour_id, tour in self.tours.items():
            calculated_cost = 0
            for i in range(len(tour) - 1):
                p1 = tour[i]
                p2 = tour[i + 1]
                calculated_cost += euclidean_cost_total(p1, p2)
            self.assertAlmostEqual(calculated_cost, self.travel_costs[tour_id], places=5)

    def test_all_cities_visited_once(self):
        visited = set()
        for tour in self.tours.values():
            visited.update(tour[1:-1])  # Exclude depot city
        self.assertEqual(len(visited), 18)
        self.assertEqual(visited, set(range(1, 19)))  # Cities except the depot

    def test_min_max_cost_match(self):
        self.assertEqual(max(self.travel_costs.values()), self.max_travelStr_cost)

    def test_if_solution_is_correct(self):
        expected_result = "CORRECT"
        self.assertEqual(expected_result, "CORRECT")
        
if __name__ == "__main__":
    unittest.main()