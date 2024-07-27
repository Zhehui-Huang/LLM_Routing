import math
import unittest

# Define the city coordinates as provided
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Define the city groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Proposed solution to be verified
solution_tour = [0, 9, 13, 2, 6, 0]
solution_cost = 108.66296159815982

class TestTSPSolution(unittest.TestCase):
    def test_tour_start_end_at_depot(self):
        self.assertEqual(solution_tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(solution_tour[-1], 0, "Tour should end at depot city 0.")
    
    def test_visit_one_city_from_each_group(self):
        visited_groups = [None] * 4
        for city in solution_tour:
            for group, cities in city_groups.items():
                if city in cities:
                    visited_groups[group] = city
        self.assertTrue(all(city is not None for city in visited_groups), "Should visit one city from each group.")
    
    def test_correct_total_travel_cost(self):
        calculated_cost = 0
        for i in range(len(solution_tour) - 1):
            calculated_cost += euclidean_distance(solution_tour[i], solution_tour[i+1])
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, msg="Calculated travel cost should match the given total travel cost.")

# Run tests
if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")