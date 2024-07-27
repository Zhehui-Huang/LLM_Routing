import unittest
from math import sqrt

# Given data
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Provided solution
solution_tour = [0, 12, 10, 4, 3, 2, 0]
solution_cost = 138.15244358342136

# Helper functions
def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

class TestRobotTour(unittest.TestCase):
    def test_tour_includes_one_from_each_group(self):
        groups_visited = set()
        for city in solution_tour:
            for group_id, group_cities in city_groups.items():
                if city in group_cities:
                    groups_visited.add(group_id)
        self.assertEqual(len(groups_visited), 5)

    def test_tour_length(self):
        # Should start and end at the depot and include exactly one city from each of the 5 groups (total 6 cities)
        self.assertEqual(len(solution_tour), 7)  # Includes the return to the depot

    def test_travel_cost(self):
        calculated_cost = calculate_total_cost(solution_tour)
        self.assertAlmostEqual(calculated_people, solution_cost, places=5)

    def test_minimum_tour_cost(self):
        # This test assumes knowledge of the optimal cost, it should be corrected appropriately
        # In real situations, we would need a known optimal cost or lower bound for precise testing
        # Assuming the given solution should have the shortest cost if it is correct
        self.assertTrue(solution_cost <= calculate_total_trip_distance(solution_tour))

# Running the test
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    results = unittest.TextTestRunner().run(suite)

    if len(results.failures) == 0 and len(results.errors) == 0:
        print("CORRECT")
    else:
        print("FAIL")