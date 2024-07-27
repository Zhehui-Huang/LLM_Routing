import unittest
import math

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
            (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
            (43, 67), (58, 48), (58, 27), (37, 69)
        ]
        
        self.tours = [
            [0, 0],
            [1, 10, 1],
            [2, 13, 2],
            [3, 8, 12, 3],
            [4, 11, 15, 4],
            [5, 14, 5],
            [6, 6],
            [7, 9, 7]
        ]
        
        self.tour_costs = [0.0, 14.142135623730951, 18.110770276274835, 33.94039963350503, 
                           26.480522629341756, 16.97056274847714, 0.0, 20.09975124224178]

        self.expected_total_cost = 129.7441421535715

    def calculate_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def test_solution(self):
        all_cities = set(range(16))
        visited_cities = set()
        computed_total_cost = 0

        for tour, expected_cost in zip(self.tours, self.tour_costs):
            # Check the tour starts and ends at the same depot
            self.assertEqual(tour[0], tour[-1], f"Robot should start and end at the same depot for tour {tour}")
            tour_cost = 0

            # Calculate total travel cost and validate each visited city
            last_city = tour[0]
            for city in tour[1:]:
                visited_cities.add(city)
                tour_cost += self.calculate_distance(last_city, city)
                last_city = city

            # Check individual tour costs
            computed_total_cost += tour_cost
            self.assertAlmostEqual(tour_cost, expected_cost, places=5, 
                                   msg="Tour cost does not match expected value")
        
        # Test if all cities are visited exactly once
        self.assertEqual(visited_cities, all_cities, "Not all cities visited exactly once")
        
        # Check the sum of costs
        self.assertAlmostEqual(computed_total_cost, self.expected_total_cost, places=5,
                               msg="Overall cost does not match the expected total cost")

if __name__ == '__main__':
    unittest.main()