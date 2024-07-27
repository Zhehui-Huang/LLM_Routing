import unittest
import math

# Setting up the city coordinates as given
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

class TestRobotTours(unittest.TestCase):
    def calculate_distance(self, city1, city2):
        return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

    def test_completeness_of_visit(self):
        """ Test if all cities are visited exactly once """
        tours = [[0, 6, 18, 5, 7, 2, 9, 15, 13, 17], [1, 10, 12, 14, 4, 11, 3, 8, 16]]
        visited = [city for tour in tours for city in tour]
        self.assertEqual(sorted(visited), list(range(19)))

    def test_start_and_end_points(self):
        """ Test whether robots start at the designated depots, and end at any city """
        tour0 = [0, 6, 18, 5, 7, 2, 9, 15, 13, 17]
        tour1 = [1, 10, 12, 14, 4, 11, 3, 8, 16]
        self.assertEqual(tour0[0], 0)  # Starts at depot 0
        self.assertEqual(tour1[0], 1)  # Starts at depot 1
        
    def test_travel_costs(self):
        """ Test the total travel costs of the tours against given costs """
        tours = [[0, 6, 18, 5, 7, 2, 9, 15, 13, 17], [1, 10, 12, 14, 4, 11, 3, 8, 16]]
        costs = [108.73402552219146, 80.07544105166045]
        calculated_costs = []
        
        for tour in tours:
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += self.calculate_distance(tour[i], tour[i + 1])
            calculated_costs.append(total_cost)
        
        for provided_cost, calculated_cost in zip(costs, calculated_costs):
            self.assertAlmostEqual(provided_cost, calculated_cost, places=5)

# Running the test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)