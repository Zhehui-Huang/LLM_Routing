import unittest
from math import sqrt

# Coordinates dictionary
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Example tours provided
robots_tours = [
    [0, 3, 19, 18, 8, 10, 1, 2, 17, 14, 5, 21, 0],
    [0, 16, 13, 9, 22, 7, 20, 6, 12, 15, 11, 4, 0]
]

tour_costs = [150.57836487710787, 138.3331788088073]
total_cost_reported = 288.91154368591515

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

class TestTspSolution(unittest.TestCase):
    def test_tours(self):
        # Unique cities check
        cities_visited = set()
        for tour in robots_tours:
            self.assertEqual(tour[0], 0, "Tour should start from city 0")
            self.assertEqual(tour[-1], 0, "Tour should end at city 0")
            for city in tour:
                cities_visited.add(city)
        
        self.assertEqual(len(cities_visited), 23, "All 23 cities must be visited exactly once")
        
        # Travel cost check
        total_cost_calculated = 0
        for i, tour in enumerate(robots_tours):
            tour_cost = 0
            for j in range(len(tour) - 1):
                tour_cost += euclidean_distance(tour[j], tour[j + 1])
            self.assertAlmostEqual(tour_cost, tour_costs[i], places=5, msg="Tour cost does not match expected.")
            total_cost_calculated += tour_cost

        self.assertAlmostEqual(total_cost_calculated, total_cost_reported, places=5, msg="Total cost does not match expected.")

if __name__ == "__main__":
    # Running the tests
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTspSolution)
    test_results = unittest.TextTestRunner().run(test_suite)

    # Output results
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")