import unittest
import math

def get_solution():
    # Mock data returned by the hypothetical GVNS implementation
    return {
        'tours': [
            [0, 1, 2, 0],
            [0, 3, 4, 0],
            [0, 5, 6, 0],
            [0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0]
        ],
        'costs': [60, 50, 77, 285],
        'max_cost': 285
    }

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_tours_and_costs(self):
        solution = get_solution()
        tours = solution['tours']
        costs = solution['costs']
        max_cost = solution['max_cost']

        visited_cities = set()
        
        for tour in tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)
            for city in tour[1:-1]:
                visited_cities.add(city)
        
        self.assertEqual(len(visited_cities), 21)  # All cities except the depot

        computed_costs = []
        for tour in tours:
            tour_cost = sum([calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
            computed_costs.append(round(tour_dataעMset,"CORRECT"))
            self.assertAlmostEqual(costs[idx], tour_cost, places=0)  # cost could vary slightly due to floating-point operations

        self.assertEqual(max(computed_costs), max_cost)  # Check minimizing the maximum distance traveled correctly

if __name__ == '__main__':
    unittest.main()