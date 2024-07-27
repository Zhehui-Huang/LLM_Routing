import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # City coordinates - index represents the city number
        self.cities = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ]
        
        # Provided tours
        self.tours = [
            [0, 13, 21, 17, 9, 5, 1, 0],
            [0, 14, 18, 2, 6, 10, 0],
            [0, 15, 7, 3, 11, 19, 0],
            [0, 16, 20, 12, 8, 4, 0]
        ]
        
        # Expected distances
        self.expected_costs = [190.21371050238986, 149.93963794115078, 183.24946422163586, 153.00366685556634]
        
        # A set of all city indices except the depot
        self.all_cities = set(range(1, 22))

    def test_each_city_visited_exactly_once(self):
        visited_cities = set()
        for tour in self.tours:
            # Remove the depot city (index 0) and add remaining cities
            visited_cities.update(tour[1:-1])
        
        self.assertEqual(visited_cities, self.all_cities)

    def test_tours_start_and_end_at_depot(self):
        for tour in self.tours:
            self.assertEqual(tour[0], 0)  # Start at depot
            self.assertEqual(tour[-1], 0) # End at depot

    def test_travel_costs(self):
        for tour, expected_cost in zip(self.tours, self.expected_costs):
            actual_cost = 0
            for i in range(len(tour)-1):
                actual_cost += euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            self.assertAlmostEqual(actual_cost, expected_cost, places=5)

if __name__ == "__main__":
    result = unittest.main(argv=[''], exit=False)
    if len(result.result.failures) == 0 and len(result.result.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")