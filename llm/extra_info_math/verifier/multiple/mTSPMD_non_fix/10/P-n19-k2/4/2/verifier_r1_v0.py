import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
            (61, 33), (62, 63), (63, 69), (45, 35)
        ]
        self.robot_0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
        self.robot_1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
        self.expected_total_cost = 241.29056448233058
    
    def test_starts_at_depot(self):
        self.assertEqual(self.robot_0_tour[0], 0)
        self.assertEqual(self.robot_1_tour[0], 0)
        
    def test_cities_visited_once(self):
        all_cities = set(range(len(self.coordinates)))
        visited_cities = set(self.robot_0_tour[1:-1] + self.robot_1_tour[1:-1])  # Ignore depots start/end in tour
        self.assertSetEqual(visited_cities, all_cities - {0})

    def test_end_at_any_city(self):
        allowed_ends = {0}
        self.assertIn(self.robot_0_tour[-1], allowed_ends)
        self.assertIn(self.robot_1_tour[-1], allowed_ends)

    def test_minimize_total_travel_cost(self):
        def calculate_tour_cost(tour, coordinates):
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            return cost

        total_cost = (calculate_tour_cost(self.robot_0_tour, self.coordinates) + 
                      calculate_tour_cost(self.robot_1_tour, self.coordinates))
        self.assertAlmostEqual(total_cost, self.expected_total_cost, places=5)

    def test_no_sub_tours(self):
        def has_sub_tours(tour):
            # To check for sub-tours, make sure no subset of nodes exists that circles back to its own start
            visited = set()
            for city in tour[:-1]:  # Ignore last element as it is return to depot
                if city in visited:
                    return True
                visited.add(city)
            return False

        self.assertFalse(has_sub_tours(self.robot_0_tour))
        self.assertFalse(has_sub_tours(self.robot_1_tour))

# Run the tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)